# TODO 1 Create the snake body
# TODO 2 Move the snake
# TODO 3 Create the snake food
# TODO 4 Detect collision with food
# TODO 5 Create a scoreboard
# TODO 6 Detect collision with wall
# TODO 7 Detect collision with tail


# TODO 1 Create the snake body

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
        self.refresh()  # Initial placement of foody

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)


# SnakeGame class
class SnakeGame:
    def __init__(self):
        # Initialize the game window and snake

        self.initialize_game()
        self.create_snake()
        self.game_engine()
        self.game_over = False
        self.paused = False
        self.should_restart = False

    def restart_game(self):
        self.game_over = False

        # Clear snake segments
        for segment in self.segments:
            segment.hideturtle()  # hide each segment
        self.segments.clear()  # clear the segments list

        # Clear the screen
        self.screen.clear()

        # Reinitialize the game
        self.initialize_game()

        # Recreate the snake
        self.create_snake()

        # Reset the food and its position
        self.food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Reset the game speed and any counters or variables if necessary
        self.move_speed = 0.1  # or whatever the initial speed is
        self.food_count = 0  # or any other counter you're using

        # Run the game engine
        self.game_engine()

    def game_engine(self):
        if not self.paused:
            self.screen.listen()
            self.screen.onkeypress(self.move_up, "Up")
            self.screen.onkeypress(self.move_down, "Down")
            self.screen.onkeypress(self.move_left, "Left")
            self.screen.onkeypress(self.move_right, "Right")
            self.screen.onkeypress(self.pause_game, "space")
        else:
            self.screen.onkeypress(None, "Up")
            self.screen.onkeypress(None, "Down")
            self.screen.onkeypress(None, "Left")
            self.screen.onkeypress(None, "Right")
            self.screen.onkeypress(self.pause_game, "space")

    def initialize_game(self):
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

        self.score_turtle = Turtle()
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.color("white")
        self.score_turtle.goto(-200, 260)
        # Initialize food
        self.food = Food()
        self.food_count = 0

        self.highest_score_turtle = Turtle()
        self.highest_score_turtle.clear()
        self.highest_score_turtle.penup()
        self.highest_score_turtle.hideturtle()
        self.highest_score_turtle.color("white")
        self.highest_score_turtle.goto(160, 260)

        self.paused = False

        self.highest_score()

        self.play_again_turtle = Turtle()
        self.play_again_turtle.penup()
        self.play_again_turtle.hideturtle()
        self.play_again_turtle.color("white")
        self.play_again_turtle.goto(0, 0)

    def end_game(self):
        self.game_over = True
        self.screen.bye()

    def play_again(self):
        self.play_again_turtle.clear()
        # Display initial game-over message
        self.play_again_turtle.write(
            "Do you want to play again? (y/n)",
            align="center",
            font=("Arial", 24, "normal"),
        )

        # Turtle for countdown display
        countdown_turtle = Turtle()
        countdown_turtle.penup()
        countdown_turtle.hideturtle()
        countdown_turtle.color("white")
        countdown_turtle.goto(0, -50)

        # Modified restart_game method to set the flag
        def restart_and_set_flag():
            self.restart_game()
            self.should_restart = True

        # Countdown loop
        for i in range(10, 0, -1):
            # Listen for 'y' or 'n' keypresses
            self.screen.listen()
            self.screen.onkeypress(restart_and_set_flag, "y")
            self.screen.onkeypress(self.end_game, "n")

            # Display current countdown value
            countdown_turtle.clear()
            countdown_turtle.write(
                f"Game closes in: {i}", align="center", font=("Arial", 24, "normal")
            )

            # Check if game should be restarted
            if self.should_restart:
                break

            # Wait for a second
            time.sleep(1)

            # End game if countdown finishes
            if i == 1:
                self.end_game()

    def pause_game(self):
        if not self.game_over:
            self.paused = not self.paused
            self.game_engine()

    def update_high_score_file(self, new_high_score):
        file_path = r"C:\Users\ediacon\OneDrive - MORNINGSTAR INC\Documents\Python Scripts\02.100 Days of Python\20.Day_20\data.txt"

        with open(file_path, encoding="utf-8", mode="w") as file:
            file.write(str(new_high_score))

    def highest_score(self):
        current_score = self.food_count * 10
        high_score = self.get_high_score_from_file()
        new_high_score = max(current_score, high_score)

        if current_score > high_score:
            self.update_high_score_file(new_high_score)

        self.highest_score_turtle.write(
            f"High Score: {new_high_score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def get_high_score_from_file(self):
        file_path = r"C:\Users\ediacon\OneDrive - MORNINGSTAR INC\Documents\Python Scripts\02.100 Days of Python\20.Day_20\data.txt"

        try:
            with open(file_path, encoding="utf-8", mode="r") as file:
                high_score = int(file.read())
                return high_score
        except (FileNotFoundError, ValueError):
            return 0

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

    def collision_with_food(self):
        head = self.segments[0]
        if head.distance(self.food) < 20:
            self.food.refresh()
            self.extend_snake()
            self.food_count += 1
            self.update_score()

    def collision_with_tail(self):
        head = self.segments[0]
        for segment in self.segments[1:]:
            if head.distance(segment) < 10:
                return True
        return False

    def extend_snake(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        last_segment = self.segments[-1]
        new_segment.goto(last_segment.xcor(), last_segment.ycor())
        self.segments.append(new_segment)

    def collision_with_wall(self):
        head = self.segments[0]
        return (
            head.xcor() < self.left_boundary
            or head.xcor() > self.right_boundary
            or head.ycor() > self.top_boundary
            or head.ycor() < self.bottom_boundary
        )

    def handle_game_over(self):
        self.game_over = True
        self.play_again()
        current_score = self.food_count * 10
        high_score = self.get_high_score_from_file()

        if current_score > high_score:
            self.update_high_score_file(current_score)

    def run_game(self):

        while not self.game_over:

            self.screen.update()
            if not self.game_over:
                self.game_engine()

            if not self.paused:

                self.collision_with_food()
                for i in range(len(self.segments) - 1, 0, -1):
                    x = self.segments[i - 1].xcor()
                    y = self.segments[i - 1].ycor()
                    self.segments[i].goto(x, y)

                self.segments[0].forward(20)

                if self.collision_with_wall() or self.collision_with_tail():
                    self.handle_game_over()
                self.increase_speed()


# Main game loop
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
