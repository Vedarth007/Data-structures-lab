

M = []
B = []
A = []
add = []
sub =[]
trans =[]
mul =[]

matrix=[]
list1=[]
r = int(input("enter rows: "))
c = int(input("enter column: "))

'''def matinput(matrix):'''
for i in range(r):
		print("input for matrix ")
		A=[]
		for j in range(c):
			A.append(int(input("Enter element: ")))
		matrix.append(A)

def matadd(matrix,list1):

	for i in range(r):
		d =[]
		for i in range(c):
			d.append(0)
		add.append(d)

	for i in range(r):
		for j in range(c):
			add[i][j] = matrix[i][j] + list1[i][j]

	print(add)
matadd(matrix,list1)
"""
def matsub(list,list1):
	
	for i in range(r):
		d =[]
		for i in range(c):
			d.append(0)
		sub.append(d)

	for i in range(r):
		for j in range(c):
			sub[i][j] = list[i][j] - list1[i][j]

	print(sub)

def mattranspose(list):
	
	for i in range(r):
		d =[]
		for i in range(c):
			d.append(0)
		trans.append(d)
	for i in range(r):
		for j in range(c):
			trans[i][j] = list[j][i]
	print(trans)

def matmul(list,list1):

	for i in range(r):
			d =[]
			for i in range(c):
				d.append(0)
			mul.append(d)

	for i in range(r):
		for j in range(c):
			for k in range(c):
				mul[i][j] += list[i][k] * list1[k][j]

	print(mul)
	
def choice():
	print("0. to exit")
	print("1. Matrix addition")
	print("2. Matrix subtraction")
	print("3. Matrix transpose")
	print("4. Matrix multiplication")
	ch = int(input("enter your choice: "))
	if ch == 0:
		exit()
	if (ch == 1):
		matadd(matrix,list1)
		choice()
	if (ch == 2):
		matsub(A,B)
		choice()
	if (ch == 3):
		mattranspose(A)
		choice()
	if (ch == 4):
		matmul(A,B)
		choice()
	
		
def main():
	choice()
	

main()
"""



