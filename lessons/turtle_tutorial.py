from turtle import Turtle, colormode, done

#  Mini project
bob: Turtle = Turtle()
side_length: int = 300

i: int = 0
while (i < 20):
    bob.forward(side_length)
    bob.left(122)
    side_length = side_length * 0.99
    i += 1
done()


#  Leo the Turtle Tutorial
# leo: Turtle = Turtle()

# # How to make a triangle and move it around
# leo.penup()
# leo.goto(-130, -100)
# leo.pendown()
# #  Adds the RGB mode scale
# colormode(255) 
# # leo.color(99, 204, 250)
# leo.pencolor("pink")
# leo.fillcolor(32, 67, 93)
# leo.color("green", "yellow")
# leo.begin_fill()

# leo.speed(50)
# leo.hideturtle()

# i: int = 0
# while (i < 3):
#     leo.forward(300)
#     leo.left(120)
#     i = i + 1
# leo.end_fill()

# done()

# How to make a large square (up in the right hand corner)
# i: i = 0
# while (i < 4):
#     leo.forward(300)
#     leo.left(90)
#     i = i + 1
# done()

#  How to make a small square
    # leo.forward(50)
    # leo.left(30)
    # leo.right(40)

    # leo.left(30)
    # leo.right(110)
    # leo.forward(50)

    # leo.left(110)
    # leo.right(200)
    # leo.forward(50)

    # leo.left(20)
    # leo.right(110)
    # leo.forward(50)

    # done()