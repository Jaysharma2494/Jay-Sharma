s=str(input("enter the sentnce:"))
t=' '
for i in s:
    if i not in t:
        t=t+i
print(t)
