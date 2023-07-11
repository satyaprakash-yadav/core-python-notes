# Regular Expression == validation, scripting

# regular expression is used to match search pattern and perform operation as per method.
# re module used to express the data.
import re

# 1). findall() :- It search the pattern and return match data in the list form also, it takes two parameter (search pattern, data pattern)
# 2). match() :- It search the string pattern and return match object if does not match return None.
# 3). search() :- It is similar to match method it search all pattern if not available return None.
# 4). sub() :- It is used to replace search data and match data.

# Meta Characters :-
# 1). [] - set
# 2). \ - escape
# 3). . - any character
# 4). * - zero or more occurence
# 5). + - one or more occurence
# 6). ^ - start with
# 7). $ - end with
# 8). ? - zero or one occurence
# 9). {} - no. of occurence
# 10). | - or
'''
# 1). [] - set :-
data = "hello class this is pythonz"
p = "[a-i]"
x = re.findall(p, data)
print(x)

# Example 2 :-
data = "hello class 45"
p = "[0-9]"
x = re.findall(p, data)
print(x)

# Example 3 :-
data = "My Name Is Mahesh"
p = "[A-Z]"
x = re.findall(p, data)
print(x)


# 2). \ - escape :-
data = "google$com yahoo.in python.org"
p = "[a-z]\.[a-z]"
x = re.findall(p, data)
print(x)


# 3). . - any character :-
data = "hello class me mahesh"
p = "ma...h"
x = re.findall(p, data)
print(x)


# 4). * - zero or more occurence :-
data = "hello class this is pyython"
p = "h*"
x = re.findall(p, data)
print(x)


# 5). + - one or more occurence :-
data = "today is riday"
p = "f+"
x = re.findall(p, data)
print(x)


# 6). ^ - start with :-
data = "hello class"
p = "^h...o"
x = re.findall(p, data)
print(x)


# 7). $ - end with :-
data = "knownledge is powerful weapon the world"
p = ".*d$"
x = re.findall(p, data)
print(x)


# 8). ? - zero or one occurence :-
data = "pip"
p = "p.?p"
x = re.findall(p, data)
print(x)


# 9). {} - no. of occurence :-
data = "hello world this is python"
p = "p.{4}n"
x = re.findall(p, data)
print(x)

# 10). | - or :-
data = "mahi satya ashi rakesh"
p = "mahi|rakesh"
x = re.findall(p, data)
print(x)
'''

# Special Sequence :-
# 1). \n - new line
# 2). \t - tab space 
# 3). \A - start with string
# 4). \b - start and end with word
# 5). \d - only digit
# 6). \D - except digit
# 7). \w - a-z A-Z 0-9 _
# 8). \W - except \w
'''
# 3). \A - start with string :-
data = "a hello class this is mahi"
p = r"\Aa"
x = re.findall(p, data)
print(x)


# 4). \b - start and end with word :-
data = "write a one python example"
p = r"\be.*e\b"
x = re.findall(p, data)
print(x)


# 5). \d - only digit :-
data = "python developed in 1990"
p = r"\d"
x = re.findall(p, data)
print(x)

# 6). \D - except digit
data = "python developed in 1990"
p = r"\D"
x = re.findall(p, data)
print(x)


# 7). \w - a-z A-Z 0-9 _ :-
data = "since copyright (C) in 1991_1995 #$@%$!$#"
p = r"\w"
x = re.findall(p, data)
print(x)


# 8). \W - except \w :-
data = "since copyright (C) in 1991_1995 #$@%$!$#"
p = r"\W"
x = re.findall(p, data)
print(x)
'''

# Regex Methods :-

'''
# 2). match() :-
data = "a hello class"
p = r"h.{3}o\b"
x = re.match(p, data)
print(x)


# 3). search() :-
data = "a hello class"
p = r"h.{3}o\b"
x = re.search(p, data)
print(x)


# 4). sub() :-
data = "today is my last day in COLLege 45 91 batchs"
p = r"C.*L"
x = re.sub(p, '', data)
print(x)
'''


























