
t=int(input())
count=0
count_1=0
for i in range(t):
    a1,a2,a3,a4,a5,a6,a7=map(int,input().split())
    list=[a1,a2,a3,a4,a5,a6,a7]
    for k in range(7):
        if list[k]==1:
            count=count+1
        elif list[k]==0:
            count_1+=1
    if count>count_1:
        print("yes")
    else:
        print("no")
