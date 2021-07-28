f = open("26-j4.txt")
n = int(f.readline())
o = 0
s = 0
mx = 0
l,m = [], []
for i in range(n//10):
    l.append(101)
    m.append(0)
for i in range(n):
    z = int(f.readline())
    o += z
    if z < max(l):
        l[l.index(max(l))] = z
    if z > min(m):
        mx = m[m.index(min(m))]
        m[m.index(min(m))] = z
    
print(o-sum(m)-sum(l))
print(mx)