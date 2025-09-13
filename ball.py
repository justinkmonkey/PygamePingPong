import turtle
class Ball(turtle.Turtle):
    def __init__(self, shape="circle"):
        super().__init__(shape)
        self.speed(0)
        self.shapesize(1, 1)
        self.color('brown')
        self.penup()
        self.goto(0, 0)
        self.dx = 5
        self.dy = 5

    def movement(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
    