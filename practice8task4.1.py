n=int(input('Enter the number of rows:'))
m=int(input('Enter the number of columns:'))
A=[]
print('Enter numbers:')
for i in range(n):
    B=[]
    for j in range(n):
        B.append(int(input()))
    A.append(B)

print('MATRIX:')
for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
s=[]
for i in range(len(A)):
    s.append(sum(A[i]))
print(A[s.index(max(s))],'Largest sum:',max(s),A[s.index(min(s))],'Smallest sum:',min(s))
