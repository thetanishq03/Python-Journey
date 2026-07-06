#MINI PROJECT:USERNAME GENERATOR
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")
username = first_name[0] + last_name + birth_year[-2:]
print(f"Your username is: {username}")
print(f"Email: {username.lower()}@example.com")