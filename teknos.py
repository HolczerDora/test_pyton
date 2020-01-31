import turtle

# ABLAK

ablak = turtle.Screen()
ablak.setup(width=800,height=600)
ablak.bgcolor("purple")
ablak.title("Pong Game")
ablak.tracer()

# Bal oldali ütő
balUto = turtle.Turtle()
balUto.speed(0)
balUto.shape("square")
balUto.shapesize(stretch_wid=5,stretch_len=1)
balUto.color("white")
balUto.penup()
balUto.goto(-350,0)

# Jobb oldali ütő
jobb = turtle.Turtle()
jobb.speed(0)
jobb.shape("square")
jobb.shapesize(stretch_wid=5,stretch_len=1)
jobb.color("white")
jobb.penup()
jobb.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
#változók
ball.valtozoX = 1
ball.valtozoY = -1
def bal_uto_up():
    y = balUto.ycor()
    y+=30 # y=y+30
    balUto.sety(y)

def bal_uto_down():
    y = balUto.ycor()
    y-=30 # y=y-30
    balUto.sety(y)    

def jobb_uto_up():
    y = jobb.ycor()
    y+=30 # y=y+30
    jobb.sety(y) 

def jobb_uto_down():
    y = jobb.ycor()
    y-=30 # y=y-30
    jobb.sety(y)       

ablak.onkey(bal_uto_up,"e")
ablak.onkey(bal_uto_down,"f")
ablak.onkey(jobb_uto_up,"p")
ablak.onkey(jobb_uto_down,"l")

# a képernyő figyelése
ablak.listen()

while True:
    # a képernyő frissítése
    ablak.update() 
    # a labdát figyeli, az aktuális pozicíójához ad hozzá vagy vesz el
    ball.setx(ball.xcor() + ball.valtozoX)
    ball.sety(ball.ycor() - ball.valtozoY)
    # a labda elegánsan pattanjon vissza az oldal tetejéről 
    if ball.ycor() > 288:
        ball.sety(288)
        ball.valtozoY *= -1
    # a labda az X oldalról az Origóra visszamegy    
    if ball.xcor() > 388:
        ball.goto(0,0)
        ball.valtozoX *= -1

    # a labda elegánsan pattanjon vissza az oldal aljáról        
    if ball.ycor() < -288:
        ball.sety(-288)
        ball.valtozoY *= -1

    # a labda az X oldalról az Origóra visszamegy      
    if ball.xcor() < -388:
        ball.goto(0,0)
        ball.valtozoX *= -1

    # visszapattan a jobb oldali ütőről
    if jobb.xcor()-20 < ball.xcor() < jobb.xcor() and jobb.ycor()-40 < ball.ycor() < jobb.ycor()+40:
        ball.setx(jobb.xcor()-20)
        ball.valtozoX *=-1
    # visszapattan a bal oldali ütőről
    if balUto.xcor()+20 > ball.xcor() > balUto.xcor() and balUto.ycor()-40 < ball.ycor() < balUto.ycor()+40:
        ball.setx(balUto.xcor()+20)
        ball.valtozoX *=-1