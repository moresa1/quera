user_input = sum(list(map(lambda x: 181 if int(x) == 0 else int(x) , input().split())))
print('Yes' if user_input == 180 else 'No')