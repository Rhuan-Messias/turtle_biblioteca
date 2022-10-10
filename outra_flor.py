import turtle 

tartarugas = []
for i in range(4):
    tartaruga = turtle.Turtle()
    tartaruga.penup()
    tartarugas.append(tartaruga)

tela = turtle.Screen()
tela.setup(750,750)
tela.bgcolor('black')




tartarugas[0].goto(0,240)
tartarugas[1].goto(0,-240)
tartarugas[2].goto(240,0)
tartarugas[3].goto(-240,0)

for tartaruga in tartarugas:
    tartaruga.pendown()
    tartaruga.speed(0)
    tartaruga.color('green')
    tartaruga.pensize(1)
for vezes in range(190):
    tartarugas[0].circle(190-vezes,90)
    tartarugas[0].left(90)
    tartarugas[0].circle(190-vezes,90)
    tartarugas[0].left(18)
    tartarugas[1].circle(190-vezes,90)
    tartarugas[1].left(90)
    tartarugas[1].circle(190-vezes,90)
    tartarugas[1].left(18)
    tartarugas[2].circle(190-vezes,90)
    tartarugas[2].left(90)
    tartarugas[2].circle(190-vezes,90)
    tartarugas[2].left(18)
    tartarugas[3].circle(190-vezes,90)
    tartarugas[3].left(90)
    tartarugas[3].circle(190-vezes,90)
    tartarugas[3].left(18)

for tartaruga in tartarugas:
    tartaruga.color('red')
    tartaruga.pensize(5)
    
for vezes in range(50):
    tartarugas[0].circle(0-vezes,90)
    tartarugas[0].left(90)
    tartarugas[0].circle(0-vezes,90)
    tartarugas[0].left(18)
    tartarugas[1].circle(0-vezes,90)
    tartarugas[1].left(90)
    tartarugas[1].circle(0-vezes,90)
    tartarugas[1].left(18)
    tartarugas[2].circle(0-vezes,90)
    tartarugas[2].left(90)
    tartarugas[2].circle(0-vezes,90)
    tartarugas[2].left(18)
    tartarugas[3].circle(0-vezes,90)
    tartarugas[3].left(90)
    tartarugas[3].circle(0-vezes,90)
    tartarugas[3].left(18)


tela.mainloop()
