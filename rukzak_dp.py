'''
Examle of "knapsack problem"
Used DP (dynamic programming)
'''

weight = 6
types = 5

a = [[(0, set())]*weight for i in range(types)]
d = [0]*types
d[0] = (3, 10)
d[1] = (1, 3)
d[2] = (2, 9)
d[3] = (2, 5)
d[4] = (1, 6)

for i in range(types):
    for j in range(weight):
        if (j-d[i][0]) >= 0:
            if a[i-1][j][0] > d[i][1]+a[i-1][j-d[i][0]][0]:
                a[i][j] = a[i-1][j]
            else:
                a[i][j] = (d[i][1]+a[i-1][j-d[i][0]][0], a[i-1][j-d[i][0]][1].union(set(str(i))))
        elif (j+1-d[i][0]) >= 0:
            if a[i-1][j][0] > d[i][1]:
                a[i][j] = a[i-1][j]
            else:
                a[i][j] = (d[i][1], set(str(i)))
        else:
            a[i][j] = a[i-1][j]

print(a[types-1][weight-1])  # (25, {'0', '4', '2'})
