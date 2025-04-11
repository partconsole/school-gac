# Task 2
import turtle


# Set up turtle
wn = turtle.Screen()
pete = turtle.Turtle()
pete.speed(0)
pete.pensize(10)
pete.hideturtle()
pete.color("purple")



# Move to the left
pete.penup()
pete.goto(-100,0)
pete.pendown()

# Draw M
pete.left(90)
pete.forward(100)
pete.right(135)
pete.forward(70)
pete.left(90)
pete.forward(70)
pete.right(135)
pete.forward(100)



# Move to the right, change color
pete.penup()
pete.goto(100,0)
pete.pendown()
pete.pencolor("green")

# Draw T

pete.backward(100)
pete.left(90)
pete.forward(50)
pete.backward(100)

turtle.exitonclick()