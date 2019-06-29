import turtle
long = turtle.Turtle()

def equitriangle(edgeColor, fillColor):
    long.color(edgeColor, fillColor)
    long.begin_fill()
for i in range(3):
    long.forward(50)
    long.left(120)
    long.end_fill()
    
equitriangle(long, 50, 'blue', 'red')


    
    
