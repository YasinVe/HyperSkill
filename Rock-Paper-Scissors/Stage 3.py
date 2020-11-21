import random

win = {'scissors':'rock','paper':'scissors','rock':'paper'}
choices=["scissors", "paper", "rock"]

while True:
    user_select = input()
    comp_select = random.choice(choices)
    if user_select == "!exit":
        print("Bye!")
        break
    elif user_select in choices:
        if  user_select == comp_select:
            print(f"There is a draw ({comp_select})")
        elif win[user_select] == comp_select:
            print(f"Sorry, but the computer chose {comp_select}")
        else:
            print(f"Well done. The computer chose {comp_select} and failed")
    else:
        print("Invalid input")
