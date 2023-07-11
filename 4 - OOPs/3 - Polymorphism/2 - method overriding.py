# Method Overriding :- 
# Example



class parent:

    def car(self):
        print("Parent car is BMW")

class child(parent):

    def car(self):
        super().car()
        print("Child car is Audi")

obj = child()
obj.car()



