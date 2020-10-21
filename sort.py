import random

with open('input.txt', encoding="utf8") as questions:
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

    def get_question_end(self):
        return self.question.find('Explanation')

    def get_question(self):
        question_start = self.question.find('\n')
        question_end = self.get_question_end()
        end_question = self.get_question_end()
        return self.question[question_start:question_end]

    def get_explanation(self):
        start = self.get_question_end()
        return self.question[start:]

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



# trigers class that finds all relevant info
def record_data():
    found_question = make_questions()
    for question in found_question:
        finding = GatherData(question)
        finding.get_question_end()
        full_question = finding.get_question()
        full_expanation = finding.get_explanation()
        answer = finding.get_correct_question()
        all_questions = finding.randomize_questions()

record_data()