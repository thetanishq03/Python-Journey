#MINIPROJECT1: CALVULATOR USING FUNCTIONS
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

while True:
    choice = int(input("""1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit\nEnter your choice: """))
    if choice == 5:
        print("Exiting..")
        break
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))
    if choice == 1:
        addition = add(a,b)
        print(f"Addition: {addition}")
    elif choice == 2:
        subtraction = subtract(a,b)
        print(f"Subtraction: {subtraction}")
    elif choice == 3:
        multiplication = multiply(a,b)
        print(f"Multiplication: {multiplication}")
    elif choice == 4:
        division = divide(a,b)
        print(f"Division: {division}")