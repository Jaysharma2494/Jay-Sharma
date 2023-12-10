#1
def n(k):
    p=l[0:k]
    for i in l[0:4]:
        if i<4:
            l.remove(i)
    q=l+p
    print(q)
l=[0,1,2,3,4,5,6,7,8,9]
k=int(input("enter the number of terms that shifted b/w 0 to 9:"))
n(k)
print("*********************************************")
#2
def n():
    p=l[0:4]
    for i in l[0:4]:
        if i<4:
            l.remove(i)
    q=l+p
    print(q)
    r=p+l
    print(r)
l=[0,1,2,3,4,5,6,7,8,9]
n()
