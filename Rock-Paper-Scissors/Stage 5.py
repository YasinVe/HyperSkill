import random
user = input("Enter your name:")
print(f"Hello, {user}")
win = {'scissors':['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],\
       'paper':['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],\
       'rock':['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],\
       'lizard':['spock','rock'],
       'human':['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],\
       'wolf':['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],\
       'devil':['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning'],\
       'tree':['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],\
       'dragon':['human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],\
       'fire':['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],\
       'sponge':['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],\
       'air':['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],\
       'gun':['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],\
       'snake':['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],\
       'lightning':['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],\
       'water':['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon']}
       
choice = input()
choices = choice.split(",") if choice else ["scissors", "paper", "rock"]
print("Okay, let's start")
# file = open("rating.txt",'w')
# file.close()

def show_rating(username):
     with open("rating.txt",'r') as f:
            for i in f.readlines():
                if username in i:
                    rating = int(i.strip().split(" ")[1])
                    return rating
                


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
            
        elif comp_select in win[user_select]:
            print(f"Well done. The computer chose {comp_select} and failed")
            rating += 100
            
        else:
            print(f"Sorry, but the computer chose {comp_select}")
           
    else:
        print("Invalid input")
        
