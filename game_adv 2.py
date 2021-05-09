# Andrew A.
# April 2021

import time
import random


enemy_list = ["Hairyman", "Grizzlybear", "Bobcat"]
enemy_choice = random.choice(enemy_list)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause(
       "You take your family on a "
       "retreat in a cabin in the forest."
    )
    print_pause(
        f"Upon arriving you notice a warning of DANGER"
        " in this area."
    )
    print_pause(
        "As day turns to night"
        " you and the family go for a walk to explore."
    )
    print_pause(
        "while on your hike you discover an old mine,"
        "and hunting shack."
    )


def hunting_shack(items):
    print_pause(
        f"On approaching the shack a {enemy_choice}"
        " leaps out the window and attacks you!"
    )
    fight = input(
        "What do you do?\nEnter 1. to fight\nEnter 2. To run\n"
    )
    if fight == "1":
        if "Wood Axe" in items:
            print_pause(
                "You attack the enemy with your Wood Axe and defeat it!")
            print_pause(
                "Your family survives the ordeal")
        else:
            print_pause(
                "You protect your family and fight bare handed.")
            print_pause(
                "This is pointless you are defeated.")
            print_pause(
                "Attempt again when better prepared.")
    elif fight == "2":
        print_pause("You all get away safely")
        explore_wilderness(items)
    else:
        hunting_shack(items)


def mine(items):
    if "Wood Axe" in items:
        print_pause(
            "You have searched the mine, and found a Wood Axe."
        )
        explore_wilderness(items)
    else:
        print_pause(
            "Upon searching the old mine, you realize as you walk in,"
            "its closed off."
        )
        print_pause(
            "You look around and notice a Wood Axe"
            " in the dirt and grab it."
        )
        items.append("Wood Axe")
        print_pause("You exit the mine")
        explore_wilderness(items)


def explore_wilderness(items):
    print_pause("Where do you go?")
    choice = input(
        "Enter 1 to go to the shack\n"
        "Enter 2 search mine\n"
    )
    if choice == "1":
        hunting_shack(items)
    elif choice == "2":
        mine(items)
    else:
        print_pause("That is not an option, please choose 1 or 2")
        explore_wilderness(items)


def play_again():
    print_pause("Game Over")
    again = input("Try again?\nY for yes\nN for no\n").lower()
    if again == "y":
        play_game()
    elif again == "n":
        print_pause("Thank you for playing!")
        quit()
    else:
        print_pause("Try again?\nY for yes\nN for no\n")
        play_again()


def play_game():
    items = []
    intro()
    explore_wilderness(items)
    play_again()


play_game()
