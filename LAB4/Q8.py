n=int(input("enter the number:"))
i=2
if n==0 or n==1:
    print("number neither prime nor not prime")
while (i<n and n>=0):
    if n%i==0:
        print("not a prime no.")
        break
        i=i+1
    else:
        print("prime no")
        break
else:
    print("enter the valid number")