THEME_COLOR = "#375362"
from tkinter import *
import time

class UI:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.att = 0
        self.question = ""

        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(width=300, height=400, background="grey", padx=10, pady=10)

        self.q_canvas = Canvas()
        self.q_canvas.config(width=300, height=200, background="blue")
        self.q_text = self.q_canvas.create_text(
            150, 100, 
            width=280,
            text=self.question, 
            fill="white",
            font=("Arial", 14, "italic")
        )
        self.q_canvas.grid(column=0, row=1, columnspan=2, pady=10)

        self.t_image = PhotoImage(file=r"images\true.png")
        self.t_button = Button(
            image=self.t_image, 
            height=100, 
            width=100, 
            background="grey", 
            highlightthickness=0,
            command=self.true_pressed
        )
        self.t_button.grid(row=2, column=0)

        self.f_image = PhotoImage(file=r"images\false.png")
        self.f_button = Button(
            image=self.f_image, 
            height=100, 
            width=100, 
            background="grey", 
            highlightthickness=0,
            command=self.false_pressed
        )
        self.f_button.grid(row=2, column=1)

        self.score_label = Label(text="Score: 0", background="grey", font=("Arial", 12, "bold"))
        self.score_label.grid(row=0, column=0)

        self.q_label = Label(text="Question: 0/0", background="grey", font=("Arial", 12, "bold"))
        self.q_label.grid(row=0, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.q_canvas.config(background="blue")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.q_label.config(text=f"Question: {self.quiz.question_number}/{len(self.quiz.question_list)}")
            
            q_text = self.quiz.next_question()
            self.q_canvas.itemconfig(self.q_text, text=q_text)
            self.enable_buttons()
        else:
            self.q_canvas.itemconfig(self.q_text, text="You've completed the quiz!")
            self.q_canvas.config(background="blue")
            self.q_label.config(text=f"Total: {len(self.quiz.question_list)}")
            self.score_label.config(text=f"Final Score: {self.quiz.score}")
            self.disable_buttons()
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        
    def give_feedback(self, is_right):
        self.disable_buttons()
        if is_right:
            self.green_flick()
        else:
            self.red_flick()
        self.window.after(1000, self.get_next_question)
        
    def enable_buttons(self):
        self.t_button.config(state="normal")
        self.f_button.config(state="normal")
        
    def disable_buttons(self):
        self.t_button.config(state="disabled")
        self.f_button.config(state="disabled")

    def green_flick(self):
        self.q_canvas.config(background="green")
        time.sleep(0.5)
        self.q_canvas.config(background="blue")

    def red_flick(self):
        self.q_canvas.config(background="red")
        time.sleep(0.5)
        self.q_canvas.config(background="blue")

    def score(self, scr):
        self.score_label.config(text=f"Score : {scr}")
        self.q_label.config(text=f"Attempted : {0}")
        

    def no_score():
        pass
