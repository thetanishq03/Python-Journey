#DICTIONARIES
student = {
    "name": "Tanishq",
    "age": 18,
    "city": "Mumbai"
}
#ACCESS VALUES
print(student["name"])
#UPDATE VALUES
student["age"] = 19
#REMOVE DATA
student.pop("city")
#LOOP THROUGH DICTIONARY
for key,value in student.items():
    print(key,value)
