def low_bound(list, item):
    '''
    Returns the index in the left of item element
    '''
    low = -1
    high = len(list)
    while high - low > 1:
        mid = (low + high) // 2
        if list[mid] < item:  # list[mid] > item for decreasing
            low = mid
        else:
            high = mid
    return low

def high_bound(list, item):
    '''
    Returns the index in the right of item element
    '''
    low = -1
    high = len(list)
    while high - low > 1:
        mid = (low + high) // 2
        if list[mid] <= item:  # list[mid] >= item for decreasing
            low = mid
        else:
            high = mid
    return high

def binary_search(list, item):
    '''
    Binary search
    Returns the index of the firts item or -1
    and numbers of them
    '''
    low = low_bound(list, item)
    high = high_bound(list, item)
    if high - low == 1:
        return -1, 0
    return low + 1, high - low - 1

my_list = [1, 3, 3, 3, 4, 5, 7]
print(my_list)

print(binary_search(my_list, 3), low_bound(my_list, 3), high_bound(my_list, 3))  # (1, 3) 0 4
print(binary_search(my_list, -1), low_bound(my_list, -1), high_bound(my_list, -1))  # (-1, 0) -1 0
print(binary_search(my_list, 4), low_bound(my_list, 4), high_bound(my_list, 4))  # (4, 1) 3 5
print(binary_search(my_list, 8), low_bound(my_list, 8), high_bound(my_list, 8))  # (-1, 0) 6 7
