def counter(a,b):
    a_set,b_set = set(str(a)), set(str(b))
    return len(a_set.intersection(b_set))

print counter(123445,456)