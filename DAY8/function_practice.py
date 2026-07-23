#Question 1
def say_hello():
    print("Hello Python")

say_hello()

#Question 2
def square(number):
    return number*number

number = int(input("Enter a number: "))
squaree = square(number)
print(f"Square of {number}: {squaree}")

#Question 3
def maximum(a,b):
    if a>b:
        return a
    else:
        return b

largest = maximum(11,3)
print(f"Largest: {largest}")

#Question 4
def even_or_odd(number):
    if number%2 == 0:
        return "Even"
    else:
        return "Odd"

odd_even = even_or_odd(3)
print(f"{number} is {odd_even}")

#Question 5
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

factoriall = factorial(5)
print(f"Factorial: {factoriall}")