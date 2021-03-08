import turtle

size_factor = 1  # Float to change respective size of drawing not recommended to change because it changes Proportions
y_offset = -200

turtle.penup()
turtle.goto(0, y_offset)
turtle.pendown()


def forward(length):
    turtle.forward(int(length * size_factor))


def draw_curve(angle, details=100):
    prew_angle = turtle.heading()
    angle /= details
    for i in range(details):
        turtle.seth(prew_angle + i * angle)
        turtle.forward(1)


turtle.color("#e2bf89")
turtle.begin_fill()
turtle.seth(88)
forward(10)
turtle.seth(73)
forward(20)
turtle.seth(88)
forward(150)
draw_curve(35)
forward(150)
turtle.right(90)
forward(5)
draw_curve(-90, 50)
forward(125)
turtle.left(170)
forward(50)
turtle.right(10)
forward(150)
draw_curve(-180, 60)
forward(150)
turtle.right(10)
forward(50)
turtle.left(170)
forward(75)
turtle.right(5)
forward(150)
draw_curve(-180, 60)
forward(225)
draw_curve(45, 25)
forward(5)
turtle.left(90)
forward(50)
draw_curve(-90, 25)
forward(50)
draw_curve(-45, 25)
forward(25)
draw_curve(-150, 25)
forward(35)
# draw_curve(150, 25)
draw_curve(90, 50)
draw_curve(170, 150)
draw_curve(90, 30)
# forward(15)
draw_curve(-110, 30)
# forward(15)
draw_curve(-80, 40)
forward(50)
draw_curve(-60, 10)

while turtle.ycor() > y_offset:
    forward(abs((y_offset - turtle.ycor())//2))

turtle.end_fill()

turtle.exitonclick()
