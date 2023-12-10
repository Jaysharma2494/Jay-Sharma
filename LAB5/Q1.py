N=int(input("enter the number:"))
p=1
while p<(N+1):
  i=1
  while i<=20:
    q=p*i
    print(p,"*",i,"=",q)
    i=i+1
  p+=1
