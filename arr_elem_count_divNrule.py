def arr_elem_count(list):
    '''
    Divide and Rule (revursive)
    Counts the number of elements in list
    '''
    if list == []:
        return 0
    else:
        return 1 + arr_elem_count(list[1:])

print(arr_elem_count([1, 2, 3, 4]))  # 4
print(help(arr_elem_count))
