def prefix_pi_function(s):
    '''
    Returns the list of PI-function of string
    PI-function - max prefix length that can be own suffix
    (own suffix excludes full string)
    See also Knuth–Morris–Pratt algorithm
    '''
    l = [0]*(len(s))
    for i in range(1, len(s)):
        w = l[i-1]
        while w >= 0:
            if s[i] == s[w]:
                l[i] = w + 1
                break
            if w == 0:
                l[i] = 0
                break
            w = l[w-1]
    return l

print(prefix_pi_function("aaaa"))  # [0, 1, 2, 3]
print(prefix_pi_function("aba"))  # [0, 0, 1]
print(prefix_pi_function("abacabadabacabaf"))  # [0, 0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 0]
print(prefix_pi_function("abacabadabacabad"))  # [0, 0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 8]
print(prefix_pi_function("phenomenon"))  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
