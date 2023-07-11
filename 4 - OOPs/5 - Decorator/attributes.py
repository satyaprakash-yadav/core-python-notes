# There are 3 types of variables :-
# 1). class attribute :- Defined directly inside a class & shared across all objects.
# 2). instance attribute :- Defined inside constructor using self parameter , specific objects.
# 3). static attribute :- same object but different behaviour

'''
class Company:
    dept = "Sales"  # class  / static attribute

    def __init__(self, name, age, salary):  # Instance attribute
        self.name = name
        self.age = age
        self.salary = salary


emp1 = Company("Rahul", 23, 30000)
emp2 = Company("Ashish", 22, 25000)
emp3 = Company("Kaushik", 21, 20000)

# print(f"Name is : {emp1.name} salary is : {emp1.salary} department is : {emp1.dept}")
# print(f"Name is : {emp2.name} salary is : {emp2.salary} department is : {emp2.dept}")
# print(f"Name is : {emp3.name} salary is : {emp3.salary} department is : {emp3.dept}")

# particular emp dapt chnge :-
# emp3.dept = "IT"

# print(f"Name is : {emp1.name} salary is : {emp1.salary} department is : {emp1.dept}")
# print(f"Name is : {emp2.name} salary is : {emp2.salary} department is : {emp2.dept}")
# print(f"Name is : {emp3.name} salary is : {emp3.salary} department is : {emp3.dept}")

# all dept chnge
# Company.dept = "IT"
# print(f"Name is : {emp1.name} salary is : {emp1.salary} department is : {emp1.dept}")
# print(f"Name is : {emp2.name} salary is : {emp2.salary} department is : {emp2.dept}")
# print(f"Name is : {emp3.name} salary is : {emp3.salary} department is : {emp3.dept}")
'''







