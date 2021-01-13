user_input = input()

def single(n):
	if len(n) == 1:
		# return int(n)
		print(n)
	else:
		t = sum([int(x) for x in n])
		single(str(t))


single(user_input)

