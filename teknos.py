import turtle

# ABLAK

window = turtle.Screen()
window.setup(width=800,height=600)
window.bgcolor("purple")
window.title("Pong Game")
window.tracer()

# Bal oldali ütő

rightSite = turtle.Turtle()
rightSite.speed(0)
rightSite.shape("square")
rightSite.shapesize(stretch_wid=5,stretch_len=1)
rightSite.color("blue")
rightSite.penup()
rightSite.goto(-350,0)

# Jobb oldali ütő

leftSite = turtle.Turtle()
leftSite.speed(0)
leftSite.shape("square")
leftSite.shapesize(stretch_wid=5,stretch_len=1)
leftSite.color("orange")
leftSite.penup()
leftSite.goto(350,0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)

# Pontszámok

right_score = 0
left_score = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(f"Player_Right:{right_score} Player_Left:{left_score}", align="center", font=("arial", 18, "normal"))

# Változók

ball.varX = 2
ball.varY = -2

def bal_uto_up():
    y = rightSite.ycor()
    y+=30 # y=y+30
    rightSite.sety(y)

def bal_uto_down():
    y = rightSite.ycor()
    y-=30 # y=y-30
    rightSite.sety(y)    

def jobb_uto_up():
    y = leftSite.ycor()
    y+=30 # y=y+30
    leftSite.sety(y) 

def jobb_uto_down():
    y = leftSite.ycor()
    y-=30 # y=y-30
    leftSite.sety(y)       

window.onkey(bal_uto_up,"d")
window.onkey(bal_uto_down,"c")
window.onkey(jobb_uto_up,"k")
window.onkey(jobb_uto_down,"m")

# a képernyő figyelése
window.listen()

while True:
    # a képernyő frissítése

    window.update() 

    # a labdát figyeli, az aktuális pozicíójához ad hozzá vagy vesz el
    ball.setx(ball.xcor() + ball.varX)
    ball.sety(ball.ycor() - ball.varY) # a labda elegánsan pattanjon vissza az oldal tetejéről 
    if ball.ycor() > 285:
        ball.sety(285)
        ball.varY *= -1

    # a labda az jobb oldalról az Origóra visszamegy    
    if ball.xcor() > 388:
        ball.goto(0,0)
        ball.varX *= -1
        right_score +=1
        score.clear()
        score.write(f"Player_Right:{right_score} Player_Left:{left_score}",
         align="center", font=("arial", 18, "normal"))


    # a labda elegánsan pattanjon vissza az oldal aljáról        
    if ball.ycor() < -285:
        ball.sety(-285)
        ball.varY *= -1

    # a labda az X oldalról az Origóra visszamegy      
    if ball.xcor() < -388:
        ball.goto(0,0)
        ball.varX *= -1
        left_score +=1
        score.clear()
        score.write(f"Player_Right:{right_score} Player_Left:{left_score}",
         align="center", font=("arial", 18, "normal"))

    # visszapattan a jobb oldali ütőről
    if leftSite.xcor()-20 < ball.xcor() < leftSite.xcor() and leftSite.ycor()-40 < ball.ycor() < leftSite.ycor()+40:
        ball.setx(leftSite.xcor()-20)
        ball.varX *=-1

    # visszapattan a bal oldali ütőről
    if rightSite.xcor()+20 > ball.xcor() > rightSite.xcor() and rightSite.ycor()-40 < ball.ycor() < rightSite.ycor()+40:
        ball.setx(rightSite.xcor()+20)
        ball.varX *=-1