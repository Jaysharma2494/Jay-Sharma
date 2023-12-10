N=int(input('enter the no. of lines:'))
i=1
while i<=N:
  p=N 
  while p>i and p<=N:
    print("",end=" ")
    p=p-1
  k=1
  while k<=i :
    print("*",end=" ")
    k=k+1
  i=i+1
  print()
