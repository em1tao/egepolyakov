f = open("27-30b.txt")
n = int(f.readline())
mn = 10000
s = 0
for i in range(n):
    k1,k2,k3 = map(int, f.readline().split())
    a, c = max((k1,k2,k3)), min((k1,k2,k3))
    b = k1+k2+k3 - a - c
    r1, r2 = a-c, b-c
    s += c
    if mn > min(r1,r2): mn=min(r1,r2)

print(s if s%7!=0 else s+mn)