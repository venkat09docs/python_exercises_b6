from turtle import Turtle, Screen

donatello = Turtle()
my_screen = Screen()

print(my_screen.canvwidth)
print(my_screen.canvheight)

donatello.shape("turtle")
donatello.color("purple")

donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)

donatello.home()

raphel = Turtle()
raphel.shape("turtle")
raphel.color("red")

# Move raphael to a new position without drawing
raphel.penup()
raphel.goto(-150, 200)
raphel.pendown()

x = 10
while True:
    raphel.circle(x)
    donatello.circle(x + 5)
    x += 10



my_screen.exitonclick()






