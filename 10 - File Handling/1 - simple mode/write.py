# Example 1 :-
'''
with open('text_file1.txt','w') as file:
    data = input("Enter Your Data :")
    file.write(data)
    file.close()
'''
import os

# print(os.getcwd())

# os.chdir(r'C:\Users\Public\Downloads\Practice')
# print(os.getcwd())


# Example 2 :-
# create file in specific path :-
r'''
with open(r'\Users\Public\Downloads\Practice\test.txt','w') as file:
    data = input('Enter Your Data :')
    file.write(data)
'''


