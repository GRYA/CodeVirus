import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("green")
turtle.speed(0)
a = 7
b = 7

while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b ==210:
        break
    t.hideturtle

turtle.done()