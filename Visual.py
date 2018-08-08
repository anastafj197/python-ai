# Visual project using turtle graphics
# By Frank Anastasia

# Import modules
import turtle

# Load the screen 
loadWindow = turtle.Screen()

# turn off draw mode
turtle.tracer(0, 0)

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

def move_all_f(distance):
	boy0.forward(distance)
	boy1.forward(distance)
	boy2.forward(distance)
	boy3.forward(distance)
	boy4.forward(distance)

def move_all_b(distance):
	boy0.backward(distance)
	boy1.backward(distance)
	boy2.backward(distance)
	boy3.backward(distance)
	boy4.backward(distance)

def move_all_r(distance):
	boy0.right(distance)
	boy1.right(distance)
	boy2.right(distance)
	boy3.right(distance)
	boy4.right(distance)

def move_all_l(distance):
	boy0.left(distance)
	boy1.left(distance)
	boy2.left(distance)
	boy3.left(distance)
	boy4.left(distance)

big()
small()

move_all_l(60)
move_all_f(200)

small()

move_all_r(100)

boy4.left(60)

boy3.forward(20)

boy2.forward(30)



move_all_f(500)
small()

def s_unit_loop(times):
	for i in range(times): 
		move_all_f(100)
		small()

s_unit_loop(25)

move_all_l(90)
boy1.left(60)
boy2.left(90)
boy2.forward(100)


# turtle.update()

# End condition 
turtle.exitonclick()
