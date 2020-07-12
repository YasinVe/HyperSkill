class CoffeeMachine:
    def __init__(self, water=400, milk=540, coffee=120, cup=9, money=550):
        self.avilable_water = water
        self.avilable_milk = milk
        self.avilable_coffee = coffee
        self.disposal_cup = cup
        self.avilable_money = money
        self.ask()

    def show(self):
        print()
        print(f"The coffee machine has:")
        print(f"{self.avilable_water} of water")
        print(f"{self.avilable_milk} of milk ")
        print(f"{self.avilable_coffee} of coffee beans")
        print(f"{self.disposal_cup} of disposable cups")
        print(f"${self.avilable_money} of money")
        print()

    def ask(self):
        while True:
            ask = input("Write action (buy, fill, take, remaining, exit):")
            if ask == 'remaining':
                self.show()
            if ask == 'buy':
                self.choose_coffee()
            elif ask == 'fill':
                water = int(input("Write how many ml of water do you want to add:"))
                milk = int(input("Write how many ml of milk do you want to add:"))
                coffee = int(input("Write how many grams of coffee beans do you want to add:"))
                cup = int(input("Write how many disposable cups of coffee do you want to add:"))
                self.fill(add_water=water, add_milk=milk, add_coffee=coffee, add_cup=cup)
            elif ask == 'take':
                self.take_money()
            if ask == 'exit':
                break

    def make(self, water=0, milk=0, coffee=0, cup=1):
        boolean = [self.avilable_water >= water, self.avilable_milk >= milk, \
                   self.avilable_coffee >= coffee, self.disposal_cup >= 1]
        ingredients = ['water', 'milk', 'cofee', 'cup']
        for i in boolean:
            if not i:
                return f"Sorry, not enough {ingredients [boolean.index(i)]}!"
            else:
                self.avilable_water -= water
                self.avilable_coffee -= coffee
                self.disposal_cup -= cup
                self.avilable_milk -= milk
                return "I have enough resources, making you a coffee!"

    def choose_coffee(self):
        k = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if k == "1":
            self.buy_espresso()
        elif k == "2":
            self.buy_latte()
        elif k == '3':
            self.buy_cappuccino()
        elif k == 'back':
            pass

    def buy_espresso(self):
        print("For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.")
        self.make(water=250, coffee=16)
        self.avilable_money += 4

    def buy_latte(self):
        print(
            "For a latte, the coffee machine needs 350 ml of water,75 ml of milk, and 20 g of coffee beans.It costs $7.")
        self.make(water=350, coffee=20, milk=75)
        self.avilable_money += 7

    def buy_cappuccino(self):
        print(
            'And for a cappuccino, the coffee machine needs 200 ml of water,100 ml of milk, and 12 g of coffee. It costs $6.')
        self.make(water=200, coffee=12, milk=100)
        self.avilable_money += 6

    def fill(self,add_water=0,add_milk=0,add_coffee=0,add_cup=0):
        self.avilable_water += add_water
        self.avilable_coffee += add_coffee
        self.disposal_cup += add_cup
        self.avilable_milk += add_milk

    def take_money(self):
        print(f"I gave you ${self.avilable_money}")
        self.avilable_money = 0

coffee=CoffeeMachine()
