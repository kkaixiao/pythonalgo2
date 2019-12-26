x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
w = {'c': 5, 'd': 6}

z = {**x, **y}

print(z)

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
z = {**x, **y, **w}

print(z)

