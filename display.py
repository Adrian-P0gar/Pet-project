import function
ID, CATEGORY, PRODUCT, QUANTITY, PRICE = range(5)
inventory_labels = ["ID", "Category", "Product", "Quantity", "Price"]
inventory = function.read_file("stock.csv")
h_char = "-"
v_char = " " * 5


def calculate_total(list_of_items):
    total = 0
    for element in list_of_items:
        total += float(element[PRICE].replace(",", "").split(" ")[0])
    return total


def find_longest_item(list_of_items, label):
    str_length = len(inventory_labels[label])
    for item in list_of_items:
        if len(str(item[label])) > str_length:
            str_length = len(str(item[label]))
    return str_length


max_column_lengths = [find_longest_item(inventory, x) for x in range(5)]
longest_row = sum(max_column_lengths) + (len(v_char) * (len(inventory_labels) - 1))


def print_list(list_of_items, length=max_column_lengths):
    print(f"{list_of_items[ID]:>{length[ID]}}".upper() + v_char +
          f"{list_of_items[CATEGORY]:<{length[CATEGORY]}}".upper() + v_char +
          f"{list_of_items[PRODUCT]:<{length[PRODUCT]}}".upper() + v_char +
          f"{list_of_items[QUANTITY]:>{length[QUANTITY]}}".upper() + v_char +
          f"{list_of_items[PRICE]:>{length[PRICE]}}".upper()
          )


def print_table(list, menu):
    h_line = h_char * longest_row
    # header
    print(h_line)
    print(f" DUTY FREE ".upper().center(longest_row, "-"))
    print(f" {str(menu)} ".upper().center(longest_row, "-"))
    print(h_line)
    print_list(inventory_labels)
    for element in list:
        print(h_line)
        print_list(element)
    print(h_line)
    if menu == "basket":
        print(f"Total cos de cumparaturi = {calculate_total(list):,} LEI".rjust(
            longest_row).upper())
        print(h_line)


def get_input(list_labels, title):
    inputs = []
    print(title)
    for i in range(0, len(list_labels)):
        user_input = input(f"\t{list_labels[i].title()}")
        inputs.append(user_input)
    return inputs


def print_error_message(message):
    pass


list_options_for_main_menu = [
    "Press A to add to basket", "Press P to pay", "Press X to exit"]


def print_menu(list_options, title):
    print("\n", title.center(
        max([len(str(x)) for x in list_options])), "\n")

    for option in list_options:
        print(option)


# print_menu(list_options_for_main_menu, "DUTY FREE")
