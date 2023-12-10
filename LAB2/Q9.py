print("COVERSION OF SECONS TO HOURS,MINUTE,SECOND".center(50))
time=int(input("Enter the seconds in the range of 1 to 86400:"))
hour=int(time/3600)
a=hour*3600
minute= int((time-a)/60)
b=minute*60
second=(time - a - b )
if time>=0:
    print("Your given number in seconds converted into hour:minute:second",hour,":",minute,":",second)
else:
    print("Please, Entered the second in the given range")
    