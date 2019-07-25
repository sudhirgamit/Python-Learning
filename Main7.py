# Loops

# For Loops

for i in range(0,11):
    print(i,end="")

n = int(input("Enter A Number : "))
for i in range(n):
    print(i,end="")

list1 =["Sudhir","Rahul","Amit","Vijay","Raju"]
for li in list1:
    print(li,end="")

# While Loops

list2=[]
n = int(input("Enter A Values N : "))
while(n<=10):
    name = input("Enter A List Name : ")
    list2.append(name)
    n=n+1
print("List Values : ",list2)


lnum=[[[1,2,3],[4,5,6],[7,8,9]]]
for i in lnum:
    print(i)
    for j in i:
        print(j)
        for k in j:
            print(k)
