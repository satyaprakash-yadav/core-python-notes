# Example 1 :-
import random
import time
'''
class LargeError(Exception):
    pass

class SmallError(Exception):
    pass

while True:
    dice = random.randint(1, 6)
    print(dice)

    n = int(input('Enter Your Dice Number :'))

    try:
        if n > dice:
            raise LargeError

        elif n < dice:
            raise SmallError

        else:
            print('Correct Guess!')
            break

    except LargeError:
        print(f'LargeError : Guess Number {n} is Greater.')

    except SmallError:
        print(f'SmallError: Guess Number {n} is Lesser.')

    time.sleep(1)
'''

# Example 2 :-
'''
class LargeError(Exception):
    def __init__(self,msg):
        self.msg = 'LargeError :'+str(msg)

class SmallError(Exception):
    def __init__(self, msg):
        self.msg = 'SmallError :'+str(msg)

while True:
    dice = random.randint(1, 6)
    print(dice)

    n = int(input('Enter Your Dice Number :'))


    if n > dice:
        raise LargeError(f'Guess Number {n} is Greater.')

    elif n < dice:
        raise SmallError(f'Guess Number {n} is Lesser.')

    else:
        print('Correct Guess!')
        break

    time.sleep(1)
'''




