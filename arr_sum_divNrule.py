def arr_sum(list):
    '''
    Divide and Rule (revursive)
    Returns the sum of list (slower then built_in sum())
    '''
    if list == []:
        return 0
    else:
        return list[0] + arr_sum(list[1:])

print(arr_sum([1, 2, 3, 4]))  # 10
