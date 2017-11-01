from turtle import *

justin = Turtle()
myles = Turtle()
gang = Turtle()

justin.shape("turtle")
justin.color("purple")

gang.shape("turtle")
gang.color("red")

myles.shape("turtle")
myles.color("green")

colormode(255)
bgcolor(255, 102,  178)

def draw_star(x, y, points, line, fill):
     penup()
     goto(x,y)
     pendown()

     turn= 180 - (360 / points)

     color(line, fill)

     begin_fill()
     for i in range(points):
         forward(125)
         left(turn)
     end_fill()

def draw_box(x, y, points, line):
     setheading(0)
     penup()
     goto(x,y)
     pendown()
     width(10)
     color(line)   

     for i in range(8):
         forward(100)
         left(45)

def draw_spiral(x, y, radius, line):
    color(line)
    penup()
    goto(x, y)
    pendown()
    
    original_xcor = xcor()
    original_ycor = ycor()
    
    speed = 1
    while True:
        forward(speed)
        left(10)
        speed += 0.1
        if distance(original_xcor, original_ycor) > radius:
           break 

speed(10)
draw_star(0, 0, 100, "red", "purple")
draw_star(50, 0, 100, 'red', 'purple')
draw_star(0, -50, 100, 'red', 'purple')
draw_star(-50, 0, 100, 'red', 'purple')
draw_star(0, 50, 100, 'red', 'purple')
draw_spiral(0, 0, 50, "white")
draw_spiral(55, -48, 50, "white")
draw_spiral(100, 0, 50, "white")
draw_spiral(50, 50, 50, "white")
draw_box(10, -118, 4, 'white')
for i in range(12):
    justin.left(60)
    myles.left(50)
    gang.left(40)
    myles.forward(100)
    gang.forward(100)
    justin.forward(100)
done()     

