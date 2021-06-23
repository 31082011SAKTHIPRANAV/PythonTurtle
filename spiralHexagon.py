import turtle
hex = turtle.Pen()
colors = ["red","blue","yellow","orange","purple","green"]
turtle.bgcolor("black")
for i in range(360):
    hex.pencolor(colors[i%6])
    hex.width(i/100+1)
    hex.forward(i)
    hex.left(59)