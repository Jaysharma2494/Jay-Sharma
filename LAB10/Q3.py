O = {}
E = {}
while 1==1:
    x= str(input('over or not? '))
    if x=='over':
        break
    else:
        n= int(input())
        s= n**2
        c=n**3

    if n%2==0:
        E[n]=[s,c]
    else:
        O[n]=[s,c] 
print(E)
print(O)
