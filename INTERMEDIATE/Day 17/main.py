from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
# {"text": "A slug's blood is green.", "answer": "True"}
for dict in question_data:
    new_text=dict["text"]
    new_answer=dict["answer"]
    questioN=Question(new_text,new_answer)
    question_bank.append(questioN)

quiz=QuizBrain(question_bank)

while quiz.is_still_question():
    quiz.next_question()


