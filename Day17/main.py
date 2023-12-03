from question_model import Question
from data import question_data, question_data_2
from quiz_brain import QuizBrain


question_bank = []
for item in question_data_2:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)
quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_questions():
    quiz_brain.next_question()
print("You'he completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number}")
