
def diamond(n):
    '''
    '''
    for row in range(n-1):
        for col in range(n,row, -1):
            print(" ", end= " ")

        for col1 in range(row+1):
            print("*", end=" ")

        for col2 in range(row):
            print("*", end=" ")

        print()

    for row in range(n):
        for col in range(row+1):
            print(" ", end=" ")

        for col1 in range(n, row+1 , -1):
            print("*", end=" ")

        for col2 in range(n, row ,-1):
            print("*", end=" ")

        print()



def right_angle(n):
    for row in range(n):
        for col in range(row+1):
            print("*", end=" ")
        print()








