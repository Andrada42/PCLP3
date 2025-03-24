def prim(nr):
    if(nr == 2)
        return 1
    if(nr < 1 or nr % 2 == 0)
    


n = input()
ct = 0

for i in range(n):
    if prim(i) == 1:
        print (i, end=" ")
        ct += 1

print(n)