f = open("26-j3.txt")
s,n = map(int, f.readline().split())
m = [0] * (n // 100)
print(m)
for i in range(n):
    l = int(f.readline())
    if l > min(m):
        m.index(min(m)) = l
