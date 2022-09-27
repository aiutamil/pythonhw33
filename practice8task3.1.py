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
b = "symmetric"
for i in range(m):
    for j in range(n):
        if A[i][j] != A[j][i]:
            b = "not symmetric"
            break
print(b)
