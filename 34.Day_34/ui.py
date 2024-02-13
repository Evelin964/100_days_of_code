THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain
from data import question_data

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.window.resizable(False, False)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        self.score_label.grid(row=0, column=2)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", width=280, font=("Arial", 20, "italic"),fill=THEME_COLOR)
        self.canvas.grid(row=1, column=1, columnspan=2, pady=20)
        
        true_image = PhotoImage(file="34.Day_34/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=2,padx=20, pady=10)
        
        false_image = PhotoImage(file="34.Day_34/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1,padx=20, pady=10)
        
       
        
        self.get_next_question()
      
      
        
        self.window.mainloop()
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
    
    def check_end_game(self):
        if self.quiz.still_has_questions() == False:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
    
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.check_end_game()
        q_text = self.quiz.next_question()
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.itemconfig(self.question_text, text=q_text)
        
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    


