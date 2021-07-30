f = open("f.txt")
mons = []
for i in range(10):
    mons.append(list(map(int,f.readline().split())))
vars = []
def func(x=0,y=0,m=0):
    if x == 9 and y == 9:
        m += mons[y][x]
        vars.append(m)
    elif x > 9 or x < 0 or y > 9 or y <0:
        pass
    else:
        m += mons[y][x]
        func(x+1,y,m)
        func(x,y+1,m)
func()
print(max(vars))
print(min(vars))

