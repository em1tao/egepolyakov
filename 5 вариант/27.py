f = open("27-29b.txt")
n = int(f.readline())
summ = 0
s = 10000
div = 5
for i in range(n):
    k1,k2,k3 = map(int, f.readline().split())
    a,c = max(k1,k2,k3), min(k1,k2,k3)
    b = k1+k2+k3-a-c
    summ+=a+b
    r1,r2 = a-c, b-c
    if s > min(r1,r2) and min(r1,r2) % div !=0: s=min(r1,r2)

print(summ if summ % 5 != 0 else summ-s)