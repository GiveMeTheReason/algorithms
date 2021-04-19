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
generate_numbers(4)  # ['012', '021', '102', '120', '201', '210']
c = 0
for i in range(len(l)):
    if l[i][0] == '0':
        print(l[i])
        c += 1
print(c)
