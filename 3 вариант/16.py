def func(n):
    if n <= 13:
        return n**3 + n*n + 1
    elif (n > 13) and (n % 3 == 0):
        return func(n-1) + 2*n*n -3 
    elif (n > 13) and (n % 3 != 0):
        return func(n-2) + 3*n + 6

c = 0
for i in range(1,1001):
    if func(i) % 2 != 0: c+=1

print(c)