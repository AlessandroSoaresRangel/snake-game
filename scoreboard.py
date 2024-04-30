from turtle import Turtle

FONT = ("Arial", 15, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.pencolor("white")
        self.teleport(x=0, y=270)
        self.hideturtle()

        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.refresh_score()


    def game_over(self):
        self.teleport(x=0, y=0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_score()