import function
import os

ID, CATEGORY, PRODUCT, QUANTITY, PRICE = range(5)

list_options_for_main_menu = ["Press A to add to basket",
                              "Press P to pay",
                              "Press X to exit"
                              ]
list_options_for_basket_menu = ["Press R to remove item to basket",
                                'Press F to complete the oreder',
                                'Press C to change quantity to basket',
                                'Press X to exit',
                                "Press B to continue shopping"
                                ]


column_labels = ["ID", "Category", "Product", "Quantity", "Price"]
inventory = function.read_file("stock.csv")
h_char = "-"
v_char = " " * 5


def find_longest_item(list_of_items, label):
    str_length = len(column_labels[label])
    for item in list_of_items:
        if len(str(item[label])) > str_length:
            str_length = len(str(item[label]))
    return str_length


def max_lengths(list_of_items):
    return [find_longest_item(inventory, x) for x in range(5)]


def longest_row(list_of_items):
    return sum(max_lengths(list_of_items)) + (len(v_char) * (len(column_labels) - 1))


def print_list(list_of_items):
    lengths = max_lengths(list_of_items)
    print(f"{list_of_items[ID]:>{lengths[ID]}}".upper() + v_char +
          f"{list_of_items[CATEGORY]:<{lengths[CATEGORY]}}".upper() + v_char +
          f"{list_of_items[PRODUCT]:<{lengths[PRODUCT]}}".upper() + v_char +
          f"{list_of_items[QUANTITY]:>{lengths[QUANTITY]}}".upper() + v_char +
          f"{list_of_items[PRICE]:>{lengths[PRICE]}}".upper()
          )


def print_table(list_of_items, menu):
    os.system("clear")
    h_line = h_char * longest_row(list_of_items)
    length = longest_row(list_of_items)
    # header
    print(h_line)
    print(f" DUTY FREE ".upper().center(length, h_char))
    print(f" {str(menu)} ".upper().center(length, h_char))
    print(h_line)
    print_list(column_labels)
    for element in list_of_items:
        print(h_line)
        print_list(element)
    print(h_line)
    if menu == "basket":
        total = function.calculate_total(list_of_items)
        print(f"Total cos de cumparaturi = {total:,.2f} LEI".rjust(
            length).upper())
        print(h_line)


def get_single_input(text):
    return input(text)


def get_input(list_labels, title):
    inputs = []
    print(title)
    for i in range(0, len(list_labels)):
        user_input = input(f"\t{list_labels[i].title()}")
        inputs.append(user_input)
    return inputs


def print_menu(list_options):
    length = longest_row(list_options)
    h_line = h_char * length
    for option in list_options:
        print(option)
    print(h_line)


# print_menu(list_options_for_main_menu, "DUTY FREE")
