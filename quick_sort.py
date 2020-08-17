from datetime import datetime

start_time = datetime.now()

def quick_sort(list):
    '''
    Quick sort (recursive)
    '''
    if len(list) < 2:
        return list
    fund = list[0]
    middle = [fund]
    less = []
    greater = []
    for i in list[1:]:
        if i < fund:
            less.append(i)
        elif i > fund:
            greater.append(i)
        else:
            middle.append(i)
    return quick_sort(less) + middle + quick_sort(greater)

print(quick_sort([1, 2, 3, 4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(quick_sort([15, 23, 73, 12, 54, 12, 34, 54]))  # [12, 12, 15, 23, 34, 54, 54, 73]
print(quick_sort([5, 5, 5, 5, 4, 4, 6, 10]))  # [4, 4, 5, 5, 5, 5, 6, 10]

print(datetime.now() - start_time)  # 0:00:00.001000 (17.08.2020)
