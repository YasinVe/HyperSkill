data=input("Enter cells:")
wins=[]

print("-" * len("|" + data[0:3].replace(""," ") + "|"))
print("|" + data[0:3].replace(""," ") + "|")
print("|" + data[3:6].replace(""," ") + "|")
print("|" + data[6:9].replace(""," ") + "|")
print("-" * len("|" + data[0:3].replace(""," ") + "|"))
    
if data[0:3].count('X') == 3 or data[3:6].count('X') == 3 or data[6:].count('X') == 3 or \
data[0] == data[3] == data[6] == 'X' or data[1] == data[4] == data[7] == 'X' or data[2] == data[5] == data[8] == 'X' or \
data[2] == data[4] == data[6] == 'X' or data[0] == data[4] == data[8] == 'X':
    wins.append("X wins")

if data[0:3].count('O') == 3 or data[3:6].count('O') == 3 or data[6:].count('O') == 3 or \
data[0] == data[3] == data[6] == 'O' or data[1] == data[4] == data[7] == 'O' or data[2] == data[5] == data[8] == 'O' or \
data[2] == data[4] == data[6] == 'O' or data[0] == data[4] == data[8] == 'O':
     wins.append("O wins")

elif not -1 <= data.count("X") - data.count("O") <= 1:
    print("Impossible")
        
elif not data.count("X") + data.count("O") == 9:
    print("Game not finished")
else:
    print("Draw")

if wins:
    if len(wins) == 1:
        print(wins[0])
    else:
        print("Impossible")
