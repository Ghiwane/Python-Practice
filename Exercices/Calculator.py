class calculator:
    def __init__(self):
        self.n=0
        self.history_list=[]

    def addition(self, a, b):
        self.n+=1
        res = a+b
        self.history_list.append(f"{a} + {b} = {res}")
        print(res)
    
    def division(self, a, b):
        try:
            self.n+=1
            res = float(a/b)
            self.history_list.append(f"{a} / {b} = {res}")
            print(res)
        except ZeroDivisionError:
            print("We can't, buddy.")

    def multiplication(self, a, b):
        self.n+=1
        res = a*b
        self.history_list.append(f"{a} * {b} = {res}")
        print(res)
    
    def subtraction(self, a, b):
        self.n+=1
        res = a-b
        self.history_list.append(f"{a} - {b} = {res}")
        print(res)
    
    def __str__(self):
        return f"Calculator {self.n} operations"

    def history(self):
        for operation in self.history_list:
            print(operation)

calc = calculator()
calc.addition(10, 5)
calc.division(10, 0)
calc.multiplication(3, 4)
calc.history()
print(calc)