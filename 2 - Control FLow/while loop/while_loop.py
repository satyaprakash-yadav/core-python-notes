# ------------------------------------------------ WHILE LOOP --------------------------------------------


# while loop :- It runs infinite time but for loop cannot run infinite time.
# while loop works each and everytime.
#step 1: Initialization   e.g i = 1
#step 2: condition            while ( i <= 10):
#step 3: step                 i += 1

'''
# Increment order
i = 1
while (i <= 10):
    #print(i)
    i =i + 1


i = 10
while (i >= 1):
    #print(i)
    i -= 1

# Table

i = 1
#n = int(input("Enter Your Number : "))
while( i <= 10):
    #print(i*n)
    i += 1

i = 1
while (i <= 10):
    j = 2
    while ( j <= 10):
        #print(j*i , end = "\t")
        j += 1
    i += 1
    #print()


fact = 1
n = int(input("Enter Your Number : "))
while (n >= 1):
    fact = fact * n
    n = n - 1
#print(fact)


i = 1
while (i <= 10):
    print(i)

    i =i + 1

else:
    print("Program is Finish")
'''
'''
# Call Dailer (for loop):-
n = input("Enter Your Contact Number :")
for i in n:
    #print(i , end= "")


# Instragram , fb , utube , amazon (while True)
# n number of time u have to scroll down they give u new profiles the u have to follow and same time ads aslo.
'''
'''
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
'''
# Square Pattern :- 
'''
row = 0
while (row <= 5):

    col = 0
    while (col <= 5):
        print("*",end = " ")
        col += 1
    row += 1
    print()
'''
# Example 1 :-
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
'''
'''
row = 0
while (row <= 5):
    col = 0               # Data Redundency
    while(col <= row):
        print("*",end= " ")
        col += 1
    row += 1
    print()
'''
# Example 2 :-
'''
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''
'''
row = 5
while (row >= 0):
    col = 0
    while (col <= row):   # row decrement 
        print("*",end = " ")
        col += 1
    row -= 1
    print()
'''
# Example 3 :-
'''
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * * 
'''
'''
n = 5
row = 0
while (row <= n):
    col = 0
    while(col <= n - row): # col decrement
        print(" ",end= " ")
        col += 1

    col1 = 0
    while(col1 <= row):
        print("*",end = " ")
        col1 += 1

    col1 = 1
    while(col1 <= row):
        print("*",end = " ")
        col1 += 1
        
    row += 1
    print()
'''
# Hologram triangle :-
'''
        *         
      *   *       
    *       *     
  *           *   
* * * * * * * * * 
'''
'''
n = int(input("Enter Your Number : "))
row = 0
while (row < n):
    col = 0
    while (col < n*2-1):
        if (row == n-1) or (row + col == n-1) or (col - row == n-1):
            print("*",end= " ")
        else:
            print(" ",end= " ")
        col +=1
        
    row +=1
    print()

'''
# Right angle triangle :-
'''
*           
* *         
*   *       
*     *     
*       *   
* * * * * * 
'''
'''
n = int(input("Enter Your Number : "))
row = 0
while (row < n):
    col = 0
    while(col < n):
        if (row == n-1) or (col == 0) or (row == col):
            print("*",end= " ")
        else:
            print(" ",end= " ")
        col +=1
    row +=1
    print()

# holo square :-
row=0
while (row<7):
    col=0
    while(col<7):
        if(row==0 or row==6 or col==0 or col==6):
           print("*",end=" ")
        elif(col==3) and (row>=2 and row<=4):
            print("*",end=" ")
        elif(row==3) and (col>=2 and col<=4):   
            print("*",end=" ")
        else:  
           print(" ",end=" ")  
        col+=1
    row+=1
    print()
'''
'''
# simple calculator :-
print("\n---------------------- Simple Calculator -------------------------\n")
while True:
    print("1 - Addition")
    print("2 - substraction")
    print("3 - multiplication")
    print("4 - division")
    print("5 - exit")
    print()

    ch = int(input('Enter Your Choice : '))
    if ch == 1:
        a = int(input("Enter Your Number :"))
        b = int(input("Enter Your Number :"))
        print("Addition is : ",a + b,"\n")
    elif ch == 2:
        a = int(input("Enter Your Number :"))
        b = int(input("Enter Your Number :"))
        print("Substraction is : ", a - b,"\n")

    elif ch == 3:
        a = int(input("Enter Your Number :"))
        b = int(input("Enter Your Number :"))
        print("Multiplication is : ", a * b,"\n")

    elif ch == 4:
        a = int(input("Enter Your Number :"))
        b = int(input("Enter Your Number :"))
        print("Division is : ", a / b,"\n")

    elif ch == 5:
        print("--------- Thank You !!! ---------")
        break
    
    else:
        print("\n---------- Invalid Input --------\n")

'''
'''
# Number Pattern :-
row = 5
while (row >= 0):
    col = 0
    while (col <= row):   # row decrement 
        print(col,end = " ")
        col += 1
    row -= 1
    print()
'''
# Continue, Break and Pass :-
'''
# Continue
n = 0
while(n <= 10):
    if (n == 2):
        n += 1
        continue
    print(n)
    n += 1


n = 0
while(n <= 10):
    n += 1
    if (n == 2):
        continue
    print(n)
'''
'''
# break :-
n = 0
while(n <= 10):
    n += 1
    if (n == 2):
        break
    print(n)

# Pass :-
n = 0
while(n <= 10):
    pass
'''
'''
# Find Particular table number :-
n = int(input("Enter Your Number : "))
row = 1
while (row <= 10):
    print(row*n)
    row += 1
'''








