a=input("enter the first string")
b=input("enter the second string")
if len(a)==len(b) and b in a+a:
    print("rotation")
else:
    print("not rotation")