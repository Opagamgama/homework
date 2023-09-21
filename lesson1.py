from turtle import *
 

#step 1 : draw a square 
speed(8)
width(6)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square 

#drawing a door


forward(70)
color("brown")
left(90)
forward(120)      #height of the door
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

right(150)
color("blue")
begin_fill()
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(130,130)
pendown()

right(240)
color("black")
forward(40)
left(90) 
forward(60)          #making a window
left(90)
forward(40)
left(90)
forward(60)

penup()
goto(50,130)
pendown()

right(181)
color("black")
forward(60)
left(90)
forward(40)         #second window
left(90)
forward(60)
left(90)
forward(40)


exitonclick()
