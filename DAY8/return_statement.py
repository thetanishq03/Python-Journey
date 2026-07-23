#Program 1
def add(a,b):
    return a+b
result = add(5,3)
print(result)

#Program 2
def sub(a,b):
    return a-b
result = sub(5,3)
print(result)

#Program 3
def square(a):
    return a*a
result = square(5)
print(result)
 
#Program 4
def cube(a):
    return a*a*a
result = cube(5)
print(result)

#Program 5
def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
large = largest(11,3,28)
print(f"Largest: {large}")

#Program 6
def smallest(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else:
        return c
small = smallest(11,3,28)
print(f"Smallest: {small}")

#Program 7
def average(a,b,c):
    return a+b+c/3
avg = average(11,3,28)
print(f"Average: {avg}")
    