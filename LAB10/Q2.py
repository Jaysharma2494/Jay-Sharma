import random
N=int(input("Enter number of timees dice has to be rolled greater than 10,000:  "))
list=[]
frequency1,frequency2,frequency3,frequency4,frequency5,frequency6=0,0,0,0,0,0
for roll in range(N):
    face=random.randrange(1,7)
    list.append(face)
    if face==1:
        frequency1+=1
    elif face==2:
        frequency2+=1
    elif face==3:
        frequency3+=1
    elif face==4:
        frequency4+=1
    elif face==5:
        frequency5+=1
    elif face==6:
        frequency6+=1
    else:
        pass
print(list)
print("frequeny of 1 is: ",frequency1)
print("frequeny of 2 is: ",frequency2)
print("frequeny of 3 is: ",frequency3)
print("frequeny of 4 is: ",frequency4)
print("frequeny of 5 is: ",frequency5)
print("frequeny of 6 is: ",frequency6)
print(frequency1,frequency2,frequency3,frequency4,frequency5,frequency6)
