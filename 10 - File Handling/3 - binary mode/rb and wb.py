# pickling :- Its a process to convert python obj into bit format.
# unpickling :- Its a process to convert bit format to python obj or its a reverse process of pickling. 
# python by default directly not support pickling and unpickling.
# Its basically work serializer form. 
# e.g. img file open in text editor see the bit format.

import pickle

# pickling :-
with open("file.txt","wb") as file:
    d = "hello class"
    d1 = "this is"
    d2 = "python class"

    pickle.dump(d, file)
    pickle.dump(d1, file)
    pickle.dump(d2, file)

# unpickling :-

with open("file.txt","rb") as file:
    d = pickle.load(file)
    d1 = pickle.load(file)
    d2 = pickle.load(file)

print(d)
print(d1)
print(d2)

