import turtle
import math


t = turtle.Turtle()
t.speed(1)  


def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.right(angle)


def next_side_length(sides, length):
    outer_radius = (length / (2 * math.sin(math.pi / sides)))
    return 2 * outer_radius * math.sin(math.pi / (sides + 1))


length = 100
sides = 3


while sides <= 15:  
    current_length = length / (2 * math.sin(math.pi / sides))
    
    t.penup()
    t.goto(-current_length / 2, current_length / (2 * math.tan(math.pi / sides)))
    t.pendown()
    draw_polygon(t, sides, current_length)
    length = next_side_length(sides, length)
    sides += 1


t.hideturtle()
turtle.done()
