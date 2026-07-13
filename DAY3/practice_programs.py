#PRACTICE PROBLEMS

#PROBLEM 1
name = input("Enter your name: ")
print(f"Original: {name}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"Length: {len(name)}")

#PROBLEM 2
sentence = input("Enter a sentence: ")
print(f"Number of 'a's: {sentence.count('a') + sentence.count('A')}")

#PROBLEM 3
name = input("Enter your name: ")
print(f"Is 'n' in {name}? - {'n' in name}")

#PROBLEM 4
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

#PROBLEM 5
city = input("Enter your city: ")
print(f"First Character: {city[0]}")
print(f"Last Character: {city[-1]}")
print(f"Length: {len(city)}")
