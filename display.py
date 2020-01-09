import function

# show list of items


def print_table(list):
    pass

# get input


def get_input(list_labels, title):
    inputs = []
    print(title)
    for i in range(0, len(list_labels)):
        user_input = input(f"\t{list_labels[i].title()}")
        inputs.append(user_input)
    return inputs


# femei = ['maria', "ion", 'george']
# x = get_input(femei, "Boom Kiss!")
# print(x)


def print_error_message(message):
    pass

# show menu options


list_options_for_main_menu = [
    "Press A to add to basket", "Press P to pay", "Press X to exit"]


def print_menu(list_options, title):
    print("\n", title.center(
        max([len(str(x)) for x in list_options])), "\n")

    for option in list_options:
        print(option)


# print_menu(list_options_for_main_menu, "DUTY FREE")
