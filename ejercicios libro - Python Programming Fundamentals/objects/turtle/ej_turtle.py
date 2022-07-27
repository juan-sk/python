from turtle import *

t  = Turtle()

scr = t.getscreen()

t.begin_fill()
print (scr.screensize())


def move(t):
    t.forward(100)
    
def rotar90(t):
    t.left(90)
move(t)
rotar90(t)
move(t)
rotar90(t)
move(t)
rotar90(t)
move(t)
rotar90(t)



# t.forward(25)
# t.left(90)
# t.forward(25)
# t.left(90)
# t.forward(25)
# t.left(90)
# t.forward(25)


scr.exitonclick()
