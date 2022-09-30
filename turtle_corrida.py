import turtle as t 
import random as r 

#pista de corrida
pista = t.Screen()
pista.title('CORRIDA DE TARTARUGA')
pista.setup(1500,500)
pista.bgpic('pixel fundo gif.gif')

correr = False
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

quantos_players = int(pista.textinput(title='*****Quantos Jogadores*****',prompt='número de jogadores'))
apostas = []
for players in range(quantos_players):
    aposta = pista.textinput(title='****Faça sua Aposta*****',prompt='Qual cor vencerá a corrida: ')
    apostas.append(aposta)
if apostas:
    correr = True
#programando a corrida com biblioteca random 

while correr is True: 
    for participante in participantes:
        
        if participante.xcor()> 720:
            correr = False
            ganhador = participante.pencolor()
            for aposta in apostas:
                if ganhador == aposta: 
                    n = apostas.index()
                    print(f'Player {n} venceu, cor {ganhador} é o vencedor')
                else:
                    print(f'Player {n} perdeu... {ganhador} é o vencedor')
    for participante in participantes:
        velocidade = r.randint(0,10)
        participante.fd(velocidade)




pista.exitonclick()