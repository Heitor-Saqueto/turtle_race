import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
##########################################
screen.setup(width=500, height=400)
# (here is the width ,  height)
##########################################
is_race_on = False
all_turtle = []
#############################################
colors = ["red", "orange", "yellow", "green", "blue",  "pink", "black", "gray"]
#############################################
y_position = -100
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? choose a color: ")
#################################################
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-240, y=y_position)
    y_position += 40
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've win the turtle color {winning_color} crossed the line first")
            else:
                print(f"You've Lost the turtle color {winning_color} crossed the line first")


screen.exitonclick()

