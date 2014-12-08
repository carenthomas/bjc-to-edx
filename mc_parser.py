from bs4 import BeautifulSoup

test_path = "bjc-r/cur/programming/algorithms/timing/quiz-searching-through-time.html"
soup = BeautifulSoup(open(test_path))
prompt = soup.find("div", { "class" : "prompt" }).get_text()
correct_answer = soup.find("div", { "class" : "correctResponse" })
answer_list = soup.findAll("div", { "class" : "text" })
q = []
for i in range(len(answer_list)):
	q.append(answer_list[i].get_text())


def mc_parser(file):
	a = open(str(file)).read()
	problem_display_markdown = ''


	problem_display_tag = '<problem display_name="Multiple Choice" markdown="' + problem_display_markdown + '">'
	print soup


	#return a