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

def find_subsequence(sub, s):
    '''
    Returns the index of the sub in s or -1
    '''
    s1 = sub + "!" + s  # "!" - symbol not in (sub + s)
    l = prefix_pi_function(s1)
    for i in range(2*len(sub),len(s1)):
        if l[i] == len(sub):
            return(i - 2*len(sub))
    return -1

print(find_subsequence("cd", "abcde"))  # 2
print(find_subsequence("cab", "abacabadabacabaf"))  # 3
print(find_subsequence("men", "phenomenon"))  # 5
print(find_subsequence("a", "milk"))  # -1
print(find_subsequence("", "milk"))  # 0
print(find_subsequence("ce", "abcde"))  # -1
