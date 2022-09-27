
def showMatrix(mat,n,m):

    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print('')


def kthSmallest(arr, n, K):
    arr.sort()

    return arr[m - 1]


def ReplaceDiagonal(mat, n,m):
    arr = [0] * n

    for i in range(n):
        for j in range(n):
            arr[j] = mat[i][j]
        mat[i][i] = kthSmallest(arr, n, m)
    showMatrix(mat,n,m)


n = int(input("Enter the number of rows:"))
m = int(input("Enter number of columns"))
a = []
print("Enter numbers:")
for i in range(n):
    a.append(list(map(int, input().split())))

ReplaceDiagonal(a, n,m)
