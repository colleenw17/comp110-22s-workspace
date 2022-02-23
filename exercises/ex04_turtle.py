"""At the beach and in the water -- Using Turtle to Draw a Scene."""

__author__ = "730319000"

from turtle import Turtle, colormode, done

import turtle as t
t.Screen().bgcolor("lightblue")


def main() -> None:
    """The entrypoint of my scene."""
    bob: Turtle = Turtle()
    sun(bob, -300, 150) 
    sand(bob, -400, -500)
    ocean(bob, 10, -500)
    fish(bob)
    lounge_chair(bob, -220, -94)
    clouds(bob, -100, 100)
    clouds(bob, 100, 55)
    done()


def sun(bob: Turtle, x: float, y: float) -> None:
    """Drawing repeating triangle to represent the sun using a repeating function."""
    bob.speed(200)
    bob.penup()
    bob.goto(-300, 150)
    bob.pendown()
    colormode(255) 
    bob.color(252, 230, 14)
    bob.begin_fill()
    i: int = 0
    while True and (i < 21):
        bob.forward(200)
        bob.left(170)
        i += 1
    bob.end_fill()
    

def sand(bob: Turtle, x: float, y: float) -> None:
    """Drawing a rectangle to represent the sand."""
    bob.speed(10)
    bob.penup()
    bob.goto(-400, -500)
    bob.pendown()
    colormode(255)
    bob.color(175, 170, 119)
    bob.begin_fill()
    bob.left(30)
    i: int = 0
    while (i < 4):
        bob.forward(410)
        bob.left(90)
        i += 1
    bob.end_fill() 


def ocean(bob: Turtle, x: float, y: float) -> None:
    """Drawing a rectangle to represent the ocean."""
    bob.speed(10)
    bob.penup()
    bob.goto(10, -500)
    bob.pendown()
    colormode(255) 
    bob.color(34, 225, 210)
    bob.begin_fill()
    i: int = 0
    while (i < 4):
        bob.forward(410)
        bob.left(90)
        i += 1
    bob.end_fill() 


def fish(bob: Turtle) -> None:
    """Breaking up a complex function by calling other functions to create one object."""
    fish_body(bob, 220, -260)
    fish_tail(bob, 243, -266)


def fish_body(bob: Turtle, x: float, y: float) -> None:
    """Drawing a fish body using a circle."""
    bob.speed(200)
    bob.penup()
    bob.goto(220, -260)
    bob.pendown()
    bob.pencolor(255, 255, 255)
    bob.fillcolor(0, 0, 0)
    bob.begin_fill()
    bob.circle(15)
    bob.end_fill()


def fish_tail(bob: Turtle, x: float, y: float) -> None:
    """Drawing a fish tail using a triangle."""
    bob.speed(200)
    bob.penup()
    bob.goto(243, -266)
    bob.pendown()
    bob.pencolor(255, 255, 255)
    bob.fillcolor(0, 0, 0)
    bob.begin_fill()
    bob.left(60)
    i: int = 0
    while (i < 3):
        bob.forward(20)
        bob.left(120)
        i = i + 1    
    bob.end_fill()


def lounge_chair(bob: Turtle, x: float, y: float) -> None:
    """Something fun! Using the circle function to create a chair."""
    bob.speed(200)
    bob.penup()
    bob.goto(x, y)
    bob.pendown()
    bob.color(189, 34, 225)
    bob.left(45)
    bob.begin_fill()
    bob.circle(120, 180)
    bob.begin_fill()


def clouds(bob: Turtle, x: float, y: float) -> None:
    """Doing something fun again...using circles to create clouds."""
    bob.penup()
    bob.goto(x, y)
    bob.pendown()
    bob.color(255, 255, 255)
    bob.begin_fill()

    bob.circle(50)
    bob.end_fill()


if __name__ == "__main__":
    print("__name__ is ' __main__'")
    main()