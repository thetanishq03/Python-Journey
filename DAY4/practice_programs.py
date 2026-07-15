#PROBLEM 1
sports = ["Football", "Cricket", "Table Tennis", "Badminton"]
print(f"First sport: {sports[0]}")
print(f"Last sport: {sports[-1]}")
print(f"Total number of sports: {len(sports)}")

#PROBLEM 2
user_sport = input("Enter your favourite sport: ")
sports.append(user_sport)
print(sports)

#PROBLEM 3
search_sport = input("Enter sport to search: ")
if search_sport in sports:
    print("Sport found")
else:
    print("Sport not found")

#PROBLEM 4
remove_sport = input("Enter sport to remove: ")
sports.remove(remove_sport)
print(sports)