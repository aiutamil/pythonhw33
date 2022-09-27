n = int(input())
m = int(input())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
def min_elts(A):
    return list(map(min,A))
