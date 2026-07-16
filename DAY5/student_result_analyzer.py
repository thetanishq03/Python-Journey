#MINIPROJECT2: STUDENT RESULT ANALYZER
def calculate_total(a,b,c):
    return a+b+c

def calculate_average(a,b,c):
    return a+b+c/3

def find_grade(a,b,c):
    total = a+b+c
    if total >= 220:
        return "A"
    elif total >= 200:
        return "B"
    else:
        return "C"
    
def display_result():
    print("**RESULT**")
    print(f"Total: {total_}")
    print(f"Average: {avg_}")
    print(f"Grade: {grade_}")

print("Enter following subjects marks for result.")
a = int(input("English: "))
b = int(input("Maths: "))
c = int(input("Science: "))
total_ = calculate_total(a,b,c)
avg_  = calculate_average(a,b,c)
grade_ = find_grade(a,b,c)
display_result()