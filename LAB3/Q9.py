salary=float(input("enter yours gross salary:"))
if(salary<0):
  print("enter correct gross income")
elif (salary<300000):
  print("there is no income tax on it")

elif(salary>=300000 and salary<1000000):
  y=salary*(10/100)
  print("income tax on you salary is 10% so payable amount in tax is",y)

elif(salary>=1000000 and salary<2500000):
  z=salary*(20/100)
  print("income tax on you salary is 20% so payable amount in tax is",z)
elif (salary>=2500000):
  p=salary*(30/100)
  print("income tax on you salary is 30% so payable amount in tax is",p)

else:
  print("enter correct gross income")
  
  
