n = int(input("Enter the number of rows:"))
m = int(input("Enter the number of columns:"))
A = []
print("Enter numbers:")
for i in range(n):
    A.append(list(map(int, input().split())))

print('MATRIX: ')
for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

max = A[0][0]
ie = je = 0
for i in range(m):
    for j in range(n):
        if A[i][j] > max:
            max = A[i][j]
            ie = i
            je = j
A[0], A[ie] = A[ie], A[0]
A[0][0], A[0][je] = A[0][je], A[0][0]
for row in A:
    print(*map('{:2d}'.format, row))
