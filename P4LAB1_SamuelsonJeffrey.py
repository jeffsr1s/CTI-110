#Jeffrey Samuelson
#4/26/2025
#P4LAB1
#Use turtle and loops

import turtle

#create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("turtle")

#code to draw the square
for side in range(4):
    pen.forward(100)
    pen.left(90)

#code to draw the triangle
sides = 3
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

#wait for user to close window
win.mainloop()
