import turtle

pen = turtle.Turtle()
pen.speed(0)

window = turtle.Screen()
window.bgcolor("skyblue")

rainbow = ["red", "orange", "yellow", "green", "blue", "indigo", "violet",
           "skyblue"]

size = 250
pen.penup()
pen.goto(0, -360)

for color in rainbow:
    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()
    size -= 20

turtle.done()
