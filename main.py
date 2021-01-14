user_input = int(input())

for _ in range(user_input, 0, -1):
	for __ in range(_, 0, -1):
		print(_ * __, end=' ')
	print()