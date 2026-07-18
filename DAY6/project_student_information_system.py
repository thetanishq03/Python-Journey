students = {
    101:{
        "name":"Tanishq",
        "marks":90
    },
    102:{
        "name":"Raj",
        "marks":85
    }
}
while True:
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display Students")
    print("4. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        id = int(input("Student Id: "))
        name = str(input("Name: "))
        marks = int(input("Marks: "))
        students[id] = {
            "name" : name,
            "marks" : marks
        }
    elif choice == 2:
        search = int(input("Enter student id: "))
        if search in students:
            print("Name: ",students[search]["name"])
            print("Marks: ",students[search]["marks"])
        else:
            print("Student not found!")
    elif choice == 3:
        print("*List of students*")
        for id,data in students.items():
            print("Student ID:", id)
            print("Name:", data["name"])
            print("Marks:", data["marks"])
            print("----------------------")
    elif choice == 4 in students:
        print("Exiting...")
    break