def is_braces_correct(s):
    '''
    Returns True if the braces sequence is correct ([{}])
    '''
    stack = []
    for i in s:
        if i in '([{':
            stack.append(i)
        elif i in ')]}':
            if stack:
                x = stack.pop()
                if i == ')' and x != '(':
                    return False
                elif i == ']' and x != '[':
                    return False
                elif i == '}' and x != '{':
                    return False
            else:
                return False
    if stack:
        return False
    return True

print(is_braces_correct("()((aa))()"))  # True
print(is_braces_correct("[()]"))  # True
print(is_braces_correct("[(a](}"))  # False
print(is_braces_correct("[{{}}](){()[aa[]]}"))  # True

'''
print(ord('('))  # 40
print(ord(')'))  # 41
print(ord('['))  # 91
print(ord(']'))  # 93
print(ord('{'))  # 123
print(ord('}'))  # 125
'''
