a=int(input('enter the number:'))
b=int(input("enter the number:"))
num = 1
while True:
  if (num % a == 0) and (num % b == 0):
    break
  num = num + 1
print(num)
