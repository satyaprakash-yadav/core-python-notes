#                               STRING

# 1). string is a texture type data and document type data.
# 2). string is a iterable data type and immutable data type.
# 3). string is a index positioning system.
# 4). string denoted by "" or '' and <class str>.

#  There are 3 types to define string :-
# 1). Multiline string or doc string(''') :-
# 2). Raw string(r" ") :-
# 3). String Formatting :-


# Example 1 :-
'''
name = "mahesh"
course = "python"

print("Name is :", name ,"and course is :",course)
print("Name is : "+ name +" and course is : "+str(course))
'''

# 1). string format :-
# 2). f string :-
# 3). mode string :-


# 1). string format :-
'''
shopping = "fridge"
price = 25000

print("Shopping is : {} and price is : {}".format(shopping, price))
print("Shopping is : {1} and price is : {0}".format(price, shopping))

# 2). f string :-
name = "java"
age = 30

print(f"Name is : {name} and age is : {age}")

# 3). mode string(%) :-
month = "January"
days = 31

print("Month name is : %s and days is : %d" %(month, days))


# Escape sequence or special sequence :-

st = r"Hello class this is \"Python\" Lecture"
st = "Hello class this is 'Python' Lecture"
print(st)

# 1). \n :- new line
# 2). \t :- tab space

print("1 - Addition \n2 - Substraction \n3 - Multiplication \n4 - Division")
print("1 -\t Addition \n2 -\t Substraction \n3 -\t Multiplication \n4 -\t Division")
'''

# string method :-

# 1). upper() :-
# 2). lower() :-
# 3). capitalize() :-
# 4). center() :-
# 5). strip() :-
# 6). split() :-
# 7). join() :-
# 8). isdigit() :-
# 9). isupper() :-
# 10). islower() :-

# 1). upper() :-

'''   
st = "hello class this is mahesh garu"
s = st.upper()
print(s)

# 2). lower() :-
st = "HELLO CLASS THIS IS MAHESH GARU"
s = st.lower()
print(s)

# 3). capitalize() :-
st = "mahesh raju gumpula"
s = st.capitalize()
print(s)

# 4). center() :-
st = "Hello class"
s = st.center(50)
print(s)

# 5). strip() :-
st = "                   Hello class            "
s = st.strip()
print(s)

# 6). split() :-
st = "hello class this, is mahesh"
s = st.split(",")
print(s)

# 7). join() :-
st = ['hello', 'class', 'this', 'is', 'mahesh']
s = " ".join(st)
print(s)

# 8). isdigit() :-
st = "10"
# It return boolean data and string contain only digit.
s = st.isdigit()
print(s)

if s:
    print("String contain only digit data.")

else:
    print("Mix data")

# 9). isupper() :-
st = "HELLO CLASS"
s = st.isupper()
print(s)

if s:
    print("String contain only uppercase data.")

else:
    print("Mix data")

# 10). islower() :-
st = "hello class"
s = st.islower()
print(s)

if s:
    print("String contain only lowercase data.")

else:
    print("Mix data")
'''

# 1). positive index(normal index) :-
# position by default start from 0.
# counting start from left to right.
# e.g hello class      (fourth position)
#     0    4

# 2). negative index(reverse index) :-
# position start from 0.
# counting start from right to left.
# e.g hello class  (fourth position)
#        -7    -1


# 1). positive index(normal index) :-
# syntax :- str_obj[position]
''' 
st = "hello class"
s = st[6]
print(s)

# 2). negative index(reverse index) :-
st = "hello class"
s = st[-5]
print(s)

# Access sequence inside from string or slicing :-
st = "hello class this is mahesh"
s = st[:11]        # start to mid
print(s)

s1 = st[-14:-10]   # mid
print(s1)

s2 = st[-14:]       # end to mid
print(s2)
'''
