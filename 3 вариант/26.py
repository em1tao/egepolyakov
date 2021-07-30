f = open("26-j5.txt")
n = int(f.readline())
a = []
val = 0
b = 0
m = 25
count = 0
for i in range(n):
    a.append(int(f.readline()))
for i in range(1,n-1):
    if a[i-1] >= a[i] >= a[i+1] or a[i+1] >= a[i] >= a[i-1]:
        b = a[i]
    elif a[i] >= a[i-1] >= a[i+1] or a[i+1] >= a[i-1] >= a[i]:
        b = a[i-1]
    else:
        b = a[i+1]
    if b < m:
        m = b
    elif b == m:
        count += 1
    if b < a[i]:
        val += a[i] - b
print(count, val)