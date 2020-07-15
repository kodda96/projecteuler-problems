import turtle

my_turtle=turtle.Turtle()

def squre(length,angel):
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(angel)

squre(100,90)      
squre(500,45)    
    
