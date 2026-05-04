lst=[10,20,30,40]
while True:
    print("1.add element at position")
    print("2.add element at last")
    print("3.compare two lists")
    print("4.print id of elements")
    print("5.first occurance")
    print("6.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        pos=int(input("enter the position"))
        val=int(input("enter the value"))
        lst.insert(pos,val)
        print(lst)
    elif ch==2:
        val=int(input("enter the value"))
        lst.append(val)
        print(lst)
    elif ch==3:
        list2=[10,20,30,40]
        if lst==list2:
            print("lists are equal")
        else:
            print("lists are not equal")
    elif ch==4:
        for i in list:
            print(i,id(i))
    elif ch==5:
        x=int(input("enter element"))
        print("index:",lst.index(x))
    elif ch==6:
        break