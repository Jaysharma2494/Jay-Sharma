side_1=input("enter the first side of tringle:")
side_2=input("enter the second side of tringle:")
side_3=input("enter the third side of tringle:")
if ((side_1+side_2)>side_3):
  if ((side_1==side_2)and(side_2==side_3)and(side_3==side_1)):
    print("they form equlateral triangle")
  else:
    print("they form triangle")
else:
  print("they can't form triangle")
