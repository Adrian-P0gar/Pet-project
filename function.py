import re
# read file, return a list
ID, CATEGORY, PRODUCT, QUANTITY, PRICE = range(5)

# read csv file


def read_file(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    for element in table:
        element[QUANTITY] = f"{int(element[QUANTITY])}"
        element[PRICE] = f"{float(element[PRICE]):.2f}"
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

    for j in list_to_add:
        if item in j:
            if item == j[ID]:
                j[QUANTITY] += int(quantity)
                return list_to_add
        else:
            pass
    for i in list_from_add:
        if item == i[ID]:
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


# verify id

def check_id(product_id, list_of_items):
    list_of_all_IDs = [product_id[ID] for product_id in list_of_items]
    return product_id in list_of_all_IDs

#  verify qantity


def check_quantity(product_id, quantity, list_of_items):
    product = []
    for element in list_of_items:
        if element[ID] == product_id:
            product = element
    return int(quantity) <= int(product[QUANTITY])


# payment
def card_payment():
    card_questions = ["Card number: ", "CVV: ", "Holder's name: "]
    card_details = []
    for i in card_questions:
        # x = function.get_single_input(i)
        x = input(i)
        card_details.append(x)
    return card_details


def validate_card_details(validate_data):
    validation = []
    try:
        x = re.match("^4[0-9]{12}(?:[0-9]{3})?$", validate_data[0])
        validation.append(x.group())
    except AttributeError:
        print('Card Number Error!')
    try:
        y = re.match("^[0-9]{3}$", validate_data[1])
        validation.append(y.group())
    except AttributeError:
        print('CVV Error!')
    try:
        z = re.match("^[A-Z][a-z]+\s[A-Z][a-z]+$", validate_data[2])
        validation.append(z.group())
    except AttributeError:
        print('Name Error!')

    if len(validation) == 3:
        print("Payment complete")
        return True


def update_stock(basket):
    intermediary_stock = read_file(
        "/home/pogar/Python module/SI 6/Pet-project/stock.csv")
    for i in basket:
        for x in intermediary_stock:
            if i[ID] == x[ID]:
                x[QUANTITY] = int(x[QUANTITY]) - i[QUANTITY]
    return intermediary_stock


def calculate_total(list_of_items):
    total = 0
    for element in list_of_items:
        total += float(element[PRICE]) * float(element[QUANTITY])
    return total
