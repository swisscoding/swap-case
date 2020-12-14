#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Swap case of input | ----\n", fg("red")))

# user interaction
user_input = input("Your text: ")

# options
print(stylize("\nOptions:", fg("green")))
print("> 'u' for all upper case\n> 'l' for all lower case\n> 'm' for mixed case")

# user interaction
user_choice = input(": ").lower()

# main program
if user_choice == "u":
    print(f"\nSwapped case to all upper case: {user_input.upper()}\n")
elif user_choice == "l":
    print(f"\nSwapped case to all lower case: {user_input.lower()}\n")
elif user_choice == "m":
    new_text = ""
    for i in user_input:
        if i == i.upper():
            new_text += i.lower()
        else:
            new_text += i.upper()
    print(f"\nSwapped case to mixed case: {new_text}\n")
else:
    print("\nInvalid Input\n")
