import turtle


def draw_colored_circles():
    screen = turtle.Screen()
    screen.setup(width=600, height=800)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(2)

    colors = ["purple", "black", "blue", "purple", "black", "blue", "purple","purple", "black", "blue", "purple", "black", "blue", "purple","purple", "black", "blue", "purple", "black", "blue", "purple""purple", "black", "blue", "purple", "black", "blue", "purple" ]
    radius = 80
    angle = 360 / len(colors)

    for turtle_color in colors:
        t.color(turtle_color)
        t.circle(radius)
        t.right(angle)

    turtle.done() 


draw_colored_circles()