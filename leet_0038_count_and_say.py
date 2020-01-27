"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do
so recursively, in other words from the previous member read off the digits, counting the number of
digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:
Input: 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as
"12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the
concatenation of "12" and "11" which is "1211".

"""

class Solution:

    def countAndSay_2(self, n):
        if n > 30 or n < 1:
            return ''
        if n == 1:
            return '1'
        new_num = ''
        count_loop = 1
        num = '1'

        while count_loop < n:
            idx_i, idx_j = 0, 0
            count, new_num = 0, ''

            while idx_j < len(num):
                if num[idx_i] != num[idx_j]:
                    new_num += str(count) + str(num[idx_i])
                    count = 0
                    idx_i = idx_j
                else:
                    count += 1
                    idx_j += 1

            if count > 0:
                new_num += str(count) + str(num[idx_i])
            num = new_num
            count_loop += 1

        return new_num


    def countAndSay(self, n):
        word_dict = {1: '1', 2: '11', 3: '21', 4: '1211', 5: '111221', 6: '312211', 7: '13112221',
                     8: '1113213211', 9: '31131211131221', 10: '13211311123113112211'
                     }
        if n < 11:
            return word_dict[n]


        for i in range(11, n+1):
            pre_say = word_dict[i-1]
            temp_char = pre_say[0]
            temp_count = 1
            dict_str = ''

            for j in range(1, len(pre_say)):
                if temp_char == pre_say[j]:
                    temp_count += 1
                else:
                    dict_str += str(temp_count) + temp_char
                    temp_count = 1
                    temp_char = pre_say[j]
                if j == len(pre_say) - 1:
                    dict_str += str(temp_count) + pre_say[j]



            word_dict[i] = dict_str

        return(word_dict[n])






mysolution = Solution()
print(mysolution.countAndSay(13))