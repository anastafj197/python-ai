# Basic Gui using tkinter
# First attempts at a color shifting display

import time
from tkinter import *
from itertools import cycle

root = Tk()

#theLabel = Label(root, text="Emma is a poopie brainer")
#theLabel.pack()

canvas = Canvas(root, width=200, height=150)
canvas.pack()
#                         (top x, top y, )
topRightLine = canvas.create_line(100, 10, 200, 60)
topLeftLine = canvas.create_line(100, 10, 0, 60)

bottomLeftLine = canvas.create_line(100, 110, 0, 60)
bottomRightLine = canvas.create_line(100, 110, 200, 60) #fill="red"

# first point is top left of rectangle (25 over 45 down)
# next 2 parameters are endpont of rectangle (130 over 60 down)

box = canvas.create_rectangle(50, 35, 150, 85)

# command to change box color 
canvas.itemconfig(box, fill="green")

color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
color_gen = cycle(color_list)

count = 0

#for color in color_list:
#	canvas.itemconfig(box, fill = color_list[count])
#	canvas.pack()
#	print(count)
#	count += 1
#	time.sleep(1)

	
root.mainloop()


#def box_color_shift():



#canvas.delete(redLine)
#canvas.delete(ALL)



#box_color_shift()
