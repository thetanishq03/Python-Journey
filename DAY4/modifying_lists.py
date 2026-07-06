#MODIFYING LISTS
sports = ["Football", "Cricket", "Table Tennis", "Badminton"]
#CHANGING ELEMENTS
sports[1] = "Basketball"
print(sports)

#ADDING ELEMENT
sports = ["Football", "Cricket"]
#append()
sports.append("Table Tennis")
print(sports)
#insert()
sports.insert(1, "Basketball")
print(sports)

#REMOVING ELEMENT
sports = ["Football", "Cricket", "Badminton"]
# remove()
sports.remove("Cricket")
print(sports)
#pop()
sports.pop()
print(sports)