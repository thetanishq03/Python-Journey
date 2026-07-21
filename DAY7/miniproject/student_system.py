import csv

students = {}

while True:

    print("\n====== Student Information System ======")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Save Students to CSV")
    print("7. Load Students from CSV")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # ---------------- ADD STUDENT ----------------

    if choice == 1:

        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            print("Student ID already exists!")

        else:
            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))

            students[student_id] = {
                "name": name,
                "marks": marks
            }

            print("Student Added Successfully!")

    # ---------------- SEARCH STUDENT ----------------

    elif choice == 2:

        student_id = int(input("Enter Student ID: "))

        if student_id in students:

            print("\nStudent Found")
            print("ID:", student_id)
            print("Name:", students[student_id]["name"])
            print("Marks:", students[student_id]["marks"])

        else:
            print("Student Not Found!")

    # ---------------- DISPLAY ALL ----------------

    elif choice == 3:

        if len(students) == 0:
            print("No Students Found!")

        else:

            print("\n------ Student List ------")

            for student_id, data in students.items():

                print("-----------------------")
                print("ID:", student_id)
                print("Name:", data["name"])
                print("Marks:", data["marks"])

    # ---------------- UPDATE MARKS ----------------

    elif choice == 4:

        student_id = int(input("Enter Student ID: "))

        if student_id in students:

            new_marks = int(input("Enter New Marks: "))

            students[student_id]["marks"] = new_marks

            print("Marks Updated Successfully!")

        else:
            print("Student Not Found!")

    # ---------------- DELETE ----------------

    elif choice == 5:

        student_id = int(input("Enter Student ID: "))

        if student_id in students:

            del students[student_id]

            print("Student Deleted Successfully!")

        else:
            print("Student Not Found!")

    # ---------------- SAVE CSV ----------------

    elif choice == 6:

        with open("students.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["ID", "Name", "Marks"])

            for student_id, data in students.items():

                writer.writerow([
                    student_id,
                    data["name"],
                    data["marks"]
                ])

        print("Students Saved Successfully!")

    # ---------------- LOAD CSV ----------------

    elif choice == 7:

        try:

            with open("students.csv", "r") as file:

                reader = csv.reader(file)

                next(reader)

                students.clear()

                for row in reader:

                    student_id = int(row[0])

                    students[student_id] = {
                        "name": row[1],
                        "marks": int(row[2])
                    }

            print("Students Loaded Successfully!")

        except FileNotFoundError:

            print("students.csv not found!")

    # ---------------- EXIT ----------------

    elif choice == 8:

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")