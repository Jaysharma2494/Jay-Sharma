n=(input("enter the number:"))
r=len(n)
p=int(n)
# while (p>0):
for i in range(1,r+1):
  if n[i]==n[r-i-1]:
    print("number is pelindrome")
    break
  else:
    print("number is not pelindrome")
    break
left=0
right=r-1
while left<right:
  if n[left]==n[right]:
    print("palidrome")
    left=left+1
    right-=r-1
  else:
    print("not palidrome")
