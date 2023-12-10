x=str(input("enter the sentance:"))
y=x.split()
print("orginal",x)
L=len(y)

for i in range(-1,(-L-1),-1):
    print(y[i],end=" ")
