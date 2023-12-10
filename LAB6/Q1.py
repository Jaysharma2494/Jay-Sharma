name=input("enter the sentance:")
p=(len(name))
voval="AEIOUaeiou"
count=0
counts=0
x=len(voval)
for i in range(p):
  if name[i]==" ":
    counts+=1
  for k in range(x):
    if name[i]==voval[k]:
      count=count+1
print("vowals:",count)
# print(counts+1)
print("constance:",p-count-counts)
print("total words:",p-counts)
