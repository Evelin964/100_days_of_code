# we are going to create a miles to km converter and a km to miles converter
# using tkinter module
# this is part of day 27 of 100 days of code with Angela Yu


import tkinter as tk


window = tk.Tk()

window.title("Miles to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

label=tk.Label(text="is equal to",font=("Arial",24))
label.grid(column=0,row=0)
label.config(padx=20,pady=20)

def button_click():
    label['text']= imput.get()


def get_imput():
    print(imput.get())
    label['text']=imput.get()

button = tk.Button(text="Calculate",command=button_click)
button.grid(column=1,row=2)

imput = tk.Entry(width=10)
imput.grid(column=4,row=3)

new_button = tk.Button(text="New Button")
new_button.grid(column=2,row=0)


window.mainloop()


# def summing(*args):    
#     sum=0
#     for n in args:
#         sum+= n
#     return sum

# alba=summing(1,2,3,4,5)
# print(alba)


# def calculate(n,**kwargs):
#     print(kwargs)
#     n+=kwargs["add"]
#     n*=kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)

# class car():
#     def __init__(self, **kw):
#         self.make=kw.get("make")
#         self.model=kw.get("model")
#         self.color=kw.get("color")
#         self.seats=kw.get("seats")
        
        
        
# my_car=car(make="Nissan", model="GT-R")
# print(my_car.model)