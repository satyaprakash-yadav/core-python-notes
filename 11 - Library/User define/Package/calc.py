from calc_module import simple_calc, complex_calc, pattern_gen

# print(dir(complex_calc))

# help(complex_calc)

print('\n---------------- Calculator Application ------------------\n')

while True:
    print("1 - simple calculator")
    print("2 - complex calculator")
    print("3 - pattern generate")
    print("4 - exit")
    print()

    app_ch = int(input("Enter Your Choice :"))
    print()

    if(app_ch == 1):
        print("\n---------------- Welcome To Simple Calculator -----------------\n")
        while True:
            print("1 - Addition")
            print("2 - Substraction")
            print("3 - Multiplication")
            print("4 - Division")
            print("5 - Exit")
            print()

            ch = int(input("Enter Your Choice :"))
            print()

            if(ch == 1):
                n1 = int(input("Enter Your Number :"))
                n2 = int(input("Enter Your Number :"))
                n = simple_calc.addition(n1, n2)
                print(str(n1)+" + "+str(n2)+" = "+str(n))
                print()

            elif(ch == 2):
                n1 = int(input("Enter Your Number :"))
                n2 = int(input("Enter Your Number :"))
                n = simple_calc.substraction(n1, n2)
                print(str(n1)+" - "+str(n2)+" = "+str(n))
                print()

            elif(ch == 3):
                n1 = int(input("Enter Your Number :"))
                n2 = int(input("Enter Your Number :"))
                n = simple_calc.multiplication(n1, n2)
                print(str(n1)+" * "+str(n2)+" = "+str(n))
                print()

            elif(ch == 4):
                n1 = int(input("Enter Your Number :"))
                n2 = int(input("Enter Your Number :"))
                n = simple_calc.division(n1, n2)
                print(str(n1)+" / "+str(n2)+" = "+str(n))
                print()

            elif(ch == 5):
                print("\n------------------- Thank You -------------------\n")
                break

            else:
                print("\n--------------- Invalid Input ----------------\n")


    elif(app_ch == 2):
        print("\n-------------- Complex Calculator ---------------\n")
        print("1 - Percentage")
        print("2 - Factorial")
        print("3 - Exit")
        print()

        while True:
            ch = int(input("Enter Your Choice :"))
            print()

            if(ch == 1):
                obt = int(input("Enter Your Obtain Marks :"))
                tot = int(input("Enter Your Total Marks :"))
                res = complex_calc.percentage(obt, tot)
                print(str(obt)+" / "+str(tot)+ " * 100 = "+str(round(res,2)))
                print()

            elif(ch == 2):
                n = int(input("Enter Your Factorial Number :"))
                f = complex_calc.factorial(n)
                print("Factorial of "+str(n)+" is "+str(f))
                print()

            elif(ch == 3):
                print("\n------------------- Thank You -------------------\n")
                break

            else:
                print("\n--------------- Invalid Input ----------------\n")

    elif(app_ch == 3):
        print("\n-------------------- Welcome To Pattern Generator -------------------\n")
        print("1 - Diamond")
        print("2 - Right Angle")
        print("3 - Exit")
        print()

        while True:
            ch = int(input("Enter Your Choice :"))
            print()

            if(ch == 1):
                n = int(input("Enter Your Number :"))
                ptr = pattern_gen.diamond(n)
                # print(ptr)
                print()

            elif(ch == 2):
                n = int(input("Enter Your Number :"))
                ptr = pattern_gen.right_angle(n)
                # print(ptr)
                print()                

            elif(ch == 3):
                print("\n------------------- Thank You -------------------\n")
                break

            else:
                print("\n--------------- Invalid Input ----------------\n")

    elif(app_ch == 4):
        print("\n--------------- Thank Your For Using Application ----------------\n")
        break

    else:
        print("\n---------------- Invalid Input ---------------\n")



