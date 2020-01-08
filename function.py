# read file, return a list
ID, CATEGORY, PRODUCT, QUANTITY, PRICE = range(5)

# read csv file


def read_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    for element in table:
        element[QUANTITY] = int(element[QUANTITY])
        element[PRICE] = float(element[PRICE])
    return table

# change qty from basket


def change_qunatity_from_bascket(item, quantity, bascket):
    for i in bascket:
        if item in i[ID]:
            if int(quantity) == i[QUANTITY]:
                bascket.remove(i)
            elif int(quantity) < i[QUANTITY]:
                index = bascket.index(i)
                bascket[index][QUANTITY] -= int(quantity)
            else:
                print("You not have this quantity in your bascket.")
    return bascket

# remove item from basket


def remove_from_bascket(item, bascket):
    for i in bascket:
        if item == i[ID]:
            bascket.remove(i)
    return bascket


# add to bascket
def add_basket(item, quantity, list_to_add, list_from_add):

    for i in list_from_add:
        if item in i[ID]:
            list_to_add.append(i)
            list_to_add[-1][QUANTITY] = int(quantity)
    return list_to_add


# write table in CSV
def write(basket):
    with open("stock.csv", "w") as csv_file:
        for item in range(len(basket)-1):
            csv_file.write(';'.join(map(str, basket[item])) + "\n")
        csv_file.write(';'.join(map(str, basket[len(basket)-1])))
    csv_file.close()


# sum for total
def suma(basket):
    list_sum_per_item = []
    for i in basket:
        list_sum_per_item.append(i[QUANTITY] * i[PRICE])
    total_sum = sum(list_sum_per_item)
    return total_sum


x = read_file("stock.csv")
print(x)
basket = [['2', 'Cigarets', 'Kent 8', 1, 21.0], ['3', 'Alcool',
                                                 'Ursus 330 ml', 2, 3], ['4', 'Food', 'Snickers', 1, 1.25]]

write(basket)
x = read_file("stock.csv")
print(x)


# y = [['2', 'Cigarets', 'Kent 8', 1, 21.0], ['3', 'Alcool',
#                                             'Ursus 330 ml', 25, 3.21], ['4', 'Food', 'Snickers', 30, 1.25]]
# print(y)
# change_qunatity_from_bascket("2", 1, y)
# print(y)
