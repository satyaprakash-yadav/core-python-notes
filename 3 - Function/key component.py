#               -------------------------------- Function ----------------------------------

#  Key Components of Function

# 1). Return Keyword :-
'''
def addition(a, b):
    add = a + b
    return add

x = addition(10, 20)
#print(x)

# Default parameter

def addition(a , b = 0):
    add = a + b
    return add
x = addition(10, 30)  # Data Redundancy (Overwrite)
# print(x)

# e.g
class main():
    def Passbook():
        pass

    def Payement():
        pass

    def send():
        pass

    def receive():
        pass

    def contact():
        pass

if __name__=="__main__":
    main(Payment(),Passbook()); # position


# Positional argument :-

def substraction(n1 , n2):
    sub = n1 - n2
    return "Substraction is : ",sub

x = substraction(n2 = 10,n1= 20)
#print(x)
'''
# Variable length argument

def sum(*args): # * - all , args - arguments(args is standard attribute)
    s = 0
    for i in args:
        s += i
    return s
    
x = sum(10, 20, 30)
#print(x)

# local & global Variable :-

n = 0
#print(n)

def sum(*args):
    #print(n)
    global n
    for i in args:
        n += i
    return n

x = sum(10 , 20 , 30)
# print(x)

# Local Variable :-

def addition(a,b):
    add = a + b

    print("Addition is :"+str(add)) # single - line argument


#addition(10 , 30)

#print(add)

# global Variable :-

def addition(a,b):
    global add
    
    add = a + b
    print("Addition is : "+str(add))

#addition(10,30)

#print(add)




# Percantage Calculator :-

print("\n\t\t--------------------------------- Percantage Application -----------------------------\n")

def percentage(obt , tot = 500):    # Default parameter 
    if obt > tot:
        obt , tot = tot , obt       
    res = obt / tot * 100
    return res


def sum_of_marks(*args):            # Variable length argument
    subject = 0
    for i in args:
        subject += i
    return subject                  # return keyword


hindi = int(input("Enter Your Hindi Marks :"))
marathi = int(input("Enter Your Marathi Marks :"))
maths = int(input("Enter Your Maths Marks :"))
science = int(input("Enter Your Science Marks :"))
history = int(input("Enter Your History Marks :"))
geography = int(input("Enter Your Geography Marks :"))
english = int(input("Enter Your English Marks :"))


allmarks = sum_of_marks(hindi , marathi , maths , science , history , geography , english) # function

per = percentage(allmarks)

print("Percentage of All Marks is : ",round(per,2),"%")
































