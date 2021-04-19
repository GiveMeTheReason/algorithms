x = 3
y = -7
dx = 1
dy = 0
for i in range(4):
    print(x+dx)
    print(y+dy)
    print()
    dx, dy = -dy, dx

'''
Output:
4
-7

3
-6

2
-7

3
-8

'''
