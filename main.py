import time
from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")
screen.tracer(0)

snakes = []

for i in range(3):
    snakes.append(Turtle(shape="square"))
    snakes[i].penup()
    if i - 1 >= 0:
        snakes[i].goto(x=snakes[i - 1].xcor() - 20, y=0)
    snakes[i].color("white")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snake_number in range(len(snakes) - 1, 0, -1):
        new_x = snakes[snake_number - 1].xcor()
        new_y = snakes[snake_number - 1].ycor()

        snakes[snake_number].goto(new_x, new_y)

    snakes[0].forward(20)
    snakes[0].left(90)


screen.exitonclick()
