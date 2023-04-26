from turtle import Turtle, Screen

with open("../../PYTHON/high_score.txt" ) as f:
    s = int(f.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 260)
        self.score = 0
        self.high_score = s
        self.write(f"Score:{self.score}  High Score:{self.high_score} ", align="center", font=("Courier", 24))





    def update_scoreboard(self):
        score = self.score
        self.clear()
        self.write(f"Score:{self.score}  High Score:{self.high_score} ", align="center", font=("Courier", 24))

    def update_high_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score
            self.update_scoreboard()
            with open("high_score.txt", "w") as f:
                f.write(str(self.high_score))

    def game_over(self):
        self.setposition(0,0)
        self.write(f"Game Over", align="center", font=("Courier", 30))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        self.update_high_score()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()
        self.update_high_score()


