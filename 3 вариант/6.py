for s in range(1,1000):
    z = s
    n = 50
    while s > 0:
        s = s // 2
        n = n - 3
    if n == 23:
        break
print(z)