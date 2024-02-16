"""

MATCH - CASE

Since there is no switch in python we have MATCH - CASE for doing the same, in python we do not need the break after each case

"""

numbers = int(input("Enter a number and I will try to guess if possible "))

match numbers:
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case _:
        print("Sorry, I have no idea")