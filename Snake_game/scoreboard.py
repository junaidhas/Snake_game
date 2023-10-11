from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore_data.txt") as file:
            self.highscore=int(file.read())


        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.clear()
        self.goto(0, 270)
        self.write(arg=f" Score: {self.score} Highscore: {self.highscore}", move=True, align=ALIGNMENT, font=FONT)

    def reset_score(self):

        if self.score >self.highscore:
            self.highscore=self.score
            with open("highscore_data.txt",mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.write_score()
    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", move=True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

