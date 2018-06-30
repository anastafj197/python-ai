# Visual project using turtle graphics
# By Frank Anastasia

# Import modules
import turtle

# Load the screen 
loadWindow = turtle.Screen()

# turn off draw mode
# turtle.tracer(0, 0)

boy0 = turtle.Pen()
boy0.color("red")
boy0.speed(0)

boy1 = turtle.Pen()
boy1.color("orange")
boy1.speed(0)

boy2 = turtle.Pen()
boy2.color("yellow")
boy2.speed(0)

boy3 = turtle.Pen()
boy3.color("green")
boy3.speed(0)

boy4 = turtle.Pen()
boy4.color("blue")
boy4.speed(0)

# Basic loop to draw a top mandala 
def big():
	for i in range (74):
		boy0.forward(100)
		boy0.left(99)
		boy1.forward(100)
		boy1.left(79)
		boy2.forward(100)
		boy2.left(69)
		boy3.forward(100)
		boy3.left(59)
		boy4.forward(100)
		boy4.left(49)

def small():
	for i in range (74):
		boy0.forward(50)
		boy0.right(99)
		boy1.forward(50)
		boy1.right(79)
		boy2.forward(50)
		boy2.right(69)
		boy3.forward(50)
		boy3.right(59)
		boy4.forward(50)
		boy4.right(49)

big()
small()

boy0.forward(200)
boy1.forward(200)
boy2.forward(200)
boy3.forward(200)
boy4.forward(200)

small()


# turtle.update()

# End condition 
turtle.exitonclick()
