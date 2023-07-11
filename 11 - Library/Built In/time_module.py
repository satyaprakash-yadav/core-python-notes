import time

# print(dir(time))

# help(time)


# Time delay :-
'''
print("Hello class this python")
time.sleep(5)
print("Hey Everyone I am Mahesh")
'''

# help(time.strftime)

'''
%Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
'''

# To check current time :-
'''
timeinfo = time.strftime("%I:%M:%S %p") 
print(timeinfo)
'''

# To check current date :-
'''
dinfo = time.strftime("%d/%m/%Y %A")
print(dinfo)
'''

# Example 1 :-
'''
while True:
    timeinfo = time.strftime("%I:%M:%S %p") 
    print(timeinfo)
    time.sleep(1)
'''


