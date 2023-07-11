# (w+) write+read :-

# Example 1 :-
'''
with open('new_text.txt','w+') as file:
    data = input("Enter Your Data :")
    file.write(data)

    # set position
    file.seek(2)

    # read data
    data = file.read()
    print(data)
    file.close()
'''

