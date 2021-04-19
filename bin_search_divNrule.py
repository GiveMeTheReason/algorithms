def bin_search(list, item):
    '''
    Divide and Rule (revursive)
    Binary search
    Returns the index of the element or -1
    '''
    mid = len(list) // 2
    if list == []:
        return -1
    if list[mid] == item:
        return mid
    if list[mid] > item:
        return bin_search(list[:mid], item)
    else:
        return mid + 1 + bin_search(list[mid+1:], item)

print(bin_search([1, 2, 3, 4, 5, 6, 7, 8], 1))  # 0
print(bin_search([1, 2, 3, 4, 5, 6, 7, 8], -1))  # -1
