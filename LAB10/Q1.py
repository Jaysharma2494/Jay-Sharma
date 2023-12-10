


p=input("enter the paragraph:")
d={}
vowels="AEIOUaeiou"
for x in p:
    if x in vowels:
        d[x]=p.count(x)
print(d)
v=d.values()
print(v)
