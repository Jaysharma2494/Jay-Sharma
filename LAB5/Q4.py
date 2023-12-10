
N=int(input("Enter the positive no."))
p=1
count=0
count_1=0
while N!=-999 and p!=-999:
    p=int(input("enter the positive number:"))
    q=p%N
    if q==0:
        count=count+1
    else:
        count_1=count_1+1
print("no of divisible no.:",count)
print("no of non-divisible no.:",count_1)
