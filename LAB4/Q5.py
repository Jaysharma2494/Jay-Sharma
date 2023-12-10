n=int(input("enter the number:"))
i=1
fact=1
while i<=n and n>1:
  fact=fact*i
  i=i+1
print(fact)
if n==0:
  print(1)
elif n<0:
  print("enter the valid nnumber")
