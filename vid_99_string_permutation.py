
def permute(s):
    out = []
    # Base Case
    if len(s) == 1:
        out = [s]
        
    else:
    # for every letter in the string s
        for i, let in enumerate(s):

            for perm in permute(s[:i] + s[i+1:]):
                out += [let + perm]

    return out


print(permute('abc'))
