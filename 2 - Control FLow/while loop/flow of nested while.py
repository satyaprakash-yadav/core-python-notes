# Number of Pattern : 3



# Enter Number of rows : 7




# Enter Number of rows : 10




# Enter Number of rows : 15

'''
ch = int(input("Enter Number of Pattern :"))

for i in range(ch):
    n = int(input("Enter Number of Rows : "))
    for row in range(n):
        for col in range(n-1 , row-1 , -1):
            print(" "  , end = " ")

        for col in range(row+1):
            print("*" , end = " ")

        for col in range(row):
            print("*", end = " ")
        print()

# Flow of Nested While :-

i = 1
j = 1
while (i <= 5):
    while(j <= 5):
        print(i , j)
        j += 1
    i += 1
    print()
'''







































