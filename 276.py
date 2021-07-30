f = open("27-28a.txt")
n = int(f.readline())
s = 0
m = 10000
for i in range(n):
    k1,k2 = map(int, f.readline().split())
    a = min(k1,k2)
    b = k1+k2-a
    s += a
    r1 = b-a
    if r1 < m:
        m = r1
print(s if oct(s)[-1] != "2" else s+m)
