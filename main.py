a, b, l = list(map(lambda x: int(x), input().split()))

all_l = 0
all_s = 0
c = 0

while True:
	# if l == 1:
	# 	all_s = a
	# 	break
	c += 1
	all_l += c
	if all_l > l:
		break
	all_s += c * a + b

print(all_s)
