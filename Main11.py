# File IO - Reading Data

file = open("Sudhir.txt","r")
data = file.read()
for i in data:
    print(i,end=" ")