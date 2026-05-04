temp=input("enter temperature(warm/cold)")
humidity=input("enter humudity(dry/humid)")
if temp=="warm":
    if(humidity=="dry"):
        print("play basketball")
    else:
        print("play tennis")
else:
    if(humidity=="dry"):
        print("play cricket")
    else:
        print("swim ")
