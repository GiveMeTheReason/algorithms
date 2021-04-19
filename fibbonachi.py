f = [1, 1]

a = 1

while a <= 200000:
    a = sum(f[-2:])
    f.append(a)

print(f)
