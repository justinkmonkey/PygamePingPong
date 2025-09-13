import turtle as t
from ball import Ball


left_rod = t.Turtle()
left_rod.shape('square')
left_rod.color('red')
left_rod.shapesize(stretch_wid=5, stretch_len=1)
left_rod.penup()
left_rod.goto(-350, 0)
right_rod = t.Turtle()
right_rod.shape('square')
right_rod.color('blue')
right_rod.shapesize(stretch_wid=5, stretch_len=1)
right_rod.penup()
right_rod.goto(350, 0)

def left_rod_up():
    if left_rod.ycor() < 250:
        y = left_rod.ycor()
        y += 20
        left_rod.sety(y)



def left_rod_down():
    if left_rod.ycor() > -250:
        y = left_rod.ycor()
        y -= 20
        left_rod.sety(y)
def right_rod_up():
    if right_rod.ycor() < 250:
        y = right_rod.ycor()
        y += 20
        right_rod.sety(y)
def right_rod_down():
    if right_rod.ycor() > -250:
        y = right_rod.ycor()
        y -= 20
        right_rod.sety(y)
t.listen()
t.onkeypress(left_rod_up, 'w')
t.onkeypress(left_rod_down, 's')
t.onkeypress(right_rod_up, 'Up')
t.onkeypress(right_rod_down, 'Down')


ball = Ball()
speed = 5
spx = speed 
spy = speed

while True:
    ball.movement(spx,spy)
    
    if ball.ycor()>250:
        spy=-speed
    
    if ball.ycor()<-250:
        spy=speed
    
    if abs(ball.xcor()-left_rod.xcor())<10:
        if abs(ball.ycor()-left_rod.ycor())<50:
            spx = speed
            ball.color('blue')

    
    if abs(ball.xcor()-right_rod.xcor())<10:
        if abs(ball.ycor()-right_rod.ycor())<50:
            spx = -speed
            ball.color('red')


t.done()