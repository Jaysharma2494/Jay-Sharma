x=str(input("enter the paragraph:"))
di_count=0
al_count=0
al_count1=0
s_count=0
for i in x:
    if i.islower():
        al_count+=1
    elif i.isupper():
        al_count1+=1
    elif i.isdigit():
        di_count+=1
    else:
        s_count+=0

print("the lower characters are",al_count)
print("the upper characters are",al_count1)
print("the digit characters are",di_count)
print("the special characters are",s_count)
