import turtle as t
import random

pytera = t.Turtle()
pyterinha = t.Turtle()
t.bgcolor('Black')
pytera.speed(0)
pytera.forward(50)
pyterinha.backward(50)
pyterinha.speed(0)
radius=45
pytera.pensize(1)
cores = ['Red','Magenta','Blue','Green']
for x in range(100):
    pytera.color(cores[3])
    pyterinha.color(cores[3])
    for petalas in range(10):
        pytera.circle(radius)
        pyterinha.circle(radius)
        pyterinha.left(45)
        pytera.right(45)
    radius = radius + 4
t.exitonclick()