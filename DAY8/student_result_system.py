def calculate_total(a,b,c,d,e):
    return a+b+c+d+e

def calculate_percentage(a,b,c,d,e):
    return total/500 * 100

def grade(a,b,c,d,e):
    if percentage >= 80:
        return "A Grade"
    elif percentage >= 50:
        return "B Grade"
    else:
        return "C Grade"

def display_result():
    print(f"Total Marks: {total}")
    print(f"Percentage: {percentage}%")
    print(f"Grade: {gradee}")
        
print("**STUDENT RESULT SYSTEM**")
print("5 papers 100 marks each")
a = int(input("Enter Marks For English: "))
b = int(input("Enter Marks For Math: "))
c = int(input("Enter Marks For Science: "))
d = int(input("Enter Marks For Computer: "))
e = int(input("Enter Marks For History: "))
total = calculate_total(a,b,c,d,e)
percentage = calculate_percentage(a,b,c,d,e)
gradee = grade(a,b,c,d,e)
display_result()
