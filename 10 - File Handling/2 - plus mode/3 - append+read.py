# (a+) append+read :-

'''
# write append :-
with open("next.txt","a+") as file:
    data = input('Enter Your Data :')
    file.write(data+'\n')

    # set position
    file.seek(2)

    # read data
    data = file.read()
    print(data)
    
'''
