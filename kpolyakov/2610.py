f = open("26-k3.txt")
n,k,m = map(int,f.readline().split())
top = []
for i in range(n):
    score = int(f.readline())
    if len(top) < k+m:
        top.append(score)
    elif score > min(top):
        top[top.index(min(top))] = score

top.sort(reverse=True)
print(top[k-1])
print(top[m+k-1])