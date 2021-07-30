def func(n):
    b = bin(n)[2::]
    if b[-1] == 0: return int(b+"10",2)
    else: return int(b+"01",2)

for i in range(100):
    if func(i) > 73:
        print(i)
        break
