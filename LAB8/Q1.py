k=int(input("enter the arbitrary length:"))
x=[]
for i in range(k):
    p=int(input("enter the element:"))
    x.append(p)
print(x)
y=0
for i in range(k):
  y=y+x[i]
print("sum of all elements:",y)
a=1
for i in range(k):
   a=a*x[i]
print("multiple of all no. is:",a)
# x.sort
v=x[0]
for i in range(0,len(x)):
   v=x[i]
print("maximun element is:",v)
