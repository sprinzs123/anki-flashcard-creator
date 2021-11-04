# is is to make flashcards that are question answer
# question answer is separated by line break and Q and A separated by " - "
# "deffininion - answer" format for all questions


### Configuration setting ###

# delimeters by which flashcard are going to be created
# global variables, can be changed depending on the format
questions_separate = ';'
question_answer_separate = '='
question_index = 0  
answer_index = 1


# location of input and output files 
# can modify depending on folder location
input_file_path= "C:\\Users\\cooke\\Desktop\\projects\\anki\\anki-flashcard-creator\\input.txt"
output_file_path = 'C:\\Users\\cooke\\Desktop\\projects\\anki\\anki-flashcard-creator\\done_cards.txt'

# file that reading information from
with open(input_file_path, encoding="utf8") as questions:
    fullText = questions.read()
text = fullText

### end of configuration settings


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
        all_cards_list = []       
        for i in range(len(self.answer_list)):
            question_str = '"' + self.question_list[i].strip() + '"'
            answer_str = '"' + self.answer_list[i].strip() + '"'
            full_card = question_str + ';' + answer_str + '\n\n'
            all_cards_list.append(full_card)

        
        unique_cards = list(set(all_cards_list))
        print(str(len(unique_cards)) + ' cards found')
        return ''.join(unique_cards)
        
    # write the output of all string representation of flash cards to a text file
    # output file path is in configurations
    def write_to_file(self):
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(self.get_str_output())
            


new_cards = QuestionFound(text)
new_cards.separate_item()
new_cards.write_to_file()