"""This is day 29 of Angela Yu's 100 Days of Python course on Udemy.
    This is a password manager program that uses a GUI to store passwords.
    """
    
import tkinter as tk

def create_rounded_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def on_button_click():
    print("Button clicked!")

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Create rounded button
button = create_rounded_rect(canvas, 50, 25, 150, 75, radius=20, fill="blue")
text = canvas.create_text(100, 50, text="Click Me", fill="white")

# Bind the click event
canvas.tag_bind(button, "<Button-1>", lambda x: on_button_click())
canvas.tag_bind(text, "<Button-1>", lambda x: on_button_click())

root.mainloop()
