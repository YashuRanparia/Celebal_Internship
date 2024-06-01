
class Calculator:
    def __init__(self) -> None:
        self.a = 0
        self.b = 0
        self.operation()
        pass

    def add(self,a, b):
        print("a+b = ",a+b)

    def subtract(self,a,b):
        print("a+b = ",a-b)

    def multiplication(self,a,b):
        print("a+b = ",a*b)

    def division(self,a,b):
        print("a+b = ",a/b)

    def operation(self):
        status = True
        operations = [0,1,2,3,4]
        while status:
            operation_input = int(input("Enter the operation you want to perform: "))

            if operation_input != 0 and operation_input in operations:
                try:
                    self.a = int(input("Enter value of a: "))
                    self.b = int(input("Enter value of b: "))
                    pass
                except:
                    print("Invalid Inputs!. Please enter valid inputs.")
                    pass

            if operation_input == 1:
                self.add(self.a,self.b)
                pass
            elif operation_input == 2:
                self.subtract(self.a,self.b)
                pass
            elif operation_input == 3:
                self.multiplication(self.a,self.b)
                pass
            elif operation_input == 4:
                self.division(self.a,self.b)
                pass
            elif operation_input == 0:
                print("Calculator Stopped!")
                status = False
            else:
                print("Invalid operation!. Please enter a valid operation.")
        pass
    pass

if __name__ == '__main__':
    print('''
    Welcome to this calculator!
------------------------------------
    Operations are numbered as :
    +       ->  1
    -       ->  2
    *       ->  3
    /       ->  4
    exit    ->  0
------------------------------------
''')
    calc = Calculator()