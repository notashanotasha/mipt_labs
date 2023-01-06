from lab2_text_from_file import read_first_line
from lab2_index import draw_index_from_str


def draw_index_from_file(filename: str):
    draw_index_from_str(read_first_line(filename))


draw_index_from_file("input.txt")