import re
import random, string

words = ['python', 'java', 'kotlin', 'javascript']
print(*"HANGMAN")

word = random.choice(words)
count = 0
word_list = ["-" for i in word]
entered_letter = set()
while True:
    choose = input("Type 'play' to play the game, 'exit' to quit:")
    if choose == 'play':
        while count < 8:
            if "".join(word_list) == word:
                print("You guessed the word!\nYou survived!\n")
                break

            print("\n", "".join(word_list))
            ask = input("Input a letter:")

            if len(ask) != 1:
                print("You should input a single letter\n")

            elif ask not in string.ascii_lowercase:
                print("It is not an ASCII lowercase letter\n")

            elif ask in entered_letter:
                print("You already typed this letter\n")

            else:
                entered_letter.add(ask)
                pattern = re.compile(rf"{ask}")

                if ask in word:
                    for i in pattern.finditer(word):
                        word_list[i.span()[0]] = ask
                else:
                    count += 1
                    print("No such letter in the word")
        else:
            print("You are hanged!\n")
    elif choose == 'exit':
        break
    continue
