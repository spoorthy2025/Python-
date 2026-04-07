name = input("Enter name: ")
birth_year = int(input("Enter year of birth: "))
current_year = 2026
age = current_year - birth_year
print("\n--- Details ---")
print("Name:", name)
print("Age:", age)

if age >= 60:
    print("Senior Citizen")
else:
    print("Not a Senior Citizen")