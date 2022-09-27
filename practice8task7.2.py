def lower(matrix, row, col):
    for i in range(0, row):

        for j in range(0, col):

            if i < j:

                print("0", end=" ")

            else:
                print(matrix[i][j],
                      end=" ")

        print(" ")


def upper(matrix, row, col):
    for i in range(0, row):

        for j in range(0, col):

            if i > j:
                print("0", end=" ")

            else:
                print(matrix[i][j],
                      end=" ")

        print(" ")


n = int(input("Enter the number of rows:"))
m = int(input("Enter the number of columns:"))
a = []
print("Enter numbers:")
for i in range(n):
    a.append(list(map(int, input().split())))

print("Lower triangular matrix: ")
lower(a, n, m)

print("Upper triangular matrix: ")
upper(a, n, m)
