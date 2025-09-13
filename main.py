import turtle as t
from ball import Ball

# Screen setup
win = t.Screen()
win.title("Ping Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Left rod
left_rod = t.Turtle()
left_rod.shape('square')
left_rod.color('red')
left_rod.shapesize(stretch_wid=5, stretch_len=1)
left_rod.penup()
left_rod.goto(-350, 0)

# Right rod
right_rod = t.Turtle()
right_rod.shape('square')
right_rod.color('blue')
right_rod.shapesize(stretch_wid=5, stretch_len=1)
right_rod.penup()
right_rod.goto(350, 0)


# Score
score_left = 0
score_right = 0
score_display = t.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Red: {score_left}  Blue: {score_right}", align="center", font=("Courier", 28, "bold"))

# Instructions
instructions = t.Turtle()
instructions.speed(0)
instructions.color("yellow")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, 220)
instructions.write("Red: W/S | Blue: Up/Down", align="center", font=("Arial", 18, "bold"))

# Decorative border
border = t.Turtle()
border.hideturtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-390, 290)
border.pendown()
for _ in range(2):
    border.forward(780)
    border.right(90)
    border.forward(580)
    border.right(90)
border.penup()

# Rod movement functions
def left_rod_up():
    if left_rod.ycor() < 250:
        left_rod.sety(left_rod.ycor() + 20)

def left_rod_down():
    if left_rod.ycor() > -250:
        left_rod.sety(left_rod.ycor() - 20)

def right_rod_up():
    if right_rod.ycor() < 250:
        right_rod.sety(right_rod.ycor() + 20)

def right_rod_down():
    if right_rod.ycor() > -250:
        right_rod.sety(right_rod.ycor() - 20)

# Keyboard bindings
win.listen()
win.onkeypress(left_rod_up, 'w')
win.onkeypress(left_rod_down, 's')
win.onkeypress(right_rod_up, 'Up')
win.onkeypress(right_rod_down, 'Down')

# Ball
ball = Ball()

# Update score display
def update_score():
    score_display.clear()
    score_display.write(f"Red: {score_left}  Blue: {score_right}", align="center", font=("Courier", 28, "bold"))

# Main game loop
def game_loop():
    global score_left, score_right
    ball.movement()

    # Top and bottom border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.bounce_y()
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.bounce_y()

    # Left rod collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (left_rod.ycor() - 50 < ball.ycor() < left_rod.ycor() + 50):
        ball.setx(-340)
        ball.bounce_x()
        ball.color('blue')

    # Right rod collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (right_rod.ycor() - 50 < ball.ycor() < right_rod.ycor() + 50):
        ball.setx(340)
        ball.bounce_x()
        ball.color('red')

    # Left miss
    if ball.xcor() < -390:
        score_right += 1
        update_score()
        ball.reset_position()
        ball.color('brown')

    # Right miss
    if ball.xcor() > 390:
        score_left += 1
        update_score()
        ball.reset_position()
        ball.color('brown')

    win.update()
    win.ontimer(game_loop, 15)

game_loop()
win.mainloop()