f = open("24-s1.txt")
s = 0
while (l:=f.readline().strip()) != "":
    if l.count("YZ") > 1:
        s+=1
print(s)