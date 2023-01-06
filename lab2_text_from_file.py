# with open('test_input.txt') as file:
#     for line in file:
#          print(line)

def read_from_file():
#    open_file = open('test_input.txt', 'r')
    with open('test_input.txt', 'r') as open_file:
        read = open_file.readlines()
        for word in read:
            print(word.rstrip())
    # open_file.close()


# read_from_file()


def read_first_line(filename: str):
    with open(filename, 'r') as open_file:
        return open_file.readline()
