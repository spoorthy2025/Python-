dict1 = {'StdNo':'532','StuName': 'Naveen', 'StuAge': 21, 'StuCity': 'Hyderabad'}
print("\n Dictionary is :",dict1)
print("\n Student Name is :",dict1['StuName'])
print("\n Student City is :",dict1['StuCity'])
print("\n All Keys in Dictionary ")
for x in dict1:
    print(x)
print("\n All Values in Dictionary ")
for x in dict1:
    print(dict1[x])
dict1["Phno"]=85457854
print("\n Uadated Dictionary is :",dict1)
dict1["StuName"]="spoorthy"
print("\n Uadated Dictionary is :",dict1)
dict1.pop("StuAge")
print("\n Uadated Dictionary is :",dict1)
print("Length of Dictionary is :",len(dict1))
dict2=dict1.copy()
print("\n New Dictionary is :",dict2)
dict1.clear()
print("\n Uadated Dictionary is :",dict1)

output:

 Dictionary is : {'StdNo': '532', 'StuName': 'spoorthy', 'StuAge': 21, 'StuCity': 'Hyderabad'}

 Student Name is : spoorthy

 Student City is : Hyderabad

 All Keys in Dictionary 
StdNo
StuName
StuAge
StuCity

 All Values in Dictionary 
532
spoorthy
21
Hyderabad

 Uadated Dictionary is : {'StdNo': '532', 'StuName': 'spoorthy', 'StuAge': 21, 'StuCity': 'Hyderabad', 'Phno': 85457854}

 Uadated Dictionary is : {'StdNo': '532', 'StuName': 'spoorthy', 'StuAge': 21, 'StuCity': 'Hyderabad', 'Phno': 85457854}

 Uadated Dictionary is : {'StdNo': '532', 'StuName': 'spoorthy', 'StuCity': 'Hyderabad', 'Phno': 85457854}
Length of Dictionary is : 4

 New Dictionary is : {'StdNo': '532', 'StuName': 'spoorthy', 'StuCity': 'Hyderabad', 'Phno': 85457854}
 Uadated Dictionary is : {}
