def generate_numbers(N, M, prefix=None):
    '''
    Returns all combinations of numbers with base N and length M
    '''
    prefix = prefix or []
    if M == 0:
        # print(''.join(map(str, prefix)))
        # print(*prefix, sep='')
        l.append(''.join(map(str, prefix)))
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

l = []
generate_numbers(3, 2)  # ['00', '01', '02', '10', '11', '12', '20', '21', '22']
print(l)
