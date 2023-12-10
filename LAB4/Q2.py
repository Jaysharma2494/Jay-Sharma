X=int(input("enter the smaller no.:"))
Y=int(input("enter the larger no.:"))
N=int(input("enter the no.:"))
i=X+1
while  i<=Y:
  p=(i)%N
  if p==0:
    print(i)
  i=i+1
else:
  print("Enter the valid number" )
    
