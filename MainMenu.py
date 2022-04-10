from prettytable import PrettyTable, NONE, ALL


def print_main_menu():
    message = PrettyTable()
    message.vrules = NONE
    message.field_names = ["Welcome to the shop!", "You may enter the following commands: "]


    message.add_rows(
                        [
                            ["q", " - quit the shop"],
                            ["h", " - help"],
                            ["view", " - view all the details on products"],
                            ["f", " - view available functions"]
                        ]
                    )

    message.vrules = ALL

    return print(message)
