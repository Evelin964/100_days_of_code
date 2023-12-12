"""This is a program that will help you to focus on your work by using the Pomodoro Technique.
From Dr. Angela Yu 100 Days of Code - Day 28 - Intermediate+ Tkinter
"""


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

import tkinter as tk
from PIL import Image, ImageTk
import time



class Pomadoro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.config(padx=10, pady=10, bg=YELLOW)
        self.resizable(False, False)
        self.display_status_text_label = "Timer!"
        self.nr_pomadoro_completed = 0
        self.create_timer_canvas()
        self.create_status_label()
        self.create_start_button()
        self.create_reset_button()
        
        self.timer_running = None
        
    
    
    def timer_type(self):
        if self.display_status_text_label == " Work!":
            if self.nr_pomadoro_completed < 3:
                # After a work period, initiate a short break
                self.timer = int(SHORT_BREAK_MIN * 60)
                self.display_status_text_label = " Short Break!"
                self.nr_pomadoro_completed += 1
            else:
                # After the fourth work period, initiate a long break
                self.nr_pomadoro_completed += 1
                self.timer = int(LONG_BREAK_MIN * 60)
                self.display_status_text_label = " Long Break!"
                
        elif self.display_status_text_label == " Short Break!":
            # After a short break, initiate a work period
            self.timer = int(WORK_MIN * 60)
            self.display_status_text_label = " Work!"

        self.pommadoro_count_label(self.nr_pomadoro_completed)
        self.update_status_label(self.display_status_text_label)
        self.timer_countdown(self.timer)

    def timer_countdown(self, count):
        minutes, seconds = divmod(count, 60)
        self.timer_canvas.itemconfig(self.timer_label, text=f"{minutes}:{seconds:02d}")
        if count > 0 and self.timer_running is True:
            self.action_id = self.after(1000, self.timer_countdown, count - 1)
        elif self.nr_pomadoro_completed < 4:
            self.attributes('-topmost',1)
            self.attributes('-topmost',0)
            self.timer_type()
        else:
            self.reset_timer()
            
    
    
    def start_timer(self):
        if self.display_status_text_label == "Timer!":
            self.timer_running = True
            
            self.timer = int(WORK_MIN * 60)
            self.display_status_text_label = " Work!"
            self.update_status_label(self.display_status_text_label)
             
            self.timer_countdown(self.timer)
    def pommadoro_count_label(self, nr_pomadoro_completed):
    # Initialize the label if it doesn't exist yet
        if not hasattr(self, 'pommadoro_count'):
            self.pommadoro_count = tk.Label(self, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
            self.pommadoro_count.grid(column=1, row=2)

        # Update the label with the correct number of check marks
        self.pommadoro_count.config(text="✅" * nr_pomadoro_completed)
            
    def reset_timer(self):
        if self.display_status_text_label != "Timer!":
            self.after_cancel(self.action_id)
            self.timer_running = None
            self.nr_pomadoro_completed = 0
            
            self.timer_canvas.itemconfig(self.timer_label, text="00:00")
            self.status_label.config(text="Timer!")
            self.display_status_text_label = "Timer!"
            self.pommadoro_count_label(self.nr_pomadoro_completed)        
        
            
      
    def update_status_label(self, display_status_text_label):
        self.status_label.config(text=display_status_text_label)   
        
    def create_reset_button(self):
        self.reset_button = tk.Button(text="Reset", highlightthickness=0,padx=10,pady=10, command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)    
        
    def create_start_button(self):
        self.start_button = tk.Button(text="Start", highlightthickness=0,padx=10,pady=10, command=self.start_timer)
        self.start_button.grid(column=0, row=2)    
        
    def create_status_label(self):
        self.status_label = tk.Label(text=self.display_status_text_label, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
        self.status_label.grid(column=1, row=0)

    def create_timer_canvas(self):
        # Load and resize the tomato image
        tomato_img = Image.open("28.Day_28/tomato.png")
        tomato_img = tomato_img.resize((200, 200))
        tomato_photo = ImageTk.PhotoImage(tomato_img)

        # Create a Canvas and add the image
        self.timer_canvas = tk.Canvas(self, width=400, height=250, bg=YELLOW, highlightthickness=0)
        self.timer_canvas.create_image(200, 100, image=tomato_photo)  # Adjust coordinates as needed
        self.timer_canvas.image = tomato_photo  # Keep a reference to the image

        # Add timer text over the image
        self.timer_label = self.timer_canvas.create_text(200, 120, text="00:00", fill=YELLOW, font=(FONT_NAME, 35, "bold"))
        self.timer_canvas.grid(column=1, row=1)

if __name__ == "__main__":
    pomadoro = Pomadoro()
    pomadoro.mainloop()
    
    