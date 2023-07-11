# There are 3 types of methods :-
# 1).class method
# 2). static method
# 3). instance method

'''
class A:
    dept = "IT"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        

    def info(self):     # instance method
        print("Name is :"+str(self.name))
        print("Age is :"+str(self.age))
        print("Qualification is :"+str(self.dept))
        print()

    @classmethod
    def change_dept(cls, dept): # class method
        cls.dept = dept

    @staticmethod
    def sports(name , sport): # static method
        print("Name is :"+str(name))
        print("Interested in :"+str(sport))

std1 = A("Rakesh", 23) 
std2 = A("Manish", 24)
'''
# std1.info()
# std2.info()

# A.chnge_dept("BSC")
# std1.dept = "BSC"
# std1.info()
# std2.info()

# A.sports("Manish", 'cricket')
