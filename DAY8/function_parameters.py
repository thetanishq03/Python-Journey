#Program 1
def greet(name):
    print("Hello", name)

greet("Tanishq")

#Program 2
def student(name, marks):
    print(f"Name: {name}\nMarks: {marks}")
    
student("Tanishq", 90)

#Program 3
def areaofrectangle(length, breadth):
    area = length*breadth
    print(f"Area of rectangle: {area}")
    
areaofrectangle(10, 15)

#Program 4
def simpleinterest(p, r, t):
    si = p*r*t/100
    print(f"Simple Interest: {si}")
    
simpleinterest(10000, 10, 5)

#Program 5
def areaofcircle(r):
    area = 3.14*r*r
    print(f"Area of circle: {area}")
    
areaofcircle(10)

#Program 6
def fahrenheit(c):
    f = c * 1.8
    print(f"Fahrenheit: {f}")
    
fahrenheit(20)