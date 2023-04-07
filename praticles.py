import turtle

t = turtle.Turtle()

t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)


t.penup()
t.goto(-50, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(50, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-60, -40)
t.pendown()
t.right(45)
t.circle(70, 90)
t.hideturtle()
turtle.done()
