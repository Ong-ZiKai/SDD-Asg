#loading of packages
import random
import os
import sys

#main menu function
def show_main_menu():
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Quit")
    print()
    while True:
        try:
            option = int(input('Your choice? '))
            break
        except:
            print('wrong input')
            
    return option

#main software
menu = show_main_menu()
