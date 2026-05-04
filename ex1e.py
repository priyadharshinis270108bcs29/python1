a=float(input("enter your salary"))
b=int(input("the total number of leave in month"))
if b<=2:
   print("the total salary is= ",a)
elif b>=3:
   a=a-(b-2)*500
   print("the total salary is= ",a)
