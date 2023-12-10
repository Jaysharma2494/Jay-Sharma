N=int(input("enter the number of terms:"))
a=1
b=1
print(a,b,end=" ")
i=0
while i<(N-2):
  c=a+b
  print(c,end=" ")
  a=b
  b=c
  i=i+1
