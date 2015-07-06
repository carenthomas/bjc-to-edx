#! /usr/bin/env python3

from bs4 import BeautifulSoup


def make_quiz(source, destination):
    """
    Extracting from bjc file
    """

    filename = source.rsplit('/', 1)[1]
    test_path = source
    soup = BeautifulSoup(open(test_path))

    """
    make sure this is a multiple choice quiz
    """

    if soup.find("div", { "class" : "prompt" }) == None:
        return

    prompt = ((soup.find("div", { "class" : "prompt" }).get_text()).encode('utf-8', "ignore")).strip()
    correct_answer_tag = soup.find("div", { "class" : "correctResponse" })
    correct_answer = ((soup.find(identifier=correct_answer_tag['identifier']).find("div", { "class" : "text" }).get_text()).encode('utf-8', "ignore")).strip()
    answer_list_unf = soup.findAll("div", { "class" : "text" })
    answer_list = []
    for a in answer_list_unf:
        answer_list.append(((a.get_text()).encode('utf-8', "ignore")).strip())

    feedback_list_unf = soup.findAll("div", { "class" : "feedback" })
    feedback_list = []
    for f in feedback_list_unf:
        feedback_list.append(((f.get_text()).encode('utf-8', "ignore")).strip())

    """
    Formatting for xml
    """

    xml_mul = ""
    for answer in answer_list:
        if answer == correct_answer:
            xml_mul += "<    choice correct=\"true\">" + str(answer) + "</choice>\n"
        else:
            xml_mul += "<    choice correct=\"false\">" + str(answer) + "</choice>\n"

    xml_out =     "<problem>\n" + \
                "<p>" + str(prompt) + "</p>\n" + \
                "<multiplechoiceresponse>\n" + \
                "  <choicegroup type=\"MultipleChoice\">\n" + \
                str(xml_mul) + \
                "  </choicegroup>\n" + \
                "</multiplechoiceresponse>\n\n" + \
                "<solution>\n" + \
                "<div class=\"detailed-solution\">\n" + \
                "<p>Explanation</p>\n" + \
                "<p>" + str(feedback_list[answer_list.index(correct_answer)]) + "</p>\n" + \
                "</div>\n" + \
                "</solution>\n" + \
                "</problem>\n"


    output = destination + '/problem/' + filename[:-5] + ".xml"
    # print(output)
    with open(output, 'w+') as xml_file:
        xml_file.write(xml_out)


# make_quiz('curriculum/bjc-r/cur/programming/intro/snap/test-yourself-go-team.html', 'Course')




