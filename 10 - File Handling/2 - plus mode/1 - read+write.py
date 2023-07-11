# r+ :-

# Example 1 :-
'''
with open("text_file.txt","r+") as file:
    data = file.read()
    print(data)

    # set position
    file.seek(1)

    # write data
    data = 'python'
    file.write(data)

'''
# Example 2 :-
'''
with open('text_file.txt','r+') as file:
    # set position
    file.seek(1)

    # write data
    data = input("Enter Your Data :")
    file.write(data)
'''



