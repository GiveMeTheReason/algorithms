def mex(a):
    '''
    Returns MEX of set(a)
    MEX = minimum excludant
    The min number from 0 excludant from set
    '''
    mex = 0
    while mex in a:
        mex += 1
    return mex

print(mex(set([0, 2, 3, 5])))  # 1
print(mex(set([1, 1, 2, 3, 4])))  # 0
print(mex(set([0, 1, 2, 3])))  # 4
