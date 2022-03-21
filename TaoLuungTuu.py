import turtle
tao = turtle.Pen()
tao.shape('turtle')
turtle.bgcolor('gray')

def LuungTuu(x,y):
    for i in range(1):
        tao.penup()
        tao.goto(x,y)
        tao.pendown()
        tao.begin_fill()
        tao.circle(50)
        tao.fillcolor('red')
        tao.end_fill()
        tao.penup()

def LuungPom(x,y):
    for i in range(1):
        tao.goto(x,y)
        tao.pendown()
        tao.pencolor('red')
        tao.pensize(6)
        tao.lt(45)
        tao.fd(150)
        tao.rt(90)
        tao.fd(150)

LuungTuu(100,100)
LuungTuu(-100,100)
LuungPom(-100,-100)