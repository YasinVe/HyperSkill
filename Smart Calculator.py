import re


class Calculator():
    def __init__(self):
        self.variables = {}
        self.ask()

    def check_varibale(self, variable):
        p = re.compile("^[A-Za-z]+$")
        if p.match(variable):
            return True
        else:
            return False

    def do_assignment(self, assignment):
        data = [i.strip() for i in assignment.split("=", 1)]
        if not re.compile("\+|-|\*|/").findall(data [1]):
            if self.check_varibale(data [0]):
                try:
                    self.variables [data [0]] = int(data [1])
                except ValueError:
                    if not self.check_varibale(data [1]):
                        print("Invalid assignment")
                    else:
                        try:
                            self.variables [data [0]] = self.variables [data [1]]
                        except KeyError:
                            print("Unknown variable")
            else:
                print("Invalid identifier")

        elif self.calculate(data [1]):
            self.variables [data [0]] = self.calculate(data [1])

    def calculate(self, data):
        p = re.compile("^[A-Za-z]+$")
        if p.match(data):
            print(self.variables.get(data,"Unknown variable"))
        else:
            data = list(data.replace(" ", ""))
            for i in data:
                if i.isalpha():
                    try:
                        data [data.index(i)] = f"{self.variables [i]}"
                    except:
                        break
            try:
                print(int(eval("".join(data))))
            except BaseException as err:
                if re.compile("name '[A-Za-z]+' is not defined").match(err.__str__()):
                    print("Unknown variable")
                else:
                    print('Invalid assignment')

    def ask(self):
        f = re.compile("^(([0-9]\D){2,}([\+\*/-]\D)+)+(([0-9]\D)*\D([\+\*/-]\D)*)*")
        while True:
            data = input()
            if f.match(data):
                self.calculate_postfix(data)
            elif data.count("/")>1:
                print("Invalid expression")
            elif data == '/exit':
                print("bye!")
                break
            elif data == '/help':
                self.show_help()
            elif data.startswith("/") and data not in ["/exit", "/help"]:
                print("Unknown command")
            elif not data:
                pass

            else:
                if "=" in data:
                    self.do_assignment(data)
                else:
                    self.calculate(data)

    def show_help(self):
        print("The program calculates the sum of numbers")

    def calculate_postfix(self,data):
        p = re.compile("^[\+\*-/]?$")
        a = data.split(" ")
        while len(a) != 1:
            for i in range(len(a)):
                if p.match(a [i]):
                    k = a [i - 2]
                    l = a [i - 1]
                    a [i - 2] = str(eval(a [i - 2] + a [i] + a [i - 1]))
                    del a [i - 1]
                    del a [i - 1]
                    break
        print(int(*a))
calculator = Calculator()

