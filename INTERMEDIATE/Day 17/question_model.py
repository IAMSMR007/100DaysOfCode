class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer
question=Question("2+2=4","True")
print(question.answer)