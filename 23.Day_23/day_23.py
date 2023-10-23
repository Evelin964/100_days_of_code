"""THis is my day 23 game.
From Angela Yu's 100 days of code course.
This game is a turtle crossing game.
"""

# TODO 1 create the screen - done
# TODO 2 create the player turtle - done
# TODO 3 create the car turtle
# TODO 4 create the scoreboard - done
# TODO 5 move the player turtle - done
# TODO 6 create the car manager
# TODO 7 detect collision with car
# TODO 8 detect when the player reaches the other side
# TODO 9 increase the speed of the cars
# TODO 10 create the scoreboard
# TODO 11 detect when the player loses


from turtle import Turtle, Screen, onkeypress, listen, onkeypress
import random
from time import sleep


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.colors = [
            "red",
            "green",
            "blue",
            "yellow",
            "orange",
            "purple",
            "pink",
            "black",
            "brown",
            "gray",
        ]
        self.active_cars = []
        self.car_speed = 10
        self.car_tiks = 0
        self.car_number = 0

    def car_manager(self):
        self.car_tiks += 1
        self.car_number = random.randint(3, 9)
        for _ in range(self.car_number):
            if self.car_tiks == 3:
                self.car_tiks = 0
                self.car_location()
        self.move_cars()
        self.screen.update()

    def increase_speed(self):
        if self.car_speed <= 100:
            self.car_speed += 10

    def move_cars(self):
        for car in self.active_cars:
            car.forward(self.car_speed)

        # Hide and delete the cars that are outside the visible area
        for car in self.active_cars:
            if car.xcor() < -300:
                car.hideturtle()

        # Filter out the cars that are still within the visible area
        self.active_cars = [car for car in self.active_cars if car.xcor() >= -300]

    def is_occopied(self, xcor):
        for car in self.active_cars:
            if car.xcor() == xcor:
                return True
        return False

    def car_location(self):
        car = self.create_car()
        while self.is_occopied(car.xcor()):
            car.goto(300, random.randint(-280, 280))
        self.active_cars.append(car)

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("square")
        car.color(random.choice(self.colors))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.goto(300, random.randint(-280, 280))
        self.screen.update()
        return car


class TurtleCross:
    def __init__(self) -> None:
        self.screen = Screen()
        self.setup_screen()
        self.create_player()
        self.level_nr = 0
        self.level_board()
        self.game_running = True
        self.paused = False

        self.screen.update()
        self.car_manager = CarManager()

        ############################
        self.screen.listen()
        self.screen.onkeypress(self.move_player_up, "Up")
        self.screen.onkeypress(self.move_player_down, "Down")
        self.screen.onkeypress(self.toogle_paused, "space")
        ############################

        self.run_game()

    def run_game(self):

        while self.game_running:
            self.screen.update()
            if not self.paused:
                if not self.check_collision():
                    self.car_manager.car_manager()
                    if self.player.ycor() >= 280:
                        self.level_nr += 1
                        self.level.clear()
                        self.level.write(
                            f"Level: {self.level_nr}", font=("Arial", 20, "normal")
                        )
                        self.player.penup()
                        self.player.goto(0, -280)
                        self.player.pendown()
                        self.car_manager.increase_speed()
                    sleep(0.1)
                else:
                    self.game_over()

    def toogle_paused(self):
        self.paused = not self.paused

    def game_over(self):
        self.level.goto(0, 0)
        self.level.write("Game Over", font=("Arial", 20, "normal"))
        self.game_running = False

    def check_collision(self):
        for car in self.car_manager.active_cars:
            if self.player.distance(car) < 20:
                return True
        return False

    def level_board(self):
        self.level = Turtle()
        self.level.penup()
        self.level.hideturtle()
        self.level.color("black")
        self.level.goto(-280, 260)
        self.level.write(f"Level: {self.level_nr}", font=("Arial", 20, "normal"))

    def move_player_down(self):
        if not self.game_running:
            return
        self.player.penup()
        self.player.setheading(270)
        self.player.forward(10)
        self.screen.update()
        self.player.pendown()

    def move_player_up(self):
        if not self.game_running:
            return
        self.player.penup()
        self.player.setheading(90)
        self.player.forward(10)
        self.screen.update()
        self.player.pendown()

    def create_player(self):
        self.player = Turtle()
        self.player.shape("turtle")
        self.player.color("blue")
        self.player.penup()
        self.player.setheading(90)
        self.player.goto(0, -280)
        self.player.pendown()

    def setup_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("white")
        self.screen.title("Turtle Crossing")
        self.screen.tracer(25)


if __name__ == "__main__":

    game = TurtleCross()
    game.screen.exitonclick()
