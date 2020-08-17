def lis(a):
    '''
    Returns the largest increasing subsecuence
    and it's length
    '''
    F = [0]*(len(a))
    for i in range(0, len(a)):
        m = 0
        for j in range(0,i):
            if a[i] > a[j] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    F_max = 0
    F_ind = 0
    for i in range(len(a)):
        if F[i] > F_max:
            F_max = F[i]
            F_ind = i
    return F_max, a[F_ind-F_max+1:F_ind+1]

print(lis([0, 1, 2, 5, 0]))  # (4, [0, 1, 2, 5])
print(lis("akyzvieruhf"))  # (4, 'akyz')
