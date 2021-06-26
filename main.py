from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for i in question_data:
    new_question = Question(i["question"], i["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
