# MINIPROJECT3: UTILITY TOOLKIT
def even_odd(num):
    if num % 2 == 0:
        return "Its even."
    else:
        return "Its odd."
    
def prime(num):
    for i in range(2, num):
        if num <= 1 or num % i == 0 :
            return "Not a prime number."
        else:
            return "Its a prime number."
        
def factorial(num):
    factorial_ = 1
    if num < 0:
        return "Negative number do not have factorial."
    elif num == 0:
        return "Factorial of 0: 1"
    else:
        for i in range(1, num+1):
            factorial_ = factorial_ * i
        print(f"Factorial of {num} :  {factorial_}")
        
def table(num):
    for i in range(1, 11):
        print(f"{num}x {i} = {num * i}")

num = int(input("Enter a number: "))
while True:
    choice = int(input("""**Menu**\n1.Even odd checker\n2.Prime number checker\n3.Factorial\n4.Multiplication table\n5.Exit\nEnter your choice: """))
    # num = int(input("Enter a number: "))
    if choice == 1:
        even_odd_ = even_odd(num)
        print(even_odd_)
    elif choice == 2:
        prime_ = prime(num)
        print(prime_)
    elif choice == 3:
        factorial(num)
    elif choice == 4:
        table(num)
    else:
        print("Exitingg...")
        break