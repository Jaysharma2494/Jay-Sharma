k=int(input("enter the arbitrary length:"))
x=[]
for i in range(k):
    p=int(input("enter the element:"))
    x.append(p)
print(x)
# c=[]
for i in range(k):
    s=min(x)
    x[i].append(s)
    x.remove(s)
print(x)
