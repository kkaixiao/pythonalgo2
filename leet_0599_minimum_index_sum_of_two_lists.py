"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of
favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is
a choice tie between answers, output all of them with no order requirement. You could assume
there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index
sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        # the dictionary's value will be like [a, b], where a is the number of occurence, and
        # b is the index number sum

        dictRest = {}

        for i in range(len(list1)):
            dictRest[list1[i]] = [dictRest.get(list1[i], [0, i])[0] + 1, i]

        listIdx = []
        for j in range(len(list2)):
            orgIdx, orgOcc = dictRest.get(list2[j], [0, 0])[1], dictRest.get(list2[j], [0, 0])[0]

            if dictRest.get(list2[j], [0, j])[0] > 0:
                listIdx.append(j + orgIdx)

            dictRest[list2[j]] = [orgOcc + 1, j + orgIdx]

        minIdx = min(listIdx)
        res = []

        for k, v in dictRest.items():
            if v[0] > 1 and v[1] == minIdx:
                res.append(k)

        return res

    # a bit optimized function
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # the dictionary's value will be like [a, b], where a is the number of occurence, and
        # b is the index number sum

        dictRest1 = {}

        for i in range(len(list1)):
            dictRest1[list1[i]] = [dictRest1.get(list1[i], [0, i])[0] + 1, i]

        dictRest2 = {}
        minIdx = 2000
        for j in range(len(list2)):
            orgIdx, orgOcc = dictRest1.get(list2[j], [0, 0])[1], dictRest1.get(list2[j], [0, 0])[0]

            if orgOcc > 0:
                dictRest2[list2[j]] = j + orgIdx
                minIdx = min(minIdx, j + orgIdx)

        res = []

        for k, v in dictRest2.items():
            if v == minIdx:
                res.append(k)

        return res