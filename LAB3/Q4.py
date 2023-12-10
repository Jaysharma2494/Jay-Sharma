xyz=int(input("enter three digit no.:"))
ones = xyz % 10
tens = (xyz% 100) // 10
hundreds = (xyz % 1000) // 100
sum=ones+tens+hundreds
print("sum of three digits is:",sum)
if sum % 3==0:
  print("number is divisible by 3")

else:
  print("number is not divisible by 3")
