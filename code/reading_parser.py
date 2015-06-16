import shutil, os, re

def convert_readings(destination):
	if not os.path.exists(os.getcwd() + '/readings/reading-locations.txt'):
		print('ERROR: file with locations not found in current directory.')
		return
	
	with open('readings/reading-locations.txt', 'r') as locations:
		readinglist = locations.readlines()

	currentweek = None
	skip = False
	for item in readinglist:
		if 'Week' in item:
			if currentweek and not skip:
				with open(destination + '/sequential/' + currentweek + '-readings.xml', 'a') as seq:
					seq.write('</sequential>')

			currentweek = (item.strip("\n")).replace(" ", "")[0:-1]
			if "No Readings" in item:
				skip = True
			else:
				with open(destination + '/chapter/' + currentweek + '.xml', 'a') as chapter:
					chapter.write(' <sequential url_name="' + currentweek + '-readings"/>\n')
		elif item == '\n':
			pass
		else:
			skip = False
			temp = item.rsplit(" ", 1)
			title = temp[0]
			location = temp[1].strip("\n")
			location = location[1:-1]
			name = re.sub('[\W_]+', '', title.replace(" ", "-"))
			if not os.path.exists(os.getcwd() + '/' + destination + '/sequential/' + currentweek + '-readings.xml'):
				with open(destination + '/sequential/' + currentweek + '-readings.xml', 'w') as seq:
					seq.write('<sequential display_name="Readings">\n')
			with open(destination + '/sequential/' + currentweek + '-readings.xml', 'a') as seq:
				seq.write('  <vertical url_name="' + name + '"/>\n')

			
			with open(destination + '/vertical/' + name + '.xml', 'w') as vertical:
				vertical.write('<vertical display_name="' + title + '">\n')
				vertical.write('  <html url_name="Reading-' + name + '"/>\n')
				vertical.write('</vertical>')

			if "files/" in location:
				with open(destination + '/html/Reading-' + name + '.html', 'w') as html:
					html.write('<p>' + title + '<a href="/static/' + location.split("/", 1)[1] + '" target="_blank"><button>Download</button></a></p>')
					shutil.copyfile(os.getcwd() + '/readings/' + location, destination + '/static/' + location.split("/", 1)[1])
			else:
				with open(destination + '/html/Reading-' + name + '.html', 'w') as html:
					html.write('<p><iframe src="' + location + '" width="100%" height="800"></iframe></p>')

			with open(destination + '/html/Reading-' + name + '.xml', 'w') as companion_xml:
				companion_xml.write('<html filename="reading-' + name + '" display_name="' + title + '"/>')

	#close last sequential file	
	if not skip:		
		with open(destination + '/sequential/' + currentweek + '-readings.xml', 'a') as seq:
			seq.write('</sequential>\n')

				

