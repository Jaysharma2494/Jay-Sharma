year=int(input("Enter the year(in 4 digit):"))
if year>0:
  if year%4==0:   #jo year agr 4 se complete divide ho jati he vo leap year hoti he or yha agr remainder 0 aya to leap year hounga 
    print("Entered Year(",year,") is a lear year ")
  else:
    print("Entered Year is not a leap year")
elif (year<=0):
  print("Entered the valid year")
else:
  print("you can try again")
