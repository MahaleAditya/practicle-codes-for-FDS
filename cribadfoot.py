U=[]
u=int(input("Total number of students in class:"))
for i in range(u):
    i=i+1
    U.append(i)
print("total number of studentys in calss:")

A=[]
a=int(input("No of stuents who play cricket:"))

for i in range(a):
    r=int(input("enter the roll numbers:"))
    A.append(r)
print("Roll numbers of students who play cricket:",A)

B=[]
b=int(input("No of students who play badminton:"))

for i in range(b):
    r=int(input("Enter the roll number:"))
    B.append(r)
print("Roll numbers of students who play badminton:",B)

C=[]
c=int(input("Number of students who play football:"))

for i in range(c):
    r=int(input('Enter the roll numbers:'))
    C.append(r)
print("Roll numbers of students who play football:",C)

AandB=[]

for i in range(a):
    for j in range(b):
        if A[i]==B[j]:
            AandB.append(A[i])
print("Number of students who play both cricket and badminton:",AandB)

AorB=[]
for i in range(a):
    AorB.append(A[i])
for i in range(b):
    flag=0
    for j in range(a):
        if(B[i]==A[j]):
            flag=1
            break
    if(flag==0):
        AorB.append(B[i])
#print("Number of students who play cricket or Badminton",AorB)

N=[]
for i in range(len(AorB)):
    flag=0
    for j in range(len(AandB)):
        if(AorB[i]==AandB[j]):
            flag=1
            break
    if flag==0:
        N.append(AorB[i])
print("Number of Students who play cricket and badminton but not both: ",N)

X=[]
for i in range(u):
    flag=0
    for j in range(len(AorB)):
        if U[i]==AorB[j]:
            flag=1
            break
    if flag==0:
        X.append(U[i])
print("Number of students who play neither nor badminton: ",X)

AandC=[]
for i in range(a):
    for j in range(c):
        if A[i]==C[j]:
            AandC.append(A[i])
#print("Number of students who play both cricket and football",AandC)

Y=[]
for i in range(len(AandC)):
    flag=0
    for j in range(b):
        if AandC[i]==B[j]:
            flag=1
            break
    if flag==0:
        Y.append(AandC[i])
print("Students who play cricketand football but not badminton",Y)


