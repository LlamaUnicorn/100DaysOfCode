class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

# TODO: Retrieve the item at the current question_number from the question_list.
# TODO: Use the input() function to show the user the Question text and ask for the user's answer
    def still_has_questions(self):

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ask_user = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")


