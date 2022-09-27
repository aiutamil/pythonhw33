n = int(input("Enter the numbers of rows:"))
m = int(input("Enter the number of columns:"))
A = []
print("Enter the numbers:")
for i in range(n):
    A.append(list(map(int, input().split())))

print('MATRIX:')
for i in range(m):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

a = [[1 if x > 0 else 0 for x in i] for i in A]
for i in range(len(A)):
    print(*[A[i][x] if x <= i else '' for x in range(len(A[i]))], '')
