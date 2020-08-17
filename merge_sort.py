from datetime import datetime

start_time = datetime.now()

def merge_sort(list):
    '''
    Merge sort (recursive)
    '''
    if len(list) < 2:
        return list
    first_part = merge_sort(list[:len(list)//2])
    last_part = merge_sort(list[len(list)//2:])
    i = j = 0
    res = []
    while i < len(first_part) and j < len(last_part):
        if first_part[i] < last_part[j]:
            res.append(first_part[i])
            i += 1
        else:
            res.append(last_part[j])
            j += 1
    res.extend(first_part[i:])
    res.extend(last_part[j:])
    return res

print(merge_sort([1, 2, 3, 4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(merge_sort([15, 23, 73, 12, 54, 12, 34, 54]))  # [12, 12, 15, 23, 34, 54, 54, 73]
print(merge_sort([5, 5, 5, 5, 4, 4, 6, 10]))  # [4, 4, 5, 5, 5, 5, 6, 10]

print(datetime.now() - start_time)  # 0:00:00.000971 (17.08.2020)
