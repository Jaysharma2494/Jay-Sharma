#1
n=int(input(" the length of the list:"))
l=[]
q=[]
for i in range(n):
    p=int(input("enter the element:"))
    l.append(p)
print(l)
for x in l:
    if x not in q:
        q.append(x)
print(q)

#2

n=int(input(" the length of the list:"))
l=[]
for i in range(n):
    p=int(input("enter the element:"))
    l.append(p)
print(l)
l=set(l)
l=list(l)
print(l)

