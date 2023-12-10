digit=int(input("enter the 5 digit no:"))
t=(digit%10)//1
i=(digit%100)//10
g=(digit%1000)//100
i_1=(digit%10000)//1000
d=(digit%100000)//10000
if (d==t and i==i_1 and g==g):
  print("entered no. is palindrome")

else:
  print("entered no. is not palindrome")
