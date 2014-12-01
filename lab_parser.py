import os, sys
from os import listdir
from os.path import isfile, join
from shutil import copyfile, move 
from functools import reduce


#########################################
## Backend Lab Parser for Berkeley BJC ##
#########################################


### Creates folders containing the necessary items to import into an edX course ###
### Should make a sequential file, a folder of vertical files, and a folder of html files ###



### trigger tags ###
	### set of tags that should note where a certain piece of info lies ###
	### please add to this set ### 
tags = {"title:", "resource:", "quiz:", "assignment:", "group:", "forum:", "video:", "reading:", "big-idea:", "learning-goal:"}
vertical_tags = {"resource:", "assignment:", "group:", "forum:"}
#NOTE: vertical_tag "quiz" is removed for now because quiz parser isn't working yet #

### helper functions ###

def prepare_file(filename, destination):
	path = destination + "/" + filename
	if os.path.exists(path):
		os.remove(path)
	with open(path, 'a') as f:
		os.utime(path, None)
	return path


def read_topicfile(filename):
	with open(filename, 'r') as content:
		return [x for x in [s.strip() for s in content.readlines()] if not x == '']


def get_content(line, start_char=None, end_char=None):
	"""Returns an additive string between two tags"""
	result = ''
	words = line.split()
	for word in words:
		if word not in tags and word!=start_char and word!=end_char:
			result += word + ' '
	return result[:-1]  


def insert_title(title, lines):
	for i in range(len(lines)):
		if "<body>" in lines[i]:
			lines.insert(i+1, '<h1>' + title + '</h1>')
			break
	return lines


def strip_quotes(name):
	return (name.replace('"', "")).replace("'", "")


def remove_comments(lines):
	"""Removes comments from the topic file"""
	result = []
	for line in lines:
		if not line.startswith('//'):
			line = line.rsplit('//', 1)[0] # removes inline comments
			result += [line]
	return result

def count_special(el_inline):
	"""Counts src and hrefs in a list line"""
	return len(list(filter(lambda x: "src" in x or "href" in x, el_inline)))

def separate_elements(el_inline):
	"""Separates list element of multiple links to several lists of one link"""
	if count_special(el_inline) < 2:
		return [el_inline] 
	else:
		end = [] 
		while count_special(el_inline)>1:	
			index = 0
			result = []
			while "src" not in el_inline[index] and "href" not in el_inline[index]:
				result += [el_inline[index]]
				index += 1 
			result += [el_inline[index]]
			end.append(result)
			el_inline = el_inline[index+1:]
		end.append(el_inline)
		return end 


def remove_whitespace(el_inline):
	"""Changes src = to src= in a split line"""
	result = []
	i = 0
	while i < len(el_inline):
		if el_inline[i] == "href" or el_inline[i] == "src":
			if el_inline[i+1] == "=":
				modded = el_inline[i] + el_inline[i+1] + el_inline[i+2]
				result.append(modded)
				i += 3
			else:
				modded = el_inline[i] + el_inline[i+1]
				result.append(modded)
				i += 2 
		elif el_inline[i] == "href=" or el_inline[i] == "src=":
			if (i + 1) == len(el_inline):
				result.append(el_inline[i])
				i += 1
			else:
				modded = el_inline[i] + el_inline[i+1]
				result.append(modded)
				i += 2
		else:
			result.append(el_inline[i])
			i += 1 
	return result 

def fix_links(lines):
	result = []
	for line in lines:
		if "href" in line:
			el_inline = line.split() 
			el_inline = remove_whitespace(el_inline)
			el_inline = separate_elements(el_inline)
			for el in el_inline:	
				index = 0
				href_exists = True
				while "href" not in el[index]:
					index += 1
					if index >= len(el):
						href_exists = False
						break
				if href_exists:
					relevant = el[index]
					if "http" in relevant:
						new_line = ' '.join(el)
						result.append(new_line)
					else:
						relevant = relevant.replace('href="', '')
						if "../" in relevant:
							modded_element = 'href=' + '"http://inst.eecs.berkeley.edu/~cs10/labs/' + relevant.replace("../", "")
						elif '/bjc-r' in relevant:
							modded_element = 'href=' + '"http://bjc.berkeley.edu' + relevant
						elif '#' in relevant:
							modded_element = 'href=' + relevant
						else:
							modded_element = 'href=' + '"http://bjc.berkeley.edu/' + relevant
						el[index] = modded_element
						new_line = ' '.join(el)
						result.append(new_line)
				else:
					pass
		
		elif "src" in line:
			el_inline = line.split() 
			el_inline = remove_whitespace(el_inline)
			el_inline = separate_elements(el_inline)
			for el in el_inline:			
				index = 0
				while "src" not in el[index]:
					index += 1
				relevant = el[index]
				if "http" in relevant:
					new_line = ' '.join(el)
					result.append(new_line)
				else:
					relevant = relevant.replace('src="', '')
					if "../" in relevant:
						modded_element = 'src=' + '"http://inst.eecs.berkeley.edu/~cs10/labs/' + relevant.replace("../", "")
					elif '/bjc-r' in relevant:
						modded_element = 'src=' + '"http://bjc.berkeley.edu' + relevant
					elif '#' in relevant:
						modded_element = 'src=' + relevant
					else:
						modded_element = 'src=' + '"http://bjc.berkeley.edu/' + relevant
					el[index] = modded_element
					new_line = ' '.join(el)
					result.append(new_line)
		else:
			result.append(line)
	return result 


def process_quiz(lines):
	new_lines = []
	start = lines.index("<html>")
	end = lines.index("<body>") + 1
	new_lines += lines[start:end]
	
	new_lines += ["<problem>"]
	start_index = lines.index('<div class="prompt">')
	for i in range(start_index, len(lines)):
		if lines[i] == '</div>':
			endx = i 
			break
	for line in lines[start_index:endx+1]:
		new_lines += [line]
	new_lines += ['<multiplechoiceresponse>', '<choicegroup type="MultipleChoice">']
	
	## finding correct choice ##
	for i in range(len(lines)):
		if 'class="correctResponse"' in lines[i]:
			c_index = i
			break
	correct_line = lines[c_index]
	f = lambda x: 'identifier' in x
	l = list(filter(f, correct_line.split()))[0]
	l = l.rsplit('=', 1)[1]
	correct_choice = l.rstrip('></div>')
	############################

	for i in range(len(lines)):
		line = lines[i]
		if '<div class="choice"' in line:
			choice = line.split()[2].rsplit('=', 1)[1].rstrip('>')
			inner_content = lines[i+2:i+3].pop()	
			if choice == correct_choice:
				new_lines += ['<choice correct="true">' + inner_content + "</choice>"]
			else:
				new_lines += ['<choice correct="false">' + inner_content + "</choice>"]
	new_lines += ['</choicegroup>', '</multiplechoiceresponse>', '<solution>']
	new_lines += ['<div class="detailed_solution">', '<p>Explanation</p>']

	### feedback ###
	for i in range(len(lines)):
		if 'identifier=' + correct_choice + '>' in lines[i]:
			start_index = i
			break
	k = start_index
	while k < len(lines):
		k += 1
		if "</div>" in lines[k]:
			endx = k
			break
	start_index = endx + 2
	k = start_index
	while k < len(lines):
		k += 1
		if "</div>" in lines[k]:
			endx = k
			break
	feedback = lines[start_index:endx]
	new_lines += feedback
	new_lines += ['</div>', '</solution>', '</problem>', '</body>', '</html>']
	return new_lines 


def insert_snap(lines):
	"""Inserts snap iframe to top of html page"""
	for i in range(len(lines)):
		if '<head>' in lines[i]:
			iframe = open("snap-frame.html", 'r')
			ilines = iframe.read()
			lines.insert(i, ilines)
			break
	return lines 



def make_html(line, destination):
	path = line.split()[-1]
	name = path[2:-1].rsplit('/', 1)[1][:-5]
	title = strip_quotes(get_content(line, None, path))

	output = prepare_file('html/' + name + ".html", destination)
	 

	## adding in a title for the lab ##
	copyfile(path[2:-1], output)
	with open(output, 'r') as content:
		lines = content.readlines()
	lines = insert_title(title, lines)
	
	### check for quiz ###
	for line in lines:
		if "assessment-data" in line:
				# lines = process_quiz(lines)

			break
		
	lines = fix_links(lines)
	lines = insert_snap(lines)
	lines = (' ').join(lines)
	with open(output, 'w') as new_html:
		new_html.write(lines)

def make_overview_html(name, lines, destination):
	def make_li(line):
		result = "<li>"
		result += get_content(line)
		return result + "</li>"

	with open(prepare_file("html/" + "overview-" + name + ".html", destination), 'a') as content:
		content.write("<html>\n")
		content.write("<h1>Overview</h1>\n")
		
		content.write("<h2>Big Ideas</h2>\n")
		content.write("<ul>\n")
		for line in lines:
			if line.split()[0] == "big-idea:":
				content.write(make_li(line) + "\n")
		content.write("</ul>\n")

		content.write("<h2>Activites</h2>\n")
		content.write("<ul>\n")
		for line in lines:
			if line.split()[0] == "learning-goal:":
				content.write(make_li(line) + "\n")
		content.write("</ul>\n")
		content.write("</html>")

def make_companion_xml(name, line, destination):
	"""Makes the corresponding xml file for an html file"""
	if line == 'Overview':
		with open(prepare_file('html/' + name + ".xml", destination), 'a') as target:
			target.write('<html filename="' + name + '" display_name="' + line + '"/>')	
	else:
		filename = line.split()[-1][2:-1].rsplit('/', 1)[1][:-5]
		title = strip_quotes(get_content(line, None, line.split()[-1]))
		with open(prepare_file('html/' + filename + ".xml", destination), 'a') as target:
			target.write('<html filename="' + filename + '" display_name="' + title + '"/>')	


def make_overview(name, output, destination):	
	output.write('  <vertical url_name="overview-' + name + '"/>\n')
	make_overview_html(name, remove_comments(read_topicfile(name + ".topic")), destination)
	make_companion_xml("overview-" + name, "Overview", destination)
	make_vertical("overview-" + name, None, destination)

def make_page(name, line, output, destination):
	output.write('  <vertical url_name="' + name + '"/>\n')
	## check for quiz here, and call make_quiz instead
	make_html(line, destination)
	make_companion_xml(name, line, destination)
	make_vertical(name, line, destination)


def make_vertical(name, line, destination):	
	def isSource(word):
		return word[0] == "["

	if line == None:
		title = "Overview"
		html_filename = "overview-" + name
	else:
		content = line.split()
		if isSource(content[-1]):
			title = strip_quotes(get_content(line, None, content[-1]))
			html_filename = content[-1][2:-1].rsplit('/', 1)[1][:-5]
		else:
			title = strip_quotes(get_content(line, None, None))
			# figure out what to make html_filename in the else case
	
	with open(prepare_file("vertical/" + name + ".xml", destination), 'a') as output:
		output.write('<vertical display_name="' + title + '">\n')
		output.write('  <html url_name="' + html_filename + '"/>\n')
		output.write("</vertical>")
	

def convert_lab(filename, destination):	
	dir_contents = os.listdir(destination)
	if 'course.xml' not in dir_contents:
		with open(destination + '/course.xml', 'w') as f:
			f.write('<course url_name="2014" org="BerkeleyX" course="CS__10"/>')
	if 'sequential' not in dir_contents:
		os.mkdir(destination + '/sequential')
	if 'vertical' not in dir_contents:
		os.mkdir(destination + '/vertical')
	if 'html' not in dir_contents:
		os.mkdir(destination + '/html')

	name = filename[:-6] # truncate .topic filename extention
	lines = remove_comments(read_topicfile(filename))
	with open(prepare_file("sequential/" + name + ".xml", destination), 'a') as seq:
		seq.write('<sequential display_name="Lab: ' + get_content(lines[0]) + '">\n')
		make_overview(name, seq, destination)
		for index in range(len(lines)):
			if lines[index].split()[0] in vertical_tags:
				page_name = name + "_" + str(index)
				make_page(page_name, lines[index], seq, destination)
		seq.write("</sequential>")
