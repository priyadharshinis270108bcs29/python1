a=[[1,2,3],[4,5,6]]
b=[[7,8],[9,10],[11,12]]
result=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j]=result[i][j]+a[i][k]*b[k][j]
for r in result:
    print(r)