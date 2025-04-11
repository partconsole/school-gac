# Task 1 pentagon
import turtle

pete = turtle.Turtle()
pete.speed(0)
pete.hideturtle()
pete.color("purple")

offset = 1
side_length = 10

for _ in range(100):
    pete.forward(side_length)
    pete.right(72)
    side_length = side_length + offset

turtle.exitonclick()