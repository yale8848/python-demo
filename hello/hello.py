
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
