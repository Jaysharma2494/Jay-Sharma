p=int(input("enter the amount:"))
t=int(input("enter the time(in months)"))
t_1=t/12
if p<500 or t<6:
  print("enter the minimun time and principle")
elif p>=500 and t>=6:
  si=(p*7.1*t_1)/100
  print("intrest is",si)
else:
  print("enter the right value")
