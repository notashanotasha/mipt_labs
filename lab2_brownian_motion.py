import turtle
from random import *

turtle.shape('turtle')


def random_step():
    r_value = random()
    r_step = 100 * r_value
    return r_step


def random_angle():
    r_angle = randint(-360, 360)
    return r_angle


def draw_brownian():
    i = 1
    while i > 0:
        turtle.forward(random_step())
        turtle.left(random_angle())
        i += 1


draw_brownian()
