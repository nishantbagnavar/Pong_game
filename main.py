from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Score
import time

# Set up the game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create paddles and ball
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

# Set up key bindings for paddle movement
screen.listen()
screen.onkey(fun=right_paddle.go_up, key="Up")
screen.onkey(fun=right_paddle.go_down, key="Down")
screen.onkey(fun=left_paddle.go_up, key="w")
screen.onkey(fun=left_paddle.go_down, key="s")

# Main game loop
is_game_on = True
while is_game_on:
    # Control the game speed and update the screen
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_horizontal()

    # Detect when the ball goes out of bounds on the right side
    if ball.xcor() > 380:
        ball.reset_position()
        score.count_L_score()  # Left paddle scores a point

    # Detect when the ball goes out of bounds on the left side
    if ball.xcor() < -380:
        ball.reset_position()
        score.count_R_score()  # Right paddle scores a point

# Close the game window when clicked
screen.exitonclick()
