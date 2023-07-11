#
for i in range(6):
    for j in range(6):
        if (i==0) or (i==5)or(j==0)or(j==5):
         print("*",end=" ")
        else:
         print(" ",end=" ")
    print()
print()

#
for i in range(6):
    for j in range(6):
        if (j==0)or (i==5) or (i==j):
         print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

#
for i in range(6):
    for j in range(6):
        if (j==5) or (i==5)or(j+i==5):
         print("*",end=" ")
        else:
         print(" ",end=" ")
    print()
print()

#
for i in range(6):
    for j in range(6):
        if (j==0) or (i==0)or(j+i==5):
         print("*",end=" ")
        else:
         print(" ",end=" ")
    print()

#
for i in range(6):
    for j in range(6):
        if (j==5) or (i==0)or(j==i):
         print("*",end=" ")
        else:
         print(" ",end=" ")
    print()

#
for i in range(9):
    for j in range(9):
        if (i+j==4) or (j-i==4)or(i-j==4)or (i+j==12): 
            print("*",end=" ")
        elif(i==4) and (j<=6) and (j>=2):
            print("*",end=" ")
        elif(j==4) and (i<=6) and (i>=2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#
for i in range(7):
    for j in range(7):

        if (i==0) or (i==6) or (j==0) or (j==6):
            print("*",end=" ")
            
        elif (i==3) and (j >= 2 and j <= 4): 
            print("*",end=" ")
        
        elif (j==3) and (i >= 2 and i <= 4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# --------------------------------LETTER "A"--------------------------

for i in range(7):
    for j in range(5):
        if (i+j==2 or j-i==2) and i<3:
            print("*",end=" ")
        elif(j==0 and i>=2) or (j==4 and i>=2) or i==4:                
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# -----------------------------------LETTER "B"------------------------------
for i in range(7):
    for j in range(5):
        if j==0 or (i==0 and j<=3) or (i==6 and j<=3) or (i==3 and j<=3):
           print("*",end=" ")
        elif (j==4 and i<=2 and i>=1) or (j==4 and i<=5 and i>=4):   
           print("*",end=" ")
        else:
           print(" ",end=" ")
    print()

# -----------------------------------LETTER "C"-----------------------------------
for i in range(6):
    for j in range(5):
        if (i==0 and j<=3 and j>=1) or (i==5 and j<=3 and j>=1 ):
           print("*",end=" ")
        elif (j==0 and i<=4 and i>=1) or (j==4 and i<=1 and i>=1) or (j==4 and i<=4 and i>=4):   
           print("*",end=" ")
        else:
           print(" ",end=" ")
    print()

# ---------------------------------------LETTER  "D"----------------------------------

for i in range(6):
    for j in range(5):
        if j==0 or (i==0 and j<=3) or (i==5 and j<=3):
            print("*",end=" ")
        elif (j==4 and i<=4 and i>=1):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# -----------------------------------LETTER "E"---------------------------
for i in range(7):
    for j in range(5):
        if j==0 or i==6 or i==0 or i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# -------------------------------------LETTER "F"-----------------------------
for i in range(7):
    for j in range(5):
        if j==0 or i==0 or (i==3 and j<=3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# ---------------------------------------LETTER "G"-----------------------------
for i in range(6):
    for j in range(5):
        if (i==3 and j>=2) or (i==0 and j<=3 and j>=1) or (i==5 and j<=3 and j>=1):
            print("*",end=" ")
        elif (j==0 and i<=4 and i>=1) or (j==4 and i<=1 and i>=1) or (j==4 and  i<=4 and i>=4):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# -------------------------------LETTER  "H"---------------------------------
for i in range(7):
    for j in range(6):
        if j==0 or j==5 or i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# -------------------------------------------LETTER "I"----------------------------
for i in range(6):
    for j in range(5):
        if i==0 or i==5 or j==2:    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# -------------------------------------------LETTER "K"------------------------------
for i in range(7):
    for j in range(5):
        if j==0 or i+j==4 or i-j==2 or (i==3 and j<=1 and j>=1):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# -----------------------------------------------LETTER "L"----------------------------
for i in range(6):
    for j in range(5):
        if j==0 or i==5:    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

        
# --------------------------LETTER " M"----------------------------

for i in range(7):
    for j in range(7):
        if j==0 or j==6:
            print("*",end=" ")
        
        elif (i==j) and i<4:
            print("*",end=" ")
        
        elif (i+j==6) and (i<4): 
            print("*",end=" ")
        
        else:
            print(" ",end=" ")
    print()

# -----------------------------------------LETTER "N"----------------------
for i in range(6):
    for j in range(6):
        if j==0 or j==5 or i==j:    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# --------------------------------------------LETTER "O"-------------------------
for i in range(6):
    for j in range(5):
        if (i==0 and j<=3 and j>=1) or (i==5 and j<=3 and j>=1):    
            print("*",end=" ")
        elif(j==0 and i<=4 and i>=1) or (j==4 and i<=4 and i>=1):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# --------------------------------------------LETTER "P"-------------------------
for i in range(7):
    for j in range(5):
        if (j==0 ) or (i==0 and j<=3 and j>=1) or (i==3 and j<=3 and j>=1):    
            print("*",end=" ")
        elif(j==4 and i<=2 and i>=1):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# --------------------------------------------LETTER "Q"-------------------------
for i in range(7):
    for j in range(5):
        if (i==0 and j<=3 and j>=1) or (i==5 and j<=3 and j>=1):    
            print("*",end=" ")
        elif(j==0 and i<=4 and i>=1) or (j==4 and i<=4 and i>=1):    
            print("*",end=" ")
        elif(i==6 and j>=2):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# ------------------------------------LETTER "R"----------------------------
for i in range(7):
    for j in range(5):
        if (j==0 ) or (i==0 and j<=3 and j>=1) or (i==3 and j<=3 and j>=1):    
            print("*",end=" ")
        elif(j==4 and i<=2 and i>=1) or (i-j==2):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# ------------------------------------LETTER "S"----------------------------
for i in range(7):
    for j in range(5):
        if (i==0 and j<=3 and j>=1) or (i==3 and j<=3 and j>=1) or (i==6 and j<=3 and j>=1):
            print("*",end=" ")
        elif (j==0 and i<=2 and i>=1) or (j==0 and i>=5 and i<=5):    
            print("*",end=" ")
        elif(j==4 and i>=1 and i<=1) or (j==4 and i<=5 and i>=4):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


# ------------------------------------LETTER "T"----------------------------
for i in range(6):
    for j in range(7):
        if (i==0) or j==3:        
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# ------------------------------------LETTER "U"----------------------------
for i in range(6):
    for j in range(5):
        if (j==0 and i<=4) or (j==4 and i<=4):        
            print("*",end=" ")
        elif(i==5 and j<=3 and j>=1):     
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    
# ------------------------------------LETTER "V"----------------------------
for i in range(6):
    for j in range(5):
        if (j==0 and i<=3) or (j==4 and i<=3):        
            print("*",end=" ")
        elif(i==4 and j<=1 and j>=1) or (i==4 and j<=3 and j>=3) or (i==5 and j<=2 and j>=2):     
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# ------------------------------------LETTER "W"----------------------------
for i in range(6):
    for j in range(7):
        if (j==0) or (j==6):        
            print("*",end=" ")
        elif(i>=2 and i+j==5) or (i>=2 and j-i==1) :     
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# ------------------------------------LETTER "X"----------------------------
for i in range(7):
    for j in range(7):
        if (i==j) or (j+i==6):        
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
# ------------------------------------LETTER "Y"----------------------------

for i in range(7):
    for j in range(7):
        if (i==j and i<=3) or (i<=3 and j+i==6) or (j==3 and i>=3) :        
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
print()
# ------------------------------------LETTER "Z"----------------------------

for i in range(6):
    for j in range(6):
        if (i==0 or i==5) or i+j==5:        
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
