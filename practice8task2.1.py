n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of colums: "))
a = []
print("Enter numbers:")
for i in range(n):
    a.append(list(map(int, input().split())))


def magicSquare(a):
    diag1 = 0
    diag2 = 0
    for i in range(n):
        diag1 += a[i][i]
        diag2 += a[i][n - i - 1]
    if not (diag1 == diag2):
        return False
    for i in range(n):
        rows = 0
        cols = 0
        for j in range(n):
            rows += a[i][j]
            cols += a[j][i]
        if not (rows == cols == diag1):
            return False

    return True


if (magicSquare(a)):
    print("Magic Square")
else:
    print("Not magic square")
