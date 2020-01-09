import display
import payment
import function
import store
import os
list_options_for_main_menu = [
    "Press A to add to basket", "Press P to pay", "Press X to exit"]
list_options_for_basket_menu = ["Press R to remove item to basket", 'Press C to change quantity to basket',
                                'Press F to complete the oreder', 'Press X to exit', "Press B to continue shopping"]


def main():
    basket = []
    while True:
        option = "0"
        if option == "0":
            stock = function.read_file("stock.csv")
            display.print_table(stock, "inventory")
            display.print_menu(list_options_for_main_menu)
            get_input = display.get_input(["Enter your option!"], "")
            option = get_input[0]

        if option.lower() == "a":
            while True:
                items_for_basket = display.get_single_input("Choose id: ")
                if function.check_id(items_for_basket, stock):
                    quantity_for_basket = display.get_single_input(
                        "Quantity: ")

                    if function.check_quantity(items_for_basket, quantity_for_basket, stock):

                        function.add_basket(
                            items_for_basket, quantity_for_basket, basket, stock)
                    else:
                        print("Not enough quantity! ")
                else:
                    print("Not in stock!")
                second_choose = display.get_input(
                    ["Do you want to add something? "], "")
                if second_choose[0].lower() == "no":
                    os.system('clear')
                    break
            option = "0"
        if option.lower() == "x":
            os.system('clear')
            exit()
        while option.lower() == "p":
            os.system('clear')
            display.print_table(basket, "basket")
            display.print_menu(list_options_for_basket_menu)
            second_choose = display.get_single_input('Choose the option: ')
            if second_choose.lower() == "r":
                id_for_remove = display.get_single_input(
                    "Choose the item for complet remove! ")
                function.remove_from_bascket(id_for_remove, basket)
                os.system('clear')
                option = "p"
            if second_choose.lower() == 'c':
                id_for_cahnge_quantity = display.get_single_input(
                    "Choose the item to change the quantity! ")
                if function.check_id(id_for_cahnge_quantity, basket):
                    quantity_for_cahange = display.get_single_input(
                        "Choose quantity! ")
                    if function.check_quantity(id_for_cahnge_quantity, quantity_for_cahange, basket):
                        function.change_qunatity_from_bascket(
                            id_for_cahnge_quantity, quantity_for_cahange, basket)
                        option = 'p'
                    else:
                        print('You do not have this quantity in the basket!')
                        option = "p"
                else:
                    print('You do not have this item in the basket!')
                    option = 'p'
            if second_choose.lower() == 'f':
                a = 0
                while a < 3:
                    to_valid = function.card_payment()
                    if function.validate_card_details(to_valid):
                        function.write(function.update_stock(basket))
                        print(
                            "Nu ai bani pe card sarakule!!!, Mars la munca baaa, lepra ce esti! Oricum nu stii sa citesti. ")
                        exit()
                    else:
                        a += 1
            if second_choose.lower() == 'b':
                option = "0"
                break
            if second_choose.lower() == 'x':
                os.system('clear')
                exit()


if __name__ == "__main__":
    main()
