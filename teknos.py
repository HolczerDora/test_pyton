import turtle

# ABLAK

ablak = turtle.Screen()
ablak.setup(width=800,height=600)
ablak.bgcolor("purple")
ablak.title("Pingi-Pongi")
ablak.tracer()

# Bal oldali ütő
balUto = turtle.Turtle()
balUto.speed(0)
balUto.shape("square")
balUto.shapesize(stretch_wid=5,stretch_len=1)
balUto.color("white")
balUto.penup()
balUto.goto(-350,0)

while True:
    ablak.update()

