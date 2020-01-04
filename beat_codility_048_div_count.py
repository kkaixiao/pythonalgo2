
def div_count(a, b, k):
    last_div_num = b//k*k
    first_div_num = (a//k+1)*k
    return int((last_div_num-first_div_num)/k+1)



print(div_count(88, 100, 3))