#Practice 1
# with open("about_me.txt", "x") as file:
#     file.write("Name: Tanishq")
    
# with open("about_me.txt","a+") as file:       #"a+" can read and append too
#     file.write("\nCity: Mumbai \nLearning: Python \nGoal: Software Developer")
#     file.seek(0)      # Move pointer to the beginning
#     data = file.read()
#     print(data)

# with open("about_me.txt", "r") as file:
#     print(file.readline())

# with open("about_me.txt", "r") as file:
#     lines = file.readlines()
# print(lines)


#Filehandling + Lists
# students = ["Rahul", "Aditi", "Tanishq"]
# with open("data.txt", "w+") as file:
#     for student in students:
#         file.write(student + "\n")
#     file.seek(0)
#     data = file.read()
# print(data)