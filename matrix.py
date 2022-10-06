matrix = []

r = int(input("Enter number of rows in a matrix :"))
c = int(input("Enter number of columns in the matrix :"))
"""for i in range(r):
A=[]
	for j in range(c):
	x=int(input())
	A.append(x)
	matrix.append(A)"""

def matinput(list):
	for i in range(r):
		print("input for matrix ")
		A=[]
		for j in range(c):
			A.append(int(input("Enter element: ")))
		list.append(A)
def matadd(list,list1):
	
	for i in range(r):
		d =[]
		for i in range(c):
			d.append(0)
		add.append(d)

	for i in range(r):
		for j in range(c):
			add[i][j] = list[i][j] + list1[i][j]

	print(add)
matadd(A,B)
