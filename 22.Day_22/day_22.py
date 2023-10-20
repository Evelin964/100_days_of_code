"""THis is my day 22 challenge. 
THe day 21 game is inside the day 20 folder.
This is a simple pong game.
"""
from turtle import Turtle, Screen, onkeypress, listen, onkey
import random
import time


# TODO 1: Create the screen - done
# TODO 2: Create and move a paddle -
# TODO 3: Create another paddle
# TODO 4: Create the ball and make it move
# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect collision with paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep score


class PongGame:
    def __init__(self) -> None:
        self.screen = Screen()
        self.setup_screen()
        self.computer_score = 0
        self.player_score = 0
        self.score_board()
        self.create_computer_paddle()
        self.create_player_paddle()
        self.create_ball()
        self.is_paused = False

        # unique variables
        self.ball_direction_x = 1
        self.ball_direction_y = 1
        self.ball_cor_y_reset = 0

        self.ball_pause_counter = 0

        self.computer_paddle_direction = 1
        # Listen for keypresses
        listen()
        onkeypress(self.player_paddle_up, "Up")
        onkeypress(self.player_paddle_down, "Down")
        onkey(self.toogle_pause, "space")

        # Set up the game loop

        self.screen.update()
        self.update_game()
        self.update_screen()

    def update_game(self):
        if not self.is_paused:
            self.move_ball()
            self.check_wall_colision()

            if self.ball_pause_counter == 0:
                self.check_paddle_collision()
            self.move_computer_paddle()
            self.screen.update()
            if self.ball_pause_counter > 0:
                self.ball_pause_counter -= 1
            self.screen.ontimer(self.update_game, 70)

    def toogle_pause(self):
        self.is_paused = not self.is_paused
        if not self.is_paused:
            self.update_game()

    def score_update(self):
        # Refresh computer's score
        self.computer_score_turtle.clear()
        self.computer_score_turtle.write(
            f"Computer: {self.computer_score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

        # Refresh player's score
        self.player_score_turtle.clear()
        self.player_score_turtle.write(
            f"Player: {self.player_score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def check_paddle_collision(self):
        ball_x = self.ball.xcor()
        ball_y = self.ball.ycor()
        player_paddle_x = self.player_paddle.xcor()
        player_paddle_y = self.player_paddle.ycor()
        computer_paddle_x = self.computer_paddle.xcor()
        computer_paddle_y = self.computer_paddle.ycor()

        paddle_width = 10
        paddle_height = 50

        if (
            ball_x - paddle_width / 2 <= player_paddle_x + paddle_width / 2
            and ball_x + paddle_width / 2 >= player_paddle_x - paddle_width / 2
            and ball_y - paddle_height / 2 <= player_paddle_y + paddle_height / 2
            and ball_y + paddle_height / 2 >= player_paddle_y - paddle_height / 2
        ):
            self.ball_direction_x *= -1
        if (
            ball_x - paddle_width / 2 <= computer_paddle_x + paddle_width / 2
            and ball_x + paddle_width / 2 >= computer_paddle_x - paddle_width / 2
            and ball_y - paddle_height / 2 <= computer_paddle_y + paddle_height / 2
            and ball_y + paddle_height / 2 >= computer_paddle_y - paddle_height / 2
        ):
            self.ball_direction_x *= -1

    def check_wall_colision(self):
        if self.ball.ycor() > 290 or self.ball.ycor() < -290:
            self.ball_direction_y *= -1
        # Check for miss (ball goes over the border)
        if self.ball.xcor() > 390:
            self.ball_cor_y_reset = random.randint(-100, 100)

            self.player_score += 1
            self.score_update()
            self.ball_direction_x *= -1
            self.ball.goto(0, self.ball_cor_y_reset)
            self.ball_pause_counter = 10
        elif self.ball.xcor() < -390:
            self.ball_cor_y_reset = random.randint(-250, 250)
            self.computer_score += 1
            self.score_update()
            self.ball_direction_x *= -1  # Reverse the direction
            self.ball.goto(0, self.ball_cor_y_reset)  # Reset the ball to the center
            self.ball_pause_counter = 10  # Pause the ball for 10 ticks

    def move_ball(self):
        if self.ball_pause_counter == 0:
            current_x = self.ball.xcor()
            current_y = self.ball.ycor()
            new_x = current_x + self.ball_direction_x * self.ball_speed
            new_y = current_y + self.ball_direction_y * self.ball_speed
            self.ball.goto(new_x, new_y)

    def update_screen(self):
        self.screen.update()
        self.screen.ontimer(self.update_screen, 1)

    def player_paddle_down(self):
        y = self.player_paddle.ycor()
        if y > -250:
            y -= 20
            self.player_paddle.sety(y)

    def player_paddle_up(self):
        y = self.player_paddle.ycor()
        if y < 250:
            y += 20
            self.player_paddle.sety(y)

    def move_computer_paddle(self):
        # Get the current y-coordinate of the computer paddle
        current_y = self.computer_paddle.ycor()

        # Calculate the new y-coordinate based on the current direction
        new_y = current_y + (
            self.computer_paddle_direction * 20
        )  # Adjust the step size as needed

        # Check if the new y-coordinate is within the screen boundaries
        if -250 < new_y < 250:
            self.computer_paddle.sety(new_y)
        else:
            # If the new y-coordinate would go out of bounds, reverse the direction
            self.computer_paddle_direction *= -1

    def create_player_paddle(self):
        self.player_paddle = Turtle()
        self.player_paddle.shape("square")
        self.player_paddle.color("white")
        self.player_paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.player_paddle.penup()
        self.player_paddle.goto(-360, 0)

    def create_computer_paddle(self):
        self.computer_paddle = Turtle()
        self.computer_paddle.shape("square")
        self.computer_paddle.color("white")
        self.computer_paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.computer_paddle.penup()
        self.computer_paddle.goto(360, 0)

    def setup_screen(self):
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("------------------------Pong-Game--------------------")
        Screen().tracer(0)
        self.dashed_line = Turtle()
        self.dashed_line.penup()
        self.dashed_line.color("white")
        self.dashed_line.pensize(2)
        self.dashed_line.speed("fastest")
        self.dashed_line.goto(0, 300)
        self.dashed_line.setheading(270)
        for _ in range(30):
            self.dashed_line.pendown()
            self.dashed_line.forward(10)
            self.dashed_line.penup()
            self.dashed_line.forward(10)

    def score_board(self):
        # Score display for the computer
        self.computer_score_turtle = Turtle()
        self.computer_score_turtle.penup()
        self.computer_score_turtle.hideturtle()
        self.computer_score_turtle.color("white")
        self.computer_score_turtle.goto(260, 260)  # Position the computer score display
        self.computer_score_turtle.write(
            f"Computer: {self.computer_score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

        # Score display for the player
        self.player_score_turtle = Turtle()
        self.player_score_turtle.penup()
        self.player_score_turtle.hideturtle()
        self.player_score_turtle.color("white")
        self.player_score_turtle.goto(-260, 260)  # Position the player score display
        self.player_score_turtle.write(
            f"Player: {self.player_score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def create_ball(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("blue")
        self.ball.shapesize(stretch_wid=1, stretch_len=1)
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball_speed = 20


if __name__ == "__main__":
    game = PongGame()
    game.screen.exitonclick()
