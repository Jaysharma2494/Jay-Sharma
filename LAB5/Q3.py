N=int(input("enter the number of lines:"))
i=1
while i<=N:
  p=0
  while p<i:
    print("*",end=" ")
    p=p+1
  i=i+1
  print()


i=1
while i<=N:
  k=N
  while (k>=i and k<=N) :
    print(" ",end=" ")
    k=k-1
  j=1
  while j<=i:
    print("*",end=" ")
    j=j+1
  print()
  i=i+1

i=1
while i<=N:
  k=N
  while k>i and k<=N:
    print(" ",end=" ")
    k=k-1
  p=1
  while p<=i:
    print("*",end=" ")
    p=p+1
  m=i-1
  while m>0 and m<=(i-1):
    print("*",end=" ")
    m=m-1
  i=i+1
  print()
  
