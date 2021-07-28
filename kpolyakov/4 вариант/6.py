g = 0
s=2384
while g != 29:
    g = 0
    s-=1
    r = s
    n = 5
    while r > 5:
        r = r // 2
        n = n + 4
    g = n
print(s)