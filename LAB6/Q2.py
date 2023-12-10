# 1
n=int(input("ENTER THE NO OF TERMS:"))
sum=0
i=1
while i<=n:
  sum=sum+(1/i)
  i=i+1
print(f"sum of {n} terms is:{sum:.9f}")

# 2
n=int(input("ENTER THE NO OF TERMS:"))
sum=0
fact=1
i=1
while i<=n:
  fact=fact*i
  i+=1
  sum=sum+(1/fact)
print(f"sum of {n} terms is:{sum:.9f}")

#3
n=int(input("ENTER THE NO OF TERMS:"))
x=int(input("enter the vale of x:"))
sum=0
i=1
while i<=n:
  sum=sum+(x**i)/i
  i+=1
print(f"sum of series {n} is:{sum:.9f}")