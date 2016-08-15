import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape('circle')
    brad.color("yellow", "black")
    brad.speed('slowest')

    for edge in range (0, 4):
        brad.forward(100)
        brad.right(90)
    brad.right(10)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)  
    angie.speed('slowest')  

def draw_triangle():
    gerry = turtle.Turtle()
    gerry.shape("classic")
    gerry.color("#285078", "#a0c8f0")

    for edge in range (0, 3):
        gerry.forward(100)
        gerry.right(120)


window = turtle.Screen()
window.bgcolor("red")

for edge in range (0, 4):
    draw_square()

#draw_circle()
#draw_triangle()

window.exitonclick()