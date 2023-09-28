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
img = Image.open("output.eps")
img.save("output.png", "PNG")

turtle.done()


# t = turtle.Turtle()
# for i in range(nr_colors):
#     if i % 2 == 0:


#     t.penup()
#     t.hideturtle()
#     t.setheading(180)
#     t.forward(40)
#     t.setheading(0)
#     t.pencolor("red")
#     t.dot(20)
#     t.forward(10)


# for i in range(4):
#     if i % 2 == 0:
#         for _ in range(5):
#             t.forward(dash_lenght)
#             t.penup()
#             t.forward(dash_lenght)
#             t.pendown()
#     else:
#         t.forward(100)
#     t.right(90)

# Set the turtle shape to a custom image (replace 'green_turtle.gif' with your image file)

# t.shape("turtle")
# t.color("green")
# t.width(5)
# radius = 100

# for _ in range(36):
#     t.circle(radius)
#     t.right(10)
#     tuple_color = (
#         random.uniform(0, 1),
#         random.uniform(0, 1),
#         random.uniform(0, 1),
#     )
#     t.pencolor(tuple_color)


# while True:

#     t.circle(radius)
#     t.right(10)

# while True:
#     tuple_color = (
#         random.uniform(0, 1),
#         random.uniform(0, 1),
#         random.uniform(0, 1),
#     )
#     t.pencolor(tuple_color)
#     t.forward(dash_lenght)
#     random_angle = random.uniform(0, 360)
#     t.setheading(random_angle)

#    turtle.done()

# for i in range(4):
#     if i % 2 == 0:
#         for _ in range(5):
#             t.forward(dash_lenght)
#             t.penup()
#             t.forward(dash_lenght)
#             t.pendown()
#     else:
#         t.forward(100)
#     t.right(90)


# turtle.done()


# sides = 4
# side_length = 50
# # tuple_color = t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# while sides < 10:

#     tuple_color = (
#         random.randint(1, 255) / 255.0,
#         random.randint(1, 255) / 255.0,
#         random.randint(1, 255) / 255.0,
#     )
#     t.pencolor(tuple_color)
#     for i in range(sides):

#         t.forward(side_length)
#         t.right(360 / sides)
#     sides += 1
#     side_length += 20
# turtle.done()


# https://docs.python.org/3/library/turtle.html#turtle.width

# you are going to do the pushups challenge in the 100daysofcode challenge
