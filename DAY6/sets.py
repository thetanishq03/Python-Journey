#SETS
numbers = {1,2,3,4}

#DUPLICATE EXAMPLE
numbers = {1,2,3,3,3,4,4}
print(numbers)

#ADD
numbers.add(10)
#REMOVE
numbers.remove(2)
#MEMBERSHIP
print(5 in numbers)

#REAL-WORLD EXAMPLE
students = ["Amit", "Rahul", "Amit", "Riya", "Rahul"]
unique_students = set(students)
print(unique_students)

#PRACTICE
movies = ["Sitaramam", "Kalank", "Uri", "Dhurandar", "Kalank"]
unique_movies = set(movies)
print(unique_movies)