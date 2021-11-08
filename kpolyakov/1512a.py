for i in range(int(input())):
    n = int(input())
    massive = input().split()
    for i in set(massive):
        if massive.count(i) == 1:
            print(massive.index(i)+1)
