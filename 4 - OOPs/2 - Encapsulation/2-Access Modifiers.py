# Access Modifiers :-
'''
1 - public/local :-
2 - protected(_) :-
3 - private(__)  :-
'''
'''
class info:
    # constructor
    def __init__(self):
        self.name = "Rohit"     # public/local
        self._age = 23          # protected
        self.__loc = "thane"    # private

    def name1(self):
        print(self.name)

    def age1(self):
        print(self._age)

    def loc1(self):
        print(self.__loc)

class B(info):

    def name2(self):
        print(self.name)

    def age2(self):
        print(self._age)

    def loc2(self):
        print(self.__loc)

obj = B()   # object

obj.name1()
obj.name2()

obj.age1()
obj.age2()

obj.loc1()
obj.loc2()
'''

class student:
    def __init__(self):
        self.__name = "Rohit"
        self._age = 23
        self._loc = "thane"
        self.qual = "BscIT"

    def get_info(self):             # getter method
        print("Student Name :"+str(self.__name))
        print("Student Age :"+str(self._age))
        print("Student Location :"+str(self._loc))
        print("Student Qualification :"+str(self.qual))

    def set_info(self, name):       # setter method
        self.__name = name          # Data Redundency


obj = student()
#obj.get_info()

# modify attribute
#obj.__name = "Raju"
#obj.get_info()

# modify with the help of set method
obj.set_info("Raju")
obj.get_info()
