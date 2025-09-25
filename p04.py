'''def negyszog(a, b):
    ker = 2 * a + 2 * b
    ter = a * b
    alakzat = "téglalap"
    if a == b:
        alakzat = "négyzet"

    return ker, ter, alakzat

def szamolas(*args):
    osszeg = sum(args)
    legnagyobb = max(args)
    return osszeg, legnagyobb


sorozat = (1,2,"három",4,5)
for elem in sorozat:
    print(elem)

for i in range(10):
    print(i)

for _ in range(10):
    print("Nem leszek rossz!")


print("Összegzés:",szamolas(1, 2, 3))
print("Összegzés:",szamolas(1, 2, 3, 4))
# a = 2
# b = 4
print("Kerület:", negyszog(4, 4)[0])
print("Terület:", negyszog(4, 4)[1])
print("Alakzat:", negyszog(4, 4)[2])
'''


import turtle
import random

def negyzet():
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.pensize(5)

    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def pont(x, y):
    turtle.goto(x, y)
    turtle.dot(10,"black")

def dobas():
    turtle.hideturtle()
    negyzet()
    szam = random.randint(6,6)
    turtle.penup()

    if szam == 1:
        pont(0,0)
    elif szam == 2:
        pont(-30, 30)
        pont(30,-30)
    elif szam == 3:
        pont(-30, 30)
        pont(30,-30)
        pont(0, 0)
    elif szam == 4:
        pont(-30, 30)
        pont(30,30)
        pont(-30, -30 )
        pont(-30, 30)
    elif szam == 5:
        pont(-30, 30)
        pont(30, -30)
        pont(0,0)
        pont(-30, -30)
        pont(30, -30)
    elif szam == 6:
        pont(-30, 30)
        pont(30, -30)
        pont(-30, -30)
        pont(30, 0)
        pont(-30, -30)
        pont(0, -30)
        turtle.hideturtle()


ablakl = turtle.Screen()

turtle.onkey(dobas, "n")
turtle.onkey(turtle.bye, "Escape")

turtle.listen()
turtle.mainloop()
