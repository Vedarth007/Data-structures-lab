T=[]
R=int(input("enter number of rows"))
C=int(input("enter number of columns"))
for i in range(R):
	A=[]
	for j in range(C):
		x=int(input())
		A.append(x)
	T.append(A)
print(T)

G=[]
P=int(input("enter number of rows"))
Q=int(input("enter number of columns"))
for i in range(P):
	C=[]
	for j in range(Q):
		y=int(input())
		C.append(y)
	G.append(C)
print(G)
#Addition:
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(result)):  
    for j in range(len(result[0])):
	
        result[i][j] = T[i][j] + G[i][j]
print("\nAddition of following matrices is : ")
for i in range(len(result)):
	print(result[i])
#subtraction:'
substraction = [[0,0,0],
                [0,0,0],
                [0,0,0]]
for i in range(len(substraction)):  
    for j in range(len(substraction[0])):
        substraction[i][j] = T[i][j] - G[i][j]
print("\nSubtraction of following matrices is : ")
for i in range(len(substraction)):
	print(substraction[i])
#transpose:
transpose = [[0,0,0],
             [0,0,0],
             [0,0,0]]
for i in range(len(transpose)):  
    for j in range(len(transpose[0])):
        transpose[i][j] = T[i][j] + G[j][i]
print("\nTranspose of following matrices is : ")
for i in range(len(transpose)):
	print(transpose[i])


mul = [[0,0,0],
             [0,0,0],
             [0,0,0]]
for i in range(len(mul)):  
    for j in range(len(mul[0])):
        mul[i][j] = T[i][j] * G[j][i]
print("\nMultiplication of following matrices is : ")
for i in range(len(mul)):
	print(mul[i])
