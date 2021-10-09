from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question['question']
    q_answer = question['correct_answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)
# for index in range(len(question_data)):
#     for key in question_data[index]:
#         print(question_data[index][key])
#         q = Question(question_data[index], question_data[index][key])
#         question_bank.append(q)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
