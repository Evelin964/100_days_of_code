"""This is my day 18 project from Dr Angela Yu 100 days of code course.
    """
import turtle
import random
import colorgram
from PIL import Image


# Specify the image path
image_path = r"C:\Users\ediacon\OneDrive - MORNINGSTAR INC\Documents\Python Scripts\02.100 Days of Python\18.Day_18\spots.jpeg"

# Extract colors from the image
colors_list = []
colors = colorgram.extract(image_path, number_of_colors=90)

for color in colors:
    rgb = (color.rgb.r / 255.0, color.rgb.g / 255.0, color.rgb.b / 255.0)
    colors_list.append(rgb)

# Set dot size and spacing
dot_size = 20
dot_nr = 10

# Create a Turtle object
t = turtle.Turtle()


for i in range(10):
    if i == 0:
        t.hideturtle()
        t.penup()
        t.setheading(225)
        t.forward(300)
        t.setheading(0)
        t.pendown()
        t.hideturtle()
    t.speed("fastest")
    t.hideturtle()
    for _ in range(10):
        t.speed("fastest")
        t.dot(dot_size, random.choice(colors_list))
        t.penup()
        t.forward(50)
        t.pendown()
    t.penup()
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)
    t.pendown()
# Save the turtle graphics canvas as a PostScript file
canvas = turtle.getcanvas()
canvas.postscript(file="output.eps", colormode="color")

# Convert the PostScript file to a PNG image using Pillow
output_file_path = r"C:\Users\ediacon\OneDrive - MORNINGSTAR INC\Documents\Python Scripts\02.100 Days of Python\18.Day_18\output.png"
img = ImageGrab.grab(bbox=turtle.getcanvas().winfo_rootx(), turtle.getcanvas().winfo_rooty(),
                     turtle.getcanvas().winfo_width() + turtle.getcanvas().winfo_rootx(),
                     turtle.getcanvas().winfo_height() + turtle.getcanvas().winfo_rooty())
img.save(output_file_path)

turtle.done()
