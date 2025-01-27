from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # Initialize the paddle with specified attributes
        self.speed(0)  # No animation delay
        self.color("white")  # Paddle color
        self.penup()  # No drawing when moving the paddle
        self.shape("square")  # Paddle shape
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch paddle shape to desired size
        self.goto(position)  # Position the paddle at the given coordinates

    def go_up(self):
        # Move the paddle up by 30 units
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        # Move the paddle down by 30 units
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
