while True:
    print("*MENU*\n1.Add note\n2.View notes\n3.Exit")
    choice = int(input("Enter you choice: "))
    if choice == 1:
        note = input("Enter note: ")
        with open("notes.txt", "r") as file:
            lines = file.readlines()
            serial = len(lines) + 1
        with open("notes.txt", "a") as file:
            file.write(f"{serial}.{note}\n")
    elif choice == 2:
        with open("notes.txt", "r") as file:
            # for note in notes:
            data = file.read()
        print(f"*NOTES*\n{data}")
    elif choice == 3:
        print("Exiting..")
        break

    