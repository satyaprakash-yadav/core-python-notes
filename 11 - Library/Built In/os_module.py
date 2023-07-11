import os

# print(dir(os))

# help(os)


# create folder (use mkdir) :-
'''
f1 = os.mkdir("Mahesh")
print(f1)
'''

# rename folder (use rename) :-
'''
r1 = os.rename("Mahesh","Rahul")
print(r1)
'''

# delete folder (use rmdir) :-
'''
rmdir1 = os.rmdir("Rahul")
print(rmdir1)
'''

# Get current working dir (use getcwd) :-
'''
cwd = os.getcwd()
print(cwd)
'''

# change cwd :- (use chdir) :-
'''
ch = os.chdir(r"C:\Users\Public\Downloads")
# print(ch)
print(os.getcwd())
'''
