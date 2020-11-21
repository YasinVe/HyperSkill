import random

win = {'scissors':'rock','paper':'scissors','rock':'paper'}
choices=["scissors", "paper", "rock"]

# file = open("rating.txt",'a')
# file.close()

def show_rating(username):
     with open("rating.txt",'r') as f:
            for i in f.readlines():
                if username in i:
                    rating = int(i.strip().split(" ")[1])
                    return rating
                
user = input("Enter your name:")
print(f"Hello, {user}")
rating = show_rating(user) or 0

while True:
    user_select = input()
    comp_select = random.choice(choices)
    
    if user_select == "!exit":
        print("Bye!")
        break
        
    elif user_select == "!rating":
        print("Your rating:",rating)
        
    elif user_select in choices:
        if  user_select == comp_select:
            print(f"There is a draw ({comp_select})")
            rating += 50
            
        elif win[user_select] == comp_select:
            print(f"Sorry, but the computer chose {comp_select}")
            
        else:
            print(f"Well done. The computer chose {comp_select} and failed")
            rating += 100
    else:
        print("Invalid input")
        
