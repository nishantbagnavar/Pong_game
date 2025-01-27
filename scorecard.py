from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0  # Initialize right player's score
        self.l_score = 0  # Initialize left player's score
        self.divide = "-"  # Divider between scores
        
        self.update_score()

    def update_score(self):
        """Display the current scores on the screen."""
        self.clear()  # Clear the previous score display
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))  # Left player's score
        self.goto(0, 200)
        self.write(self.divide, align="center", font=("courier", 80, "normal"))  # Divider
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))  # Right player's score

    def count_L_score(self):
        """Increase the left player's score by 1 and update the display."""
        self.l_score += 1  # Increment left player's score
        self.update_score()  # Update the display with the new score

    def count_R_score(self):
        """Increase the right player's score by 1 and update the display."""
        self.r_score += 1  # Increment right player's score
        self.update_score()  # Update the display with the new score
