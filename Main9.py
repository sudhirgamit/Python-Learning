# Strings

Str="this is a my code"

print("All String Value : ",Str)

print("2-5 Possion Of Character : ",Str[2:5])

print("-2 Possion of Character : ",Str[-2:])

print("-3 Possion of Character : ",Str[:-3])

print("Reverse of Character : ",Str[::-1])

print("1 to -5 Possion of Character : ",Str[1:-5])

print("First Character Is Capital : ",Str.capitalize())

print("Upper Character : ",Str.upper())

print("Lower Character : ",Str.lower())

print("Length Of Character : ",len(Str))

print("Title Character : ",Str.title())

print("Replace Of Character : ",Str.replace("this","it"))

print("Count Of Character : ",Str.count(Str))

print("Smalles Of Character : ",Str.casefold())

print("End Of Character True or False : ",Str.endswith("e"))

print("Start Of Character True or False : ",Str.startswith("h"))

print("Find Of Character : ",Str.find("my"))

print("Index Number Of Character : ",Str.index("code"))

print("String Of Character True or False : ",Str.islower())

print("String Of Number True or False : ",Str.isdigit())

# Compare List

list1 = ["sudhir","amit",34,55]
list2 = ["sudhir","amit",34,55]
list3 = ["rajesh","meet",54,15]

print("== Compare List : ",list1==list3)
print("== Compare List Values : ",list1==list2)
print("Is Compare List Memory Location : ",list1 is list2)