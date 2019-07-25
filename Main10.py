# File IO - Writing Data

file = open("Sudhir.txt","w")
print("File Mode Is : ",file.mode)
print("File Name Is : ",file.name)
print("5 line Are Write A Text : ")
for i in range(0,5):
    data=input()
    file.write(data)
file.close()
