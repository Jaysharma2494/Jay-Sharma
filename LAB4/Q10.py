a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
if a==0:
    print("Invalid input. Please enter valid numerical coefficients of a .")
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Solutions: x1 = {x1:.2f}, x2 = {x2:.2f}")
elif d == 0:
    x1 = -b / (2*a)
    print(f"Solution: x1 = {x1:.2f}")
else:
    print("No real solutions. The solutions are complex.")
    
