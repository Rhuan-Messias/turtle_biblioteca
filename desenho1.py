import turtle as t 



#Objetos
pytera = t.Turtle()
pyterinha = t.Turtle()
pyfera = t.Turtle()
pytinho = t.Turtle()

#pytera
pytera.turtlesize(0.1)
pytera.speed(0)
pytera.pensize(3)
pytera.shape('turtle')
pytera.fillcolor('pink')
pytera.penup()
pytera.forward(200)
pytera.pendown()

#pyterinha
pyterinha.turtlesize(0.1)
pyterinha.speed(0)
pyterinha.pensize(3)
pyterinha.shape('turtle')
pyterinha.fillcolor('pink')
pyterinha.penup()
pyterinha.backward(200)
pyterinha.pendown()

#pyfera
pyfera.turtlesize(0.1)
pyfera.speed(0)
pyfera.pensize(3)
pyfera.shape('turtle')
pyfera.fillcolor('pink')
pyfera.penup()
pyfera.left(90)
pyfera.backward(200)
pyfera.pendown()

#pytinho
pytinho.turtlesize(0.1)
pytinho.speed(0)
pytinho.pensize(3)
pytinho.shape('turtle')
pytinho.fillcolor('pink')
pytinho.penup()
pytinho.right(90)
pytinho.backward(200)
pytinho.pendown()

#Tela 

tela = t.Screen()
t.bgcolor('green')


raio = 50
for aumento in range(10):
    raio += 15
    for vezes in range(12):

        pyterinha.circle(raio)
        pytera.circle(raio)
        pyfera.circle(raio)
        pytinho.circle(raio)
        
        pyterinha.right(30)
        pytera.left(30)
        pyfera.left(30)
        pytinho.left(30)



t.exitonclick()

