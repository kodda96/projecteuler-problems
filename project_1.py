import turtle

my_turtle=turtle.Turtle()
my_turtle.speed(0)

def squre(length,angel):
    for i in range(4):
       my_turtle.forward(length)
       my_turtle.left(angel)

for m in range(1000):
   if m%2 == 0:
       squre(50,90)
   else:
       my_turtle.left(11)
       
