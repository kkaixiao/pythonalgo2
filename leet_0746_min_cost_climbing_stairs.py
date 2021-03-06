"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost
to reach the top of the floor, and you can either start from the step with index 0, or the
step with index 1.

Example 1:

Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:

cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

"""


def min_cost_climbing_stairs(cost):
    for i in range(2, len(cost)):
        cost[i] += min(cost[i-1], cost[i-2])
    return min(cost[-1], cost[-2])


def min_cost_climbing_stairs2(cost):
    dict_cost = dict(enumerate(cost))
    for i in range(2, len(cost)):
        dict_cost[i] += min(dict_cost[i-1], dict_cost[i-2])
    return min(dict_cost[len(cost)-1], dict_cost[len(cost)-2])



cost1 = [10, 15, 20]
# cost1 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(min_cost_climbing_stairs2(cost1))
