import turtle
class Ball(turtle.Turtle):
    def __init__(self, shape = "circle"):
        super().__init__(shape)
        self.speed(0)
        self.shapesize(1,1)
        self.color('brown')
        self.penup()
        self.goto(-200,100)
    def movement(self,direction_x,direction_y):
        self.goto(self.xcor()+direction_x    , self.ycor()+direction_y)
    