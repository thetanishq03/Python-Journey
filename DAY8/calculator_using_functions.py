def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

while True:
    print("**MENU**\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        addition = add(a,b)
        print(f"Addition of {a} and {b}: {addition}")
    elif choice == 2:
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        subtraction = subtract(a,b)
        print(f"Subtraction of {a} and {b}: {subtraction}")
    elif choice == 3:
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        multiplication = multiply(a,b)
        print(f"Multiplication of {a} and {b}: {multiplication}")
    elif choice == 4:
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        division = divide(a,b)
        print(f"Division of {a} and {b}: {division}")
    elif choice == 5:
        print("Exitingggg....")
        break
