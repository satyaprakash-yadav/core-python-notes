print()
print('-------------------------------MAHESH name in Telugu " మ  హే  ష్ " -------------------------')
print()

for i in range(0,14):
    for j in range(30):
        # LETTER "MA" 
        if (j==1 and i>=6 and i<=8) or (j==3 and i>=6 and i<=8) or (j==9 and i<=8 and i>=5) or (j==6 and i>=5 and i<=8) or (i==5 and j<=2 and j>=2): 
            print("*",end=" ")
        elif (i==9 and j<=2 and j>=2) or (i==9 and j<=5 and j>=4) or (i==9 and j<=8 and j>=7) or (i==3 and j>=2 and j<=4):
            print("*",end=" ")
        elif(i==4 and j>=5 and j<=5) or (i==2 and j>=1 and j<=1) or (i==2 and j>=3 and j<=3) or (i==1 and j>=4 and j<=4) or (i==0 and j>=5 and j<=5) :        
            print("*",end=" ")
        # LETTER "MA" OVER
        
        # LETTER "HE" START   
        elif (j==11 and i<=8 and i>=6) or (j==13 and i<=8 and i>=6) or (j==16 and i<=8 and i>=5) or (j==12 and i<=5 and i>=5) or (i==6 and j>=19 and j<=19):
            print("*",end=" ")
        elif (j==12 and i<=9 and i>=9) or (i==9 and j>=14 and j<=15) or (i==4 and j>=15 and j<=20) or (i==5 and j>=18 and j<=18)or (i==5 and j>=20 and j<=20):    
            print("*",end=" ")
        elif (i==1 and j<=13 and j>=8)or(j==13 and i<=3 and i>=1)or (i==1 and j<=13 and j>=8) or (j==15 and i<=2 and i>=1):
            print("*",end=" ")
        elif(i==3 and j<=12 and j>=12) or (j==14 and i<=0 and i>=0):                               
            print("*",end=" ")
        # LETTER "HE" OVER 

        # LETTER "SH" START
        elif (j==22 and i<=8 and i>=6) or (j==24 and i<=8 and i>=6) or (j==27 and i<=10 and i>=5) or (i==9 and j<=26 and j>=25):
            print("*",end=" ")
        elif (j==23 and i<=9 and i>=9) or (j==23 and i<=5 and i>=5) or (j==23 and i<=1 and i>=1) or (j==23 and i<=3 and i>=3):
            print("*",end=" ")
        elif (i==0 and j<=28 and j>=24)or (i==2 and j<=25 and j>=24) or (i==4 and j<=25 and j>=24):
            print("*",end=" ")
        # LETTER "SH" OVER     
        else: 
            print(" ",end=" ")
    print()
