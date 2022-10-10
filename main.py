import turtle
#from turtle import Turtle 


leonardo = turtle.Turtle() #leonardo é um objeto, possui atributos e métodos
leonardo.shape('turtle')
leonardo.color('red')
leonardo.forward(100)
tela = turtle.Screen()

print(tela.canvheight)

tela.exitonclick()
