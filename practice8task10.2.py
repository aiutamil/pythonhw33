def sortRowWise(m):
    for i in range(len(m)):

        for j in range(len(m[i])):

            for k in range(len(m[i]) - j - 1):

                if m[i][k] > m[i][k + 1]:
                    t = m[i][k]
                    m[i][k] = m[i][k + 1]
                    m[i][k + 1] = t

    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
a = []
print("Enter numbers:")
for i in range(n):
    a.append(list(map(int, input().split())))
sortRowWise(a)
