n = int(input("Enter number of rows:"))
m = int(input("Enter the number of columns:"))
A = []
print("Enter numbers:")
for i in range(n):
    A.append(list(map(int, input().split())))

print('MATRIX:')
for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()
for i in range(n):
    tmp = A[i][0]
    A[i][0] = A[i][m-1]
    A[i][m-1] = tmp

for i in range(n):
    for j in range(m):
        print("%2d " % A[i][j], end=' ')
    print()
