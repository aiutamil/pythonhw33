def maxElement(arr):
    numb_of_rows = len(arr)
    numb_of_column = len(arr[0])

    for i in range(numb_of_rows):

        max1 = 0
        for j in range(numb_of_column):
            if arr[i][j] > max1:
                max1 = arr[i][j]

        print("Maximum element is:",max1)


n = int(input("Enter the number of rows:"))
m = int(input("Enter the number of columns:"))
a = []
print("Enter the numbers:")
for i in range(n):
    a.append(list(map(int, input().split())))

maxElement(a)
