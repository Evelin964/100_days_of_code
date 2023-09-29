# this is the turtle Race game.
import turtle
import random

tim = turtle.Turtle()
tim.name = "Tim"
dom = turtle.Turtle()
dom.name = "Dom"
tom = turtle.Turtle()
tom.name = "Tom"
sam = turtle.Turtle()
sam.name = "Sam"
jim = turtle.Turtle()
jim.name = "Jim"

screen = turtle.Screen()
screen.setup(width=500, height=400)


tim.shape("turtle")
tim.color("red")

jim.shape("turtle")
jim.color("blue")
dom.shape("turtle")
dom.color("green")
tom.shape("turtle")
tom.color("yellow")
sam.shape("turtle")
sam.color("pink")

tim.penup()
jim.penup()
dom.penup()
tom.penup()
sam.penup()

tim.goto(x=-230, y=100)
jim.goto(x=-230, y=70)
dom.goto(x=-230, y=40)
tom.goto(x=-230, y=10)
sam.goto(x=-230, y=-20)


def at_edge(turtle):
    x, y = turtle.position()
    width = screen.window_width() / 2
    height = screen.window_height() / 2
    return not (-width < x < width and -height < y < height)


turtles = [tim, jim, dom, tom, sam]

available_turtle_names = ", ".join([turtle.name for turtle in turtles])
user_bet = screen.textinput(
    prompt=f"Who do you think will win ? Available turtles: {available_turtle_names}",
    title="Make your bet",
)


winner = None

while winner is None:
    for turtle in turtles:
        nr_of_steps = random.randint(1, 10)
        turtle.forward(nr_of_steps)
        if at_edge(turtle):
            winner = turtle
            break

print(f"{winner.name} is the winner")
# Check if the user's bet matches the winner
if user_bet is not None:
    if user_bet.strip().lower() == winner.name.lower():
        print("Congratulations! You won the bet.")
    else:
        print("Sorry, you lost the bet.")
screen.exitonclick()


######################################################################
# This is the ech a scehtch game.

# t = Turtle()
# screen = Screen()

# screen.listen()


# def move_forward():
#     t.forward(10)


# def move_backward():
#     t.backward(10)


# def go_left():
#     t.left(10)


# def go_right():
#     t.right(10)


# def clear_screen():
#     t.clear()
#     t.reset()


# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="c", fun=clear_screen)
# screen.onkey(key="a", fun=go_left)
# screen.onkey(key="d", fun=go_right)
# screen.onkey(key="s", fun=move_backward)
# screen.onkeypress(key="w", fun=move_forward)
# screen.onkeypress(key="c", fun=clear_screen)
# screen.onkeypress(key="a", fun=go_left)
# screen.onkeypress(key="d", fun=go_right)
# screen.onkeypress(key="s", fun=move_backward)

# screen.exitonclick()
