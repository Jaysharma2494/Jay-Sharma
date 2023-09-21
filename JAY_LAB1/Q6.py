a=int(input())
b=int(input())
c=int(input())
D=b**2-4*a*c
x_1=(-b+D**(0.5))/2*a
x_2=(-b-D**(0.5))/2*a
if D>=0:
    print(x_1,x_2)
elif D<0:
    print("imaginary roots")