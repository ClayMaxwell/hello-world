import turtle
def drawCircle (centerpoint, radius):
    (x,y) = centerpoint
    turtle.up()
    turtle.setpos(x,y)
    turtle.down()
    turtle.circle(radius)
    print("The radius of the circle is", radius)
    print("The circumference of the circle is", (2.0 * 3.14 * radius))
drawCircle((20,20), 20)
