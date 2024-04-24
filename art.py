import turtle
wn = turtle.Screen()
art = turtle.Turtle()
art.speed(10)
for _ in range(36):
    art.left(10)
    art.forward(15)
art.left(130)
art.forward(140)
for _ in range(12):
    art.right(150)
    art.forward(50)
art.right(150)
art.forward(170)
art.hideturtle()
