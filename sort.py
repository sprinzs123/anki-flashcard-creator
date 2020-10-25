import random

with open('large.txt', encoding="utf8") as questions:
    fullText = questions.read()
text = fullText


# returns at what indexes word 'Question' starts
def string_index_find():
    question_start = []
    for index, letter in enumerate(text):
        if letter == 'Q':
            if text[index: index + 8] == 'Question':
                question_start.append(index)
    return question_start


def make_questions():
    questions_list = []
    question_indexes = string_index_find()
    for letter in range(0, len(question_indexes) - 1):
        start = question_indexes[letter]
        end = question_indexes[letter + 1]
        one_question = text[start:end]
        questions_list.append(one_question)
    questions_list.append(text[question_indexes[-1]: -1])
    return questions_list

# make_questions()


class GatherData:
    def __init__(self, question):
        self.question = question

    def get_question(self):
        lst_break = self.question.split('\n')
        return lst_break[1]


    def get_explanation(self):
        lst_break = self.question.split('\n')
        explanation_list = lst_break[2:]
        explanation_str = ''
        for line in explanation_list:
            explanation_str += line + '\n'
        return explanation_str

    def get_wrong_questions(self):
        question_lst = []
        lst_break = self.question.split('\n')
        for paragraph in lst_break:
            if '. is not right.' in paragraph:
                question_lst.append(paragraph)
        sanitized_questions = []
        for question in question_lst:
            sanitized_questions.append(question[0:-14])
        return sanitized_questions

    def get_correct_question(self):
        question_lst = []
        lst_break = self.question.split('\n')
        for paragraph in lst_break:
            if paragraph.endswith('. is the right answer.'):
                question_lst.append(paragraph)
        sanitized_questions = []
        answer = question_lst[0][0:-21]
        fin = []
        fin.append(answer)
        return fin

    def randomize_questions(self):
        correct = self.get_correct_question()
        wrong = self.get_wrong_questions()
        all_questions = correct + wrong
        random.shuffle(all_questions)
        return all_questions


def make_question(question, answers):
    str_question = ''
    str_question += '"' + question + '\n' + '\n'
    for answer in answers:
        str_question += '-' + answer + '\n'
    str_question += '"'
    return str_question


def make_answer(answer, description):
    str_answer = ''
    str_answer += '"' + answer + '\n' + '\n'
    str_answer += description
    str_answer += '"'
    return str_answer


# trigers class that finds all relevant info
def record_data():
    full_set = ''
    found_question = make_questions()
    for count, question in enumerate(found_question):
        if '. is the right answer.' in question:
            print('working on ' + str(count + 1))
            finding = GatherData(question)
            full_question = finding.get_question()
            all_questions = finding.randomize_questions()
            full_expanation = finding.get_explanation()
            answer = finding.get_correct_question()[0]
            question_card = make_question(full_question, all_questions)
            answer_card = make_answer(answer, full_expanation)
            full_card = question_card + ';' + answer_card
            full_set += full_card
        print(full_set)
record_data()