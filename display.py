import function
ID, CATEGORY, PRODUCT, QUANTITY, PRICE = range(5)
inventory_labels = ["ID", "Category", "Product", "Quantity", "Price"]
inventory = function.read_file("stock.csv")
h_char = "-"
v_char = "     "


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


# show list of items
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


print_table(inventory, "inventory")


# get input
def get_input(text, list_labels):
    pass


# print error message
def print_error_message(message):
    pass

# show menu options
def print_menu(title, list_options, exit_message):
    pass
