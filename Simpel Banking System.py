# Write your code here
import random
import sqlite3

class BankCard:
    def __init__(self):
        self.bool = True
        self.data = sqlite3.connect('card.s3db')
        self.db = self.data.cursor()
        self.create_database()
        self.ask()

    def ask(self):
        while self.bool:
            choice = input("1. Create an account\n2. Log into account\n0. Exit\n")
            if choice == "1":
                self.create_card()
            elif choice == "2":
                self.log_in()
            else:
                print('Bye!')
                break

    def create_card(self):
        pin = str(random.randint(0, 10000)).rjust(4, '0')
        card_number = self.luhn_algoritm('400000' + str(random.randint(0, 1000000000)).rjust(9, '0'))
        self.add_database(card_number, pin)
        print(f"Your card has been created\nYour card number:\n{card_number}\nYour card PIN:\n{pin}")

    def log_in(self):
        c_num = input("Enter your card number:\n")
        p = input("Enter your PIN:\n")
        data = self.check(c_num, p)
        print("Wrong card number or PIN!") if not data else self.account(c_num)

    def account(self, c_num):
        print("You have successfully logged in!")
        while True:
            c = input("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n")
            if c == "1":
                print(f"Balance:{self.show_balance(c_num)}")
            elif c == '2':
                print(self.add_income(c_num))
            elif c == '3':
                print(self.transfer(c_num))
            elif c == '4':
                print(self.close_account(c_num))
                break
            elif c == '5':
                print("You have successfully logged out!")
                break
            else:
                self.bool = False
                break

    def luhn_algoritm(self, card_number):
        def check(x):
            return x - 9 if x > 9 else x
        checksum = list(map(int, list(card_number)))
        luhn = []
        for i in range(len(checksum)):
            if (i + 1) % 2 == 1:
                luhn.append(checksum[i] * 2)
            else:
                luhn.append(checksum[i])
        luhn = list(map(check, luhn))
        checksum.append(0 if sum(luhn) % 10 == 0 else (sum(luhn) // 10 + 1) * 10 - sum(luhn))
        return ''.join(map(str, checksum))

    def create_database(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS card (
                        id INTEGER,
                        number TEXT,
                        pin TEXT,
                        balance INTEGER DEFAULT 0)""")
        self.data.commit()

    def add_database(self, card_number, pin, balance=0):
        self.db.execute("""INSERT INTO card(number,pin,balance) VALUES(?,?,?)""", (card_number, pin, balance))
        self.data.commit()

    def check(self, card_number, pin):
        banker = self.db.execute("""SELECT * FROM card WHERE number=? and pin=?""", (card_number, pin))
        self.data.commit()
        return banker.fetchone()

    def add_income(self, number):
        income = int(input("Enter income:\n"))
        self.db.execute(f"UPDATE card set balance=balance+{income} where number={number}")
        self.data.commit()
        return "Income was added!"

    def show_balance(self, number):
        data = self.db.execute(f"""SELECT * FROM card WHERE number={number}""")
        self.data.commit()
        return data.fetchone()[3]

    def transfer(self, sender):
        sender_money = self.db.execute(f"""SELECT * FROM card WHERE number={sender}""").fetchone()[3]
        receiver = input("Enter card number:\n")
        receiv = self.db.execute(f"""SELECT * FROM card WHERE number={receiver}""").fetchone()
        if sender == receiver:
            return "You can't transfer money to the same account!"
        elif receiv:
            sent_money = int(input("Enter how much money you want to transfer:\n"))
            if sent_money <= sender_money:
                self.db.execute(f"""UPDATE card set balance=balance-{sent_money} WHERE number={sender}""")
                self.db.execute(f"""UPDATE card set balance=balance+{sent_money} WHERE number={receiver}""")
                self.data.commit()
                return 'Succes!'
            else:
                return "Not enough money!"
        elif receiver != self.luhn_algoritm(receiver[:-1]):
            return "Probably you made mistake in the card number. Please try again!"
        else:
            return "Such a card does not exist."

    def close_account(self, number):
        self.db.execute(f"DELETE FROM card WHERE number={number}")
        self.data.commit()
        return "The account has been closed!"

card = BankCard()
