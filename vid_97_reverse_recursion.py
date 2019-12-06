
def reverse(s):
    if len(s) == 0:
        return ''
    return s[len(s)-1] + reverse(s[:len(s)-1])

print(reverse('hello world'))