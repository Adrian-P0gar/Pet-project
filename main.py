import display
import payment
import function
import store
import os
list_options_for_main_menu = [
    "Press A to add to basket", "Press P to pay", "Press X to exit"]
list_options_for_basket_menu = ["s"]


def main():
    stock = function.read_file("stock.csv")
    print(stock)
    display.print_menu(list_options_for_main_menu, "DUTY FREE")
    get_input = display.get_input(["Enter your option!"], "")
    option = get_input[0]
    basket = []

    if option.lower() == "a":
        while True:
            items_for_basket = display.get_input(
                ["Enter item ID: ", "How many: "], "")
            try:
                function.add_basket(
                    items_for_basket[0], items_for_basket[1], basket, stock)
            except ValueError:
                print("No stock!")
            second_choose = display.get_input(
                ["Do you want to add something? "], "")
            os.system('clear')
            if second_choose[0].lower() == "no":
                return False
    if option.lower() == "x":
        os.system('clear')
        exit()
    if option.lower() == "p":
        print("paid")


if __name__ == "__main__":
    main()
