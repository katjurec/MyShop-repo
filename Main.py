# This is the main file of the shop database.
# This file contains main functionality and references to other modules used in the project.

import MainMenu as Mm

Mm.print_main_menu()
while True:
    command = input()

    if command == 'q':
        quit()
    elif command == 'h':
        Mm.print_main_menu()
    elif command == 'fun':
        print("hi")



