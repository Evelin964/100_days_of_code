import turtle

# trb sa mai curat eranul cand nu nimereste - done
# trb sa mai umblu la functia de reset game - sa reseteze ecranul si sa nu mai apara statele deja gasite - done
# sa pun un punctaj done
# sa pun un timer 


class State:
    def __init__(self):
        self.game_on = True
        self.reset_game = False
        self.current_score = 0
        self.get_data_from_csv()
        self.guessed_states = []
        self.score_board()
        self.screen_setup()
        self.run_game()

    def wrong_state(self):
        self.wrong_state_turtle = turtle.Turtle()
        self.wrong_state_turtle.penup()
        self.wrong_state_turtle.hideturtle()
        self.wrong_state_turtle.goto(0, 0)
        self.wrong_state_turtle.write(
            "Wrong state! Try again!",
            align="center",
            font=("Arial", 24, "normal"),
        )
        turtle.ontimer(self.wrong_state_turtle.clear, t=250)

    def score_board(self):
        self.score_turtle = turtle.Turtle()
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.goto(0, 250)

    def correct_answer(self):
        if self.game_on is True:
            self.score_turtle.clear()
            self.score_turtle.write(
            f"Score:{self.current_score} / {self.total_questions}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def restart_game(self):
        self.screen_setup()
        self.game_on = True
        self.guessed_states.clear()
        self.current_score = 0
        self.run_game()

    def run_game(self):
        while self.game_on:
            self.get_input()
            self.check_input()
            self.correct_answer()

    def handle_special_event(self, event):
        if event == "Exit":
            self.game_on = False
            self.exit_game()
        elif event == "Reset":
            self.game_on = False
            self.restart_game()

    def check_input(self):
        state_name = self.user_input.title()

        state_data = [state for state in self.data if state["state"] == state_name]
        if state_name in ["Exit", "Reset"]:
            self.handle_special_event(state_name)
            return

        if state_data and state_name not in self.guessed_states:
            state_x = int(state_data[0]["x"])
            state_y = int(state_data[0]["y"])
            self.write_state_name(state_name, state_x, state_y)
            self.guessed_states.append(state_name)
            self.current_score += 1

        else:
            self.wrong_state()

    def exit_game(self):
        self.game_on = False
        turtle.bye()

    def write_state_name(self, state_name, state_x, state_y):
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(state_x, state_y)
        state_turtle.write(state_name, align="center", font=("Arial", 8, "bold"))

    def get_input(self):

        screen = turtle.Screen()

        self.user_input = screen.textinput(
            title="Guess the State", prompt="What's another state's name?"
        )

    def get_data_from_csv(self):
        self.data = []  # Create an empty list to store state data
        with open(
            r"C:\Users\ediacon\OneDrive - MORNINGSTAR INC\Documents\Python Scripts\02.100 Days of Python\25.Day_25\50_states.csv",
            encoding="utf-8",
        ) as file:
            for line in file.readlines():
                state_info = line.strip().split(",")
                state = {"state": state_info[0], "x": state_info[1], "y": state_info[2]}
                self.data.append(state)
        self.total_questions = len(self.data) - 1

    def screen_setup(self):
        if self.game_on:
            screen = turtle.Screen()
            screen.title("U.S. States Game")
            screen.setup(width=800, height=600)
            background_image = r"C:\Users\ediacon\OneDrive - MORNINGSTAR INC\Documents\Python Scripts\02.100 Days of Python\25.Day_25\blank_states_img.gif"
            screen.bgpic(background_image)

            screen.tracer(0)

        elif self.game_on is False:
            screen = turtle.Screen()
            screen.clear()
            screen.title("U.S. States Game")
            screen.setup(width=800, height=600)
            background_image = r"C:\Users\ediacon\OneDrive - MORNINGSTAR INC\Documents\Python Scripts\02.100 Days of Python\25.Day_25\blank_states_img.gif"
            screen.bgpic(background_image)
            screen.tracer(0)
            self.reset_game = True


if __name__ == "__main__":
    state = State()
    if state.game_on is True:
        turtle.mainloop()
