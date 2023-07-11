import main_module

# print(dir(main_module))

# help(main_module)


print('\n---------------------- Simple Calculator -----------------------\n')

while True:
    print("1 - Addition")
    print("2 - Substraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Exit")
    print()

    try:
        ch = int(input("Enter Your Choice :"))
        print()

        if(ch == 1):
            a = int(input("Enter Your Number :"))
            b = int(input("Enter Your Number :"))
            c = main_module.addition(a, b)
            print(str(a)+" + "+str(b)+" = "+str(c))
            print()

        elif(ch == 2):
            a = int(input("Enter Your Number :"))
            b = int(input("Enter Your Number :"))
            c = main_module.substraction(a, b)
            print(str(a)+" - "+str(b)+" = "+str(c))
            print()

        elif(ch == 3):
            a = int(input("Enter Your Number :"))
            b = int(input("Enter Your Number :"))
            c = main_module.multiplication(a, b)
            print(str(a)+" * "+str(b)+" = "+str(c))
            print()

        elif(ch == 4):
            a = int(input("Enter Your Number :"))
            b = int(input("Enter Your Number :"))
            c = main_module.division(a, b)
            print(str(a)+" / "+str(b)+" = "+str(c))
            print()

        elif(ch == 5):
            print("\n-------------- Thank You ----------------\n")
            break

        else:
            print("\n-------------- Invalid Input ------------------ \n")

    except:
        print("\n <str class> <float class> invalid input try again... \n")






