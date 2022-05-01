import math
# addition

x=int(input("ENTER FIRST NUMBER:"))
y=int(input("ENTER SECOND NUMBER:"))

SUM=x+y
print("THE SUM IS: ",SUM ,"\n*****\n")

#subraction
if(x>y):
    subract=x-y

else:
    subract=y-x

print("THE DIFFERENCE IS: ",subract ,"\n*****\n")

#Multiplication
Mul=x*y
print("THE PRODUCT IS: ",Mul ,"\n*****\n")

#Division
Div=x/y
print("X/Y IS: ",Div ,"\n*****\n")

#exponentation

print("Exponentation ",x,"^",y,"is ",x**y,"\n****\n")