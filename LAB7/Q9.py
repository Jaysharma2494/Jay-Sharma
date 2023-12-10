x=input("please enter a hyphen separated sentence:")
b=x.split("-")
s=len(b)
for i in range(s):
    for j in range (0,s-i-1):
        if b[j] > b[j+1]:
           b[j],b[j+1]=b[j+1],b[j]   
Z="-".join(b)
print("sorted sentence",Z)
