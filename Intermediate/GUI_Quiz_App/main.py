from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

parameters = {
    "amount": 10,
    "difficulty": "medium",
    "type": "boolean"
}

quiz_data = requests.get("https://opentdb.com/api.php", params= parameters)
quiz_data.raise_for_status()
questions_list = quiz_data.json()["results"]

question_bank = []

for q_set in questions_list:

    question_text = q_set["question"]
    question_answer = q_set["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)
