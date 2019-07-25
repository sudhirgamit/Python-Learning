# Dictionaries

Dict = {"Id":1,"Name":"Sudhir","Age":21,"City":"Mandvi","Subject":"Python","Course":"MCA"}

print("Dictionaries To All Values : ",Dict)

print("Dictionaries To One Key Of Values : ",Dict["Name"])

print("Dictionaries To All Keys : ",Dict.keys())

print("Dictionaries To All Values : ",Dict.values())

Dict["Name"]="Rahul"

print("Dictionaries To Update Values In Name Key : ",Dict)

print("Length Of Dictionaries : ",len(Dict))

print("Max Of Dictionaries : ",max(Dict))

print("Min Of Dictionaries : ",min(Dict))

# Second Dict

data = dict(name='Sudhir',age=22,city='Surat',email='sudhir@gmail.com')
print("Second Dict : ",data)

student = {
    'Id':16,
    'Name':'Sudhir',
    'City':'Mandvi',
    'Department':'MCA',
    'Subject':['OS','MC','CN','SM','DS'],
    'Mobile':8238895676,
    'Marks':{
        'OS':56,
        'MC':76,
        'CN':67,
        'SM':45,
        'DS':89
    }
}
print(student['Mobile'])
for i in student:
    print(i," : ",student[i])


print(student.items())

