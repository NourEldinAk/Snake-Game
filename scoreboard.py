from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highest_score.txt") as file : 
            self.highest_score = file.read()
        self.score = 0
        self.clear()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}",align=ALIGNMENT,font=FONT)


    def increase_score(self):
        self.score = self.score + 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("highest_score.txt","w") as file:
            file.write(f"{self.highest_score}")

    # def gameOver(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write("Game Over",align="center",font=("arial",24,"normal"))
    #     self.hideturtle()