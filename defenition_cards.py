# is is to make flashcards that are question answer
# question answer is separated by line break and Q and A separated by " - "
# "deffininion - answer" format for all questions

import os

# delimeters by which flashcard are going to be created
# global variables, can be changed depending on the format
questions_separate = '\n'
question_answer_separate = '='
question_index = 0  
answer_index = 1

with open("C:\\Users\cooke\\Desktop\\projects\\anki\\anki-flashcard-creator\\input.txt", encoding="utf8") as questions:
    fullText = questions.read()
text = fullText


class QuestionFound:
    def __init__(self, text):
        self.text = text
        self.question_list = []
        self.answer_list = []

    # separate text by question and answer using new line
    # then futher separate by question and answer and append to lists
    # add question and answers to their lists
    def separate_item(self):
        broken_text = self.text.split(questions_separate)
        for full_flashcard in broken_text:
            question_answer = full_flashcard.split(question_answer_separate)
            if len(question_answer) == 2:                
                self.question_list.append(question_answer[question_index])
                self.answer_list.append(question_answer[answer_index])

    # for loop over answers and questions and format string
    # so that can get into anki flashcard format
    def get_str_output(self):        
        for i in range(len(self.answer_list)):
            question_str = '"' + self.question_list[i] + '"'
            answer_str = '"' + self.answer_list[i] + '"'
            full_card = question_str + ';' + answer_str
            print(full_card)


new_cards = QuestionFound(text)
new_cards.separate_item()
new_cards.get_str_output()