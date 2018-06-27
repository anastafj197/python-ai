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

# Basic loop to draw a square 
for i in range (100):
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

# turtle.update()

# End condition 
turtle.exitonclick()
