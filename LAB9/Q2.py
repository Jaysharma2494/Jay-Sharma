#1
n=int(input("enter the length of lists:"))
a=[]
b=[]
c=[]
for i in range(n):
    x=int(input("enter the element of a:"))
    a.append(x)
for i in range(n):
    y=int(input("enter the element of b:"))
    b.append(y)
a=set(a)
b=set(b)
print(a)
print(b)
# #2

print("union",a.union(b))
print("intersection",a.intersection(b))
print("differance",a.difference(b))
print(" symmetric set difference",a^b)
#3
for x in a:
    if x in b:
        c.append(x)
print(c)  
#4
a=list(a)
b=list(b)
c=a+b
c=set(c)
c=list(c)
print(c)
