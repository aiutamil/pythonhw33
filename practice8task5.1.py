def printA(arr, m, n):
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


def sortA(arr, m, n):
    for i in range(m):
        arr[i].sort()
    print()


n = int(input("Enter the number of rows:"))
m = int(input("Enter the number of columns:"))
a = []
print("Enter numbers:")
for i in range(n):
    a.append(list(map(int, input().split())))

print('MATRIX: ')
printA(a, m, n)

sortA(a, m, n)
print('SORTED:')
printA(a, m, n)
