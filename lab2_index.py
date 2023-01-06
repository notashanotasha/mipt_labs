import turtle
import math

turtle.shape('turtle')


def create_list(list_str: str):
    # new_list = [int(list_str[i]) for i in range(len(list_str))]
    # new_list = []
    # for i in range(len(list_str)):
    #     new_list.append(int(list_str[i]))
    # return [int(list_str[i]) for i in range(len(list_str))]
    return [int(char) for char in list_str]


def draw_figure(figure_val: int):
    step = 40
    if figure_val == 0:
        turtle.penup()
        turtle.pendown()
        turtle.forward(step)
        turtle.right(90)
        turtle.forward(2*step)
        turtle.right(90)
        turtle.forward(step)
        turtle.right(90)
        turtle.forward(2*step)
        turtle.penup()
        turtle.right(90)
        turtle.forward(step+5)
    elif figure_val == 1:
        turtle.penup()
        turtle.right(90)
        turtle.forward(step)
        turtle.right(180+45)
        turtle.pendown()
        turtle.forward(math.sqrt((step**2)+(step**2)))
        turtle.right(90+45)
        turtle.forward(2*step)
        turtle.penup()
        turtle.right(180)
        turtle.forward(2*step)
        turtle.right(90)
        turtle.forward(5)
        turtle.pendown()


def draw_index(index: list):
    # index_len = len(index)
    # counter = 0
    for figure in index:
        draw_figure(figure)


def draw_index_from_str(index_str: str):
    draw_index(create_list(index_str))


# draw_index_from_str('00101011')
# def print_list(list_str: str):
#     print(create_list(list_str))
# print_list('123456')
# draw_figure(0)
# draw_figure(1)
# draw_figure(0)
# draw_figure(1)
