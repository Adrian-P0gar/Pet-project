# read file, return a list


def read_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table

# remove item of list


def remove(item):
    pass

# add to bascket


def add_basket(item):
    pass

# write table in CSV


def write():
    pass

# sum for total


def sum():
    pass


print(read_file("/home/stefan/Codecool/Python/6th_TW_week/Pet-project/stock.csv"))