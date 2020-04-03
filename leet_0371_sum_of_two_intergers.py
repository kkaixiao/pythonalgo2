


"""
tmp_a and tmp_b is only used as and exit condition, they are shifted right in every iteration until
both become zeroes
mask is used to make sure tmp_a and tmp_b will eventually become zeroes and while loop is exited
we use a and b in all other operations
each bit in a and b is masked in each loop, the bitmask is shifted left every iteration
carry = 1 if any pair of masked a, masked b, or carry are both ones, carry is also shifted left in
every iteration
res = 1 if number of ones amoung masked a, masked b, and carry is an odd number
After quitting the loop, if carry is non-zero , then we "OR" it with res, but also mask it with
32bits of ones to make
 sure the answer lies in 32 bits
If res is larger than the largest signed integer in 32 bits (0x7FFFFFFF), then its left-most bit
is one and therefore must be a negative number, so we'll return its invert : -(x+1)
[https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations]) instead.
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry, bitmask, mask = 0, 1, 0xffffffff
        res = 0
        MAX = 0x7fffffff
        tmp_a, tmp_b = a&mask, b&mask
        while tmp_a or tmp_b:
            da, db = a&bitmask, b&bitmask
            res |= (da ^ db ^ carry)
            carry = ((da&db) | (da&carry) | (db&carry))
            tmp_a >>= 1
            tmp_b >>= 1
            bitmask <<= 1
            carry <<= 1
        res = (res|carry)&mask
        return res if res <= MAX else ~(res^mask)