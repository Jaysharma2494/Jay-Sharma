count1,count2,count3,count4,count5=0,0,0,0,0
while True:
   X=int(input("enter a number:"))
   if X==-1:
      break
   if X>=1 and X<=10:
      if X>=1 and X<=2:
         count1+=1
      elif X>=3 and X<=4:
         count2+=1
      elif X>=5 and X<=6:
         count3+=1 
      elif X>=7 and X<=8:
         count4+=1
      elif X>=9 and X<=10:
         count5+=1 
total=count1+count2+count3+count4+count5             
print("#"*count1,end=" ") 
print(f"{(count1/total)*100:.2f}%") 
print("#"*count2,end=" ") 
print(f"{(count2/total)*100:.2f}%")  
print("#"*count3,end=" ") 
print(f"{(count3/total)*100:.2f}%")   
print("#"*count4,end=" ") 
print(f"{(count4/total)*100:.2f}%")   
print("#"*count5,end=" ") 
print(f"{(count5/total)*100:.2f}%") 
