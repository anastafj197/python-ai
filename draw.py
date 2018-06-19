from tkinter import *

root = Tk()

theLabel = Label(root, text="Poo Poo Na Na")
theLabel.pack()

canvas = Canvas(root, width=200, height=100)
canvas.pack()
#                         (top x, top y, )
blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0, 100, 200, 50, fill="red")

# first point is top left of rectangle (25 over 45 down)
# next 2 parameters are width and height of rectangle

greenBox = canvas.create_rectangle(25, 35, 130, 60, fill="purple")

#canvas.delete(redLine)

root.mainloop()
