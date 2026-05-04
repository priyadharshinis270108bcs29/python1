x=float(input("enter your current balance"))
print("1.deposit,2.withdrawl")
y=int(input("enter your type of transaction"))
z=float(input("enter the transaction amount"))
if y==1:
   if z>=1000:
      s=x+z
      print("updated balance is= ",s)
   else:
      print("the amount cannot be deposited min balance is not sufficient")
elif y==2:
   if x-z<1000:
      print("the amount cannot be withdrawl min balance is not sufficient")
   else:
      u=x-z
      print("updated balance is= ",u)
else:
      print("invalid choice")
