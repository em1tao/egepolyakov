f = open("24-s1.txt")
k = 0
while (n:=f.readline().strip())!="":
    if n.count("S") == n.count("X"): k+=1
print(k)