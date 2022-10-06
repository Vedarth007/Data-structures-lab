def pal():
	str = input("ENTER STRING: ")

	a = len(str) - 1

	for i in range(0,len(str)):
		if str[i] == str[a]:
			i += 1
			a -= 1
			x = True
		else:
			x = False

	if x is True:
		print("is palindrome")
	else:
		print("not palindrome")
