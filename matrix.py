m=int(input("no of rows"))
n=int(input("no of cols"))
M1=[]
for i in range(m):
    sub=[]
    for j in range(n):
        e=int(input("enter elements"))
        sub.append(e)
    M1.append(sub)
print("first matrix=",M1)

M2=[]
for i in range(m):
    sub=[]
    for j in range(n):
        e=int(input("enter elements"))
        sub.append(e)
    M2.append(sub)
print("second matrix=",M2)

#addition
add=[]
for i in range(m):
    sub=[]
    for j in range(n):
        M3=M1[i][j]+M2[i][j]
        sub.append(M3)
    add.append(sub)
print("addition matrix",add)

#substraction
diff=[]
for i in range(m):
    sub=[]
    for j in range(n):
        M4=M1[i][j]-M2[i][j]
        sub.append(M4)
    diff.append(sub)
print("substraction matrix",diff)

#multiplication
mult=[]
for i in range(m):
    sub=[]
    for j in range(n):
        sum=0
        for k in range(m):
            sum=sum+M1[i][k]*M2[k][j]
        sub.append(sum)
    mult.append(sub)
print(mult)


#transpose
trans=[]
for i in range(m):
    sub=[]
    for j in range(n):
        M5=M1[j][i]
        sub.append(M5)
    trans.append(sub)
print(trans)





