d={}
s=input("enter the sentence").split()
d["beach"]="park"
d["mom"]="friend"
for i in s:
    if i in d:
       print(d[i] ,end=" ")
    else:
        print(i,end=" ")



