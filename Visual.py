# Visual project using turtle graphics
# By Frank Anastasia

# Import modules
import turtle

# Load the screen 
loadWindow = turtle.Screen()

boy0 = turtle.Pen()
boy0.color("red")

boy1 = turtle.Pen()
boy1.color("orange")

boy2 = turtle.Pen()
boy2.color("yellow")

boy3 = turtle.Pen()
boy3.color("green")

# Basic loop to draw a square 
for i in range (40):
	boy0.forward(100)
	boy0.left(89)
	boy1.forward(100)
	boy1.left(79)
	boy2.forward(100)
	boy2.left(69)
	boy3.forward(100)
	boy3.left(59)

# End condition 
turtle.exitonclick()
