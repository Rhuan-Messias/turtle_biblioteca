import turtle as t 
import random as r 

#corredores
vermelho = t.Turtle()
verde = t.Turtle()
azul = t.Turtle()
amarelo = t.Turtle()
roxo = t.Turtle()

# configurando os corredores
vermelho.penup()
vermelho.shape('turtle')
vermelho.shapesize(2)
verde.penup()
verde.shape('turtle')
verde.shapesize(2)
azul.penup()
azul.shape('turtle')
azul.shapesize(2)
amarelo.penup()
amarelo.shape('turtle')
amarelo.shapesize(2)
roxo.penup()
roxo.shape('turtle')
roxo.shapesize(2)

#pista de corrida
pista = t.Screen()
pista.title('CORRIDA DE TARTARUGA')
pista.setup(1500,500)
pista.bgpic('pixel fundo gif.gif')

#posicionar os corredores e dar o shape para eles
corredores = [vermelho,verde,azul,amarelo,roxo]
cores = ['red','green','blue','yellow','purple']
posição = [0,80,-80,160,-160,320]
item = -1 
for corredor in corredores:
    item +=1
    corredor.color(cores[item])
    corredor.setposition(-700,posição[item])

#programando a corrida com biblioteca random 



pista.exitonclick()