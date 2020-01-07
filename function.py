# read file, return a list
ID, CATEGORY, PRODUCT, QUANTITY, PRICE = range(5)


def read_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    for element in table:
        element[QUANTITY] = int(element[QUANTITY])
        element[PRICE] = float(element[PRICE])
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


print(read_file("stock.csv"))
