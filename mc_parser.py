from bs4 import BeautifulSoup

"""
Extracting from bjc file
"""
test_path = "bjc-r/cur/programming/algorithms/timing/quiz-searching-through-time.html"
soup = BeautifulSoup(open(test_path))
prompt = str(soup.find("div", { "class" : "prompt" }).get_text()).strip()
correct_answer_tag = soup.find("div", { "class" : "correctResponse" })
correct_answer = soup.find(identifier=correct_answer_tag['identifier']).find("div", { "class" : "text" }).get_text().strip()
answer_list_unf = soup.findAll("div", { "class" : "text" })
answer_list = []
for a in answer_list_unf:
	answer_list.append(a.get_text().strip())

feedback_list_unf = soup.findAll("div", { "class" : "feedback" })
feedback_list = []
for f in feedback_list_unf:
	feedback_list.append(f.get_text().strip())
	
"""
Formatting for xml
"""

xml_mul = ""
for answer in answer_list:
	if answer == correct_answer:
		xml_mul += "<choice correct=\"true\">" + answer + "</choice>\n"
	else:
		xml_mul += "<choice correct=\"false\">" + answer + "</choice>\n"

xml_out = 	"<problem>"
			"<p>" + prompt + "</p>\n" + \
			"<multiplechoiceresponse>\n" + \
			"<choicegroup type=\"MultipleChoice\">\n" + \
			xml_mul + \
			"</choicegroup>\n" + \
			"</multiplechoiceresponse>\n" + \
			"<solution>\n" + \
			"<div class=\"detailed-solution\">\n" + \
			"<p>Explanation</p>\n" + \
			"<p>" + feedback_list[answer_list.index(correct_answer)] + "</p>\n" +\
			"</div>\n" + \
			"</solution>\n" + \
			"</problem>"

xml_file = open('quiz-searching-through-time.xml', 'w+')
xml_file.write(xml_out)
xml_file.close()