class QuizBrain:

    def __init__(self, q_list):
        self.q_list = q_list
        self.question_number=0
        self.score=0

    def is_still_question(self):
        if len(self.q_list)==self.question_number:
            return False
        else:
            return True


    def check_answer(self,user,ans):
        if user == ans:
            print("You Are Right")
            self.score += 1
        else:
            print("You are wrong")
        print(f"Correct answer was {ans}")

        print(f"Your score if {self.score}/{self.question_number}")

    def next_question(self):
        new_q = self.q_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q{self.question_number}: {new_q.text}.(True/False)")
        self.check_answer(user_choice, new_q.answer)



