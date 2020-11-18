data=str(" "*9).replace(""," ")
next_player=True
play=True
wins=[]

def print_table(data):
    print("-" * len("|" + data[0:3].replace(""," ") + "|"))
    print("|" + data[0:3].replace(""," ") + "|")
    print("|" + data[3:6].replace(""," ") + "|")
    print("|" + data[6:9].replace(""," ") + "|")
    print("-" * len("|" + data[0:3].replace(""," ") + "|"))

print_table(data)

def player(c):
    global data,next_player
    if data[x-1 + (3 - y) * 3] == " ":
        data=list(data)
        data[x-1 + (3 - y) * 3] = c
        data = ''.join(data)
        print_table(data)
    else:
        print("This cell is occupied! Choose another one!")
        next_player= not next_player
    return data

def check_winner():
    global play
    if data[0:3].count('X') == 3 or data[3:6].count('X') == 3 or data[6:].count('X') == 3 or \
    data[0] == data[3] == data[6] == 'X' or \
    data[1] == data[4] == data[7] == 'X' or \
    data[2] == data[5] == data[8] == 'X' or \
    data[2] == data[4] == data[6] == 'X' or \
    data[0] == data[4] == data[8] == 'X':
        wins.append("X wins")

    if data[0:3].count('O') == 3 or data[3:6].count('O') == 3 or data[6:].count('O') == 3 or \
    data[0] == data[3] == data[6] == 'O' or \
    data[1] == data[4] == data[7] == 'O' or \
    data[2] == data[5] == data[8] == 'O' or \
    data[2] == data[4] == data[6] == 'O' or \
    data[0] == data[4] == data[8] == 'O':
         wins.append("O wins")
    if wins:
        if len(wins) == 1:
            print(wins[0])
            play=False
            
        else:
            print("Impossible")
while True:
    check_winner()
    if not play:
        break
    if not -1 <= data.count("X") - data.count("O") <= 1:
        print("Impossible")
    elif not data.count("X") + data.count("O") == 9:
        while True:
            if not " " in data:
                break
            inp = input("Enter the coordinates:")
            try:
                x,y=[int(i) for i in inp.split(" ")]
            except:
                print("You should enter numbers!")
                continue
            if 1 <= x <= 3 and 1 <= y <= 3:
                if next_player:
                    next_player=False
                    player('X') 
                else:
                    next_player=True
                    player('O')
                break
            else:
                print("Coordinates should be from 1 to 3!")
    else:
        print("Draw")
        break
