#LOOPING THROUGH LISTS
sports = ["Football", "Cricket", "Table Tennis"]
for sport in sports:
    print(sport)
#USING INDEXES
for i in range(len(sports)):
    print(i, sports[i])

#MEMBERSHIP OPERATOR
sports = ["Football", "Cricket", "Table Tennis"]
print("Football" in sports)
print("Badminton" in sports)