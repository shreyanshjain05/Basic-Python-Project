from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen=Screen()


screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #detech collision with wall

    if ball.xcor() > 280 or ball.ycor() < -280:
        #ball needs to be bounced
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()




    #detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
