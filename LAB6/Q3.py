n=int(input("enter the no. of terms:"))
i=1
total=0
while i<=n:
    total+=(1/2)**i
    i+=1
print(f"the sum of the series of {n} terms is:{total}")


n=int(input())
x=int(input())
fact=1
sum=1
i=0
for i in range(n):
    fact=fact*(2*n+1)
    a=((-1)**n)*((x)(2*n+1))/(fact)
    sum=sum+a
print(sum)


n=int(input())
x=int(input())
fact=1
sum=0
i=1
for i in range(n):
    fact=fact*(2*n-2)
    a=(-1)*(n-1)*((x)(2*n-2)/(fact))
    sum=sum+a
print(sum)
