name = input("Enter name: ")
reg_no = input("Enter reg no: ")
day = input("Enter birth day: ")
month = input("Enter birth month: ")
year = input("Enter birth year: ")
dept = input("Enter department: ")

m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
m4 = int(input("Enter marks for subject 4: "))
m5 = int(input("Enter marks for subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n--- Student Details ---")
print("Name:", name)
print("Reg No:", reg_no)
print("Department:", dept)
print("DOB:", day, "/", month, "/", year)
print("Total marks:", total)
print("Percentage:", percentage)