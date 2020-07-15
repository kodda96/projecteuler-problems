import turtle

my_turtle=turtle.Turtle()

def squre(length,angel,color):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(angel)
        my_turtle.color(color)

squre(100,90,'red')      
squre(50,90,'yellow')    
    
