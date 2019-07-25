# Object Orianted Concept

class Student:
    __id = 0
    __name = ""
    __city = ""

    def __init__(self,id,name,city):
        self.__id = id
        self.__name = name
        self.__city = city

    def set_id(self,id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_city(self,city):
        self.__city = city

    def get_city(self):
        return self.__city


id = int(input("Student Id : "))
name = input("Student Name : ")
city = input("Student City : ")

S = Student(id,name,city)

# S.set_id(id)
# S.set_name(name)
#S.set_city(city)
print(S.get_id())
print(S.get_name())
print(S.get_city())