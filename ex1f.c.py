a=int(input("enter number of rows"))
for i in range(a):
    ch=chr(65+i)
    for j in range(i+1):
        print(ch,end=" ")
    print ( )
