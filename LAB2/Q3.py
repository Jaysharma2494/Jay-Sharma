x=int(input("enter the of x:"))
y=int(input("enter the of y:"))
if x<0 or y<0:
    print("invalid input") 
elif y%x==0:
    print("y is divisible by x")
    print(y,"is dividible by",x)
else:
    print("y is not divisible by x")   

