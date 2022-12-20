#2.write a program to create the equation (a+b+c) *  (a-b-c) * ab + a^2 + b ^2 + (abc)^3.
a=float(input())
b=float(input())
c=float(input())
def equation(a,b,c):
    import math
    d=((a+b+c)*(a-b-c)*a*b)+(a**2)+(b**2)+((a*b*c)**3)
    return d
print(equation(a,b,c))
