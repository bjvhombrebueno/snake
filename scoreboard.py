from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #self.high_score = 0
        with open("data.txt", mode="r") as my_file:
            self.high_score = int(my_file.read())
        self.color("White")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE = {self.score}, High Score  = {self.high_score}", move=False, align='center', font=('Arial', 30, 'normal'))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
        #self.clear()
        #self.write(f"SCORE = {self.score}, High Score  = {self.high_score}", move=False, align='center', font=('Arial', 30, 'normal'))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", move=False, align='center', font=('Arial', 30, 'normal'))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as my_file:
                my_file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
