# Tuples

Tu = ("Sunday","Monday","Tuesday","Wednessday","Thusday","Friday","Saturday")

print("Tuples All Values : ",Tu)

print("Tuples One Values : ",Tu[3])

print("Tuples Two To Seven Values : ",Tu[2:7])

print("Reverse Tuples Values : ",Tu[::-1])

print("Length Tuples Values : ",len(Tu))

print("Max Tuples Values : ",max(Tu))

print("Min Tuples Values : ",min(Tu))

list = list(Tu)

print("Convertion Of Tuples into List : ",list)

num1 = "Red","Blue","Green"
print("None Perentathic : ",type(num1))

num2 = "Red",
print("None Perentathic : ",type(num2))

num3,num4,num5 = num1
print(type(num3)," ",num3," ",num4," ",num5)

list4 = ("sudhir",1,["Amit","Rajesh",24])
list4[2].append("Jaini")
print(list4)

i = tuple(range(1,11))
print(i,end=" ")
