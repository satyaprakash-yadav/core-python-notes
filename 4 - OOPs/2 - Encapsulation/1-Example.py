#       ------------------ Encapsulation Example -------------------

class Employee:
    # constructor
    def __init__(self):
        self.name = "Mahesh"
        self.salary = 25000
        self.project = "website api"

    def show_emp(self):
        print("Employee Name :"+str(self.name))
        print("Employee Salary :"+str(self.salary))
        print("Employee Project :"+str(self.project))

emp = Employee()    # object
#emp.show_emp()

# modify attribute & method
emp.name = "Aakash"
emp.show_emp()
