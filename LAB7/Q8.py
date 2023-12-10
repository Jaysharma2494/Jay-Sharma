x=str(input("enter the sentance:"))
word=str(input("enter the words:"))
y=x.split()
p=len(y)
print(p)
count=0
print(y[1])
if word in x:
    # x=x.count(x)
    print("present")
else:
    print("not present")
for i in range(0,p,1):
    if word==y[i]:
        count=count+1
print(count)
