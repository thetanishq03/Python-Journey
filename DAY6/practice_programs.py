#PRACTICE PROGRAMS

#PROBLEM 1
me = {
    "Name": "Tanishq",
    "Age": 18,
    "City": "Mumbai",
    "Favourite Sport": "Football"
}
for key, value in me.items():
    print(f"{key}: {value}")

#PROBLEM 2
me["Age"] = 19

#PROBLEM 3
me["Dream Company"] = "JP Morgan"

#PROBLEM 4
me.pop("City")
print(me)