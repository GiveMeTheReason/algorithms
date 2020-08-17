def arr_max(list):
    '''
    Divide and Rule (revursive)
    Returns the max of list (slower then built_in max())
    '''
    if len(list) == 0:
        return None
    if len(list) == 1:
        return list[0]
    if len(list) == 2:
        return max(list[0], list[1])
    else:
        return max(list[0], arr_max(list[1:]))

print(arr_max([1, 2, 4, 6, 3, 1]))  # 6
print(arr_max([1]))  # 1
print(arr_max([]))  # None
