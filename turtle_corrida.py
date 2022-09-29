import turtle as t 
import random as r 

#pista de corrida
pista = t.Screen()
pista.title('CORRIDA DE TARTARUGA')
pista.setup(1500,500)
pista.bgpic('pixel fundo gif.gif')

comece = False
# configurando os corredores

cores = ['red','green','blue','yellow','purple']
posição = [0,80,-80,160,-160]
participantes = []
for corredor in range(5):
    corredores = t.Turtle(shape='turtle')
    corredores.penup()
    corredores.color(cores[corredor])
    corredores.goto(x=-740,y=posição[corredor])
    participantes.append(corredores)


aposta = pista.textinput(title='*****Faça sua Aposta*****',prompt='Qual cor vencerá a corrida: ')
if aposta:
    comece = True
#programando a corrida com biblioteca random 

while comece is True: 
    for participante in participantes:
        if participante.xcor()> 730:
            print(participante.pencolor())
    for participante in participantes:
        velocidade = r.randint(0,10)
        participante.fd(velocidade)




pista.exitonclick()