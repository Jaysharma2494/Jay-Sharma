#1
x=input("space seaparated strings:")
y=x.split()
sample_string=input("enter a sample_string:")
count=0
for i in y:
    if i==sample_string:
        count+=1
print(f"count of string that contain {sample_string} as substring",count)  

#2
n=int(input("enter a number of elements:"))
list1=[]
for i in range (n):
    element=float(input("enter the value :"))
    list1.append(element)

#Method1
list2=[]
for i in (list1):
    if i <0:
        list2.append(0)
    else:
        y=i**2
        list2.append(y)
print(list2)

#Method2
list2= [0 if i <0 else i**2 for i in list1]
print(list2)
#3
n=int(input("enter a number of elements:"))
list1=[]
for i in range (n):
    element=float(input("enter the value :"))
    list1.append(element)
list2=[]
for i in list1:
    if i >10 and i <=20:
        y=i**2
        list2.append(y)
    else:
        list2.append(i)
print(list2) 

#4
x=input("space seaparated strings:")
y=x.split()
list2=[]
for i in y:
    if not i [0].istitle():
        list2.append(i.title())
    else:
        list2.append(i)
print(list2)
