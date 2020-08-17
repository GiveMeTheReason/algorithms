def generate_numbers(N, M=None, prefix=None):
    '''
    Returns all permunations of N numbers
    '''
    M = N if M == None else M
    prefix = prefix or []
    if M == 0:
        # print(''.join(map(str, prefix)))
        # print(*prefix, sep='')
        l.append(''.join(map(str, prefix)))
        return
    for digit in range(N):
        if digit in prefix:
            continue
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

l = []
generate_numbers(3)  # ['012', '021', '102', '120', '201', '210']
print(l)
