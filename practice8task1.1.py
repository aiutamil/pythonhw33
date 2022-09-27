n=3
A=[]

for i in range(n):
    B=[]
    for i in range (n):
        B.append (int(input()))
    A.append(B)

for i in range (n):
    for j in range (n):
        print (A[i][j], end=' ')
    print ()



MAX = 100

def printDiagonalSums(mat, n):

	principal = 0
	for i in range(0, n):
		for j in range(0, n):

			# Condition for principal diagonal
			if (i == j):
				principal += mat[i][j]
				print("Principal Diagonal:", principal)
	


printDiagonalSums(A, n)

