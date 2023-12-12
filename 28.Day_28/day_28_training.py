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

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer_running, nr_pomadoro, timer
    window.after_cancel(action_id)  # Cancel the ongoing timer
    timer_running = False
    nr_pomadoro = 0
    timer = WORK_MIN * 60
    timer_label.config(text="00:00")
    pommadoro_count.config(text=f"{nr_pomadoro}✅")
    status_label.config(text="Timer!")

       
       
    
    
      


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global timer_running, nr_pomadoro, timer
    if not timer_running:
        timer_running = True
        nr_pomadoro = 1
        timer = 1 * 60
        work_label()
        pommadoro_count_label(nr_pomadoro)
        timer_pomadoro()

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def timer_pomadoro():
    global timer, timer_running, nr_pomadoro
    if timer_running:
        minutes, seconds = divmod(timer, 60)
        timer_label.config(text=f"{minutes}:{seconds:02d}")
        if timer > 0:
            timer -= 1
            window.after(1000, timer_pomadoro)
            
        #------- jos intr-o functie
        else:
        # timer_label.config(text="Time's up!")
        # timer_running = False
            
            if nr_pomadoro % 2 == 0:  # Break time
                if nr_pomadoro == 4:
                    timer = 1 * 60
                    nr_pomadoro = 0
                else:
                    timer = 2 * 60
                pause_label()
            else:  # Work time
                timer = WORK_MIN * 60
                work_label()
            nr_pomadoro += 1
            pommadoro_count_label(nr_pomadoro)
    else:
        pass

            

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Pomodoro")
window.minsize(width=400, height=400)
window.config(bg="lightblue")
window.resizable(width=False, height=False)



bg_image = Image.open(r"28.Day_28/tomato.png")
bg_image = bg_image.resize((150, 150), Image.ANTIALIAS)
bg_photo = ImageTk.PhotoImage(bg_image)

image_x = (window.winfo_reqwidth() + 60) // 2
image_y = (window.winfo_reqheight() - 100) // 2

bg_label = tk.Label(window,image=bg_photo,bg="lightblue")
bg_label.place(x=image_x, y=image_y)


    
start_button = tk.Button(text="Start", bg="lightgrey",command=start_timer)
start_button.place(x=50, y=300)
start_button.config(padx=5, pady=0)

reset_button = tk.Button(window,text="Reset", bg="lightgrey",command=reset_timer)
reset_button.place(x=300, y=300)
reset_button.config(padx=5, pady=0)


timer_label = tk.Label(window, bg='lightblue', font=("Arial", 20, "bold"),text="00:00")
timer_label.place(x=160, y=250)
timer_label.config(padx=0, pady=0)


status_label = tk.Label(text="Timer!a", bg='lightblue', font=("Arial", 20))
status_label.place(x=150, y=205)
status_label.config(padx=0, pady=0)

pommadoro_count = tk.Label(text="", bg='lightblue', font=("Arial", 20))
pommadoro_count.place(x=80, y=350)
pommadoro_count.config(padx=0, pady=0)


def pommadoro_count_label(nr_pomadoro):
    pommadoro_count.config(text=f"{nr_pomadoro}✅",bg='lightblue')
    pommadoro_count.place(x=170, y=350)

def update_status_label(text):
    status_label.config(text=text)

def work_label():
    update_status_label("Work!")
    status_label.place(x=160, y=205)
def pause_label():
    update_status_label("Pause!")
    
def timer_label_funct():
    update_status_label("Timer!")
    status_label.place(x=160, y=205)




reset_time = False
timer_running = False
nr_pomadoro = 0
timer = 3 * 60



 


action_id = window.after(1000, timer_pomadoro)
# reset_button.after_cancel(action_id)

window.mainloop()
