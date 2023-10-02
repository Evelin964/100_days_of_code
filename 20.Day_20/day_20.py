"""This is my day 19 project for 100 days of code by Dr Angela Yu.
I this file we are creating a snake game.
"""
from turtle import Turtle, Screen
import random
import time

# Food class to manage the food's appearance and position
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.speed("fastest")
        self.refresh()  # Initial placement of food

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)


# SnakeGame class
class SnakeGame:
    def __init__(self):
        # Initialize the game window and snake
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)
        self.screen.title("------My Snake Game------")

        self.left_boundary = -290
        self.right_boundary = 290
        self.top_boundary = 290
        self.bottom_boundary = -290

        self.segments = []
        self.initial_positions = [(0, 0), (-20, 0), (-40, 0)]

        # Initialize food
        self.food = Food()
        self.food_count = 0

        # Scoreboard
        self.score_turtle = Turtle()
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.color("white")
        self.score_turtle.goto(0, 260)  # Position the score display
        self.update_score()

        self.screen.listen()
        self.screen.onkeypress(self.move_up, "Up")
        self.screen.onkeypress(self.move_down, "Down")
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")

        self.game_over = False

    def update_score(self):
        self.score_turtle.clear()
        score = self.food_count * 10
        self.score_turtle.write(
            f"Score: {score}", align="center", font=("Arial", 24, "normal")
        )

    def increase_speed(self):

        if self.food_count < 7:
            new_speed = 0.1 - (self.food_count * 0.01)
        else:
            new_speed = 0.03
        time.sleep(new_speed)

    def create_snake(self):
        for position in self.initial_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def check_collision(self):
        head = self.segments[0]
        if head.distance(self.food) < 20:
            self.food.refresh()
            self.extend_snake()
            self.food_count += 1
            self.update_score()

    def extend_snake(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        last_segment = self.segments[-1]
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_segment)

    def check_wall_collision(self):
        head = self.segments[0]
        if (
            head.xcor() < self.left_boundary
            or head.xcor() > self.right_boundary
            or head.ycor() > self.top_boundary
            or head.ycor() < self.bottom_boundary
        ):
            return True
        return False

    def run_game(self):
        self.create_snake()

        while not self.game_over:
            self.screen.update()
            self.check_collision()
            for i in range(len(self.segments) - 1, 0, -1):
                x = self.segments[i - 1].xcor()
                y = self.segments[i - 1].ycor()
                self.segments[i].goto(x, y)

            self.segments[0].forward(20)
            if self.check_wall_collision():
                self.game_over = True
                print("Game over - Wall collision")
            for segment in self.segments[1:]:
                if self.segments[0].distance(segment) < 10:
                    self.game_over = True
                    print("Game over - Self collision")

            self.increase_speed()
        self.screen.bye()


# Main game loop
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
