from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Jogo da Cobrinha")

snakes = []

for i in range(3):
    snakes.append(Turtle(shape="square"))
    snakes[i].penup()
    if i - 1 >= 0:
        snakes[i].goto(x=snakes[i - 1].xcor() - 20, y=0)
    snakes[i].color("white")

game_is_on = True
while game_is_on:
    for snake in snakes:
        snake.forward(20)


screen.exitonclick()
