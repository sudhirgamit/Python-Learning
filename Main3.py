# List

Subject=["OS","CN","SM","MC","JWT","C","C++"]
print("Subject List : ",Subject)

print("Subject One : ",Subject[2])

print("Subject Two To Six : ",Subject[2:6])

print("Reverse Subject Is : ",Subject[::-1])

Subject.append("JAVA")

print("Append The Subject : ",Subject)

Subject[3]="PHP"

print("Update The Subject : ",Subject)

Subject.insert(3,"CSS")

print("Insert The Subject To Position : ",Subject)

Syllebus=["Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6"]

print("Merge List : ",Subject+Syllebus)

print("Length Of List : ",len(Subject))

print("Max Of List : ",max(Subject))

print("Min Of List : ",min(Subject))

Subject.remove("SM")

print("Remove Subject In List : ",Subject)

Subject.sort()

print("Sort Order In List : ",Subject)

A = Subject.copy()

print("Copy In List : ",A)

Subject.clear()

print("Clear In List : ",Subject)

list1 = "Sudhir Gamit".split()
print("String Make Into List : ",list1)

list1 = ["Sudhir","Gamit"]
print("List Make Into String : ",','.join(list1))