from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        self.move()

    def move(self):
        """Update the ball's position based on its current movement direction."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        """Reverse the ball's vertical direction."""
        self.y_move *= -1

    def bounce_horizontal(self):
        """Reverse the ball's horizontal direction and increase its speed."""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """Reset the ball to the center and restore its initial speed."""
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_horizontal()
