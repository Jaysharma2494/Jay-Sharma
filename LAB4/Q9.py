sent=input("enter the sentence:")
i=0
capital,lower,digit,char=0,0,0,0
while i<len(sent):
  if sent[i]>= 'A' and sent[i]<='Z':
    capital=capital+1
  elif ord(sent[i])>=48 and ord(sent[i])<=57:
    digit=digit+1
  elif ord(sent[i])>=97 and ord(sent[i])<=122:
    lower=lower+1
  i=i+1

print("capital letter",capital)
print("lower letters",lower)
print("digits",digit)
print("character letters",char)
    
