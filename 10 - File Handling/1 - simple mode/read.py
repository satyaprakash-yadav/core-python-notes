# syntax :- It take 2 arguments open('fileName with extension', 'mode')


# 1 - way :-
'''
file = open('text_file.txt','r')
data = file.read()
print(data)
file.close()

print(type(file))
'''

# 2 - way :-
'''
with open('text_file.txt', 'r') as file:
    data = file.read()          # return all file data in string format.
    print(data)
    file.close()
'''

# Example 2 :-
'''
with open('text_file.txt','r') as file:
    data = file.readline()     # It return the first line.
    print(data)
    file.close()
'''

# Example 3 :-
'''
with open('text_file.txt', 'r') as file:
    data = file.readlines()     # It return all data in list format.
    print(data)
    file.close()
'''



