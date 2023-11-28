"""This is a program that converts miles to km and km to miles from Dr. Angela Yu's 100 days of code course.
Using Tkinter module
"""


import tkinter as tk

Window = tk.Tk()
Window.title("Miles to Km Converter")
Window.minsize(width=300, height=300,)
Window.config(padx=20, pady=20)
Window.configure(bg="lightblue")
Window.resizable(width=False, height=False)


def miles_to_km():
    miles = float(miles_input.get())
    km = (miles * 1.609).__round__(2)
    km_result_label.config(text=f"{km}")

def km_to_miles():
    km = float(km_input.get())
    miles = (km / 1.609).__round__(2)
    km_result_imput_label.config(text=f"{miles}")

miles_input = tk.Entry(width=10)
miles_input.grid(column=2, row=0)
miles_input.focus()
miles_input.configure(bg="lightgrey")


miles_label = tk.Label(text="Miles")
miles_label.grid(column=3, row=0)
miles_label.config(padx=10, pady=10)
miles_label.configure(bg="lightblue")

km_result_label = tk.Label(text="0")
km_result_label.grid(column=2, row=1)
km_result_label.configure(bg="lightblue")

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
is_equal_label.configure(bg="lightblue")


km_label = tk.Label(text="Km")
km_label.grid(column=3, row=1)
km_label.configure(bg="lightblue")

button = tk.Button(text="Calculate", command=miles_to_km)
button.grid(column=4, row=2)
button.config(padx=5, pady=5)
button.configure(bg="lightgrey")



km_input = tk.Entry(width=10)
km_input.grid(column=2, row=3)
km_input.configure(bg="lightgrey")

km_imput_label = tk.Label(text="Km")
km_imput_label.grid(column=3, row=3)
km_imput_label.config(padx=10, pady=10)
km_imput_label.configure(bg="lightblue")

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(column=0, row=4)
is_equal_label.configure(bg="lightblue")

miles_label = tk.Label(text="Miles")
miles_label.grid(column=3, row=4)
miles_label.configure(bg="lightblue")

button_2 = tk.Button(text="Calculate", command=km_to_miles)
button_2.grid(column=4, row=5)
button_2.config(padx=5, pady=5)
button_2.configure(bg="lightgrey")

km_result_imput_label = tk.Label(text="0")
km_result_imput_label.grid(column=2, row=4)
km_result_imput_label.configure(bg="lightblue")



Window.mainloop()