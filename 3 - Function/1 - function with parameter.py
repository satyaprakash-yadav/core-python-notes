# ----------------------------------------- FUNCTION WITH PARAMETER ---------------------------------------------

# Example - 1 :-
'''
def addition(num_1 , num_2):
    print("Addition is : "+str(num_1 + num_2)) # Single line argumnet  

a = int(input('Enter Your Number : '))
b = int(input('Enter Your Number : '))

#addition(a,b)
'''
'''
# Example 2 :-

# Month Name Function :-

def monthnum(val):
    if val in ["1" , "01"]:
        return "Your Month Name is : "+"January"

    elif val in ['2','02']:
        return "Your Month Name is : "+'February'

    elif val in ['3','03']:
        return "Your Month Name is : "+'March'

    elif val in ['4','04']:
        return "Your Month Name is : "+'April'

    elif val in ['5','05']:
        return "Your Month Name is : "+'May'

    elif val in ['6','06']:
        return "Your Month Name is : "+'June'

    elif val in ['7','07']:
        return "Your Month Name is : "+'July'

    elif val in ['8','08']:
        return "Your Month Name is : "+'August'

    elif val in ['9','09']:
        return "Your Month Name is : "+'September'

    elif val in ['10']:
        return "Your Month Name is : "+'October'

    elif val in ['11']:
        return "Your Month Name is : "+'November'

    elif val in ['12']:
        return "Your Month Name is : "+'December'
    
    else:
        return "Invalid Input"

n = input("Enter Your Month Number :")
print(monthnum(n))
'''
'''
print('\n\t\t\t----------------- Percantage Application -----------------\n')
while True:
    print('\n\t1 - Percentage\n\t2 - Pattern\n\t3 - Exit\n')            

    ch = input('Enter Your Number : ')
    
    def per(obt , tot):
        res = obt / tot * 100
        return "Total Percentage is : "+str(round(res,2))+"%"


    if ch == "1":
        obt = int(input('Enter Your Obtain Marks : '))
        tot = int(input('Enter Your Total Marks : '))
        ans = per(obt , tot)
        print(ans)

    elif ch == "2":
        n = int(input('Enter Number Of Rows :'))
        for row in range(n):
            for col in range(row+1):
                print("*",end = " ")
            print()

    
    elif ch == "3":
        print('\n-------- Thank You --------\n')
        break

    else:
        print('Invalid Input')
'''





























