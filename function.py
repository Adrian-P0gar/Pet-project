# read file, return a list
ID, CATEGORY, PRODUCT, QUANTITY, PRICE = range(5)


def read_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    for element in table:
        element[QUANTITY] = f"{int(element[QUANTITY]):,}"
        element[PRICE] = f"{float(element[PRICE]):,.2f} Lei"
    return table

# remove item of list


def remove(item):
    pass

# add to bascket


def add_basket(item, quantity, list_to_add, list_from_add):

    for i in list_from_add:
        if item in i[ID]:
            list_to_add.append(i)
            list_to_add[-1][QUANTITY] = int(quantity)
    return list_to_add


# write table in CSV


def write():
    pass

# sum for total


def sum():
    pass


# print(read_file("stock.csv"))
# x = read_file("stock.csv")
# y = [['2', 'Cigarets', 'Kent 8', 1000, 21.0]]
# add_basket("3", 5, y, x)
# print(y)
