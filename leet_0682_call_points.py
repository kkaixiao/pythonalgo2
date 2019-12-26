#!/usr/bin/python
# -*- coding: UTF-8 -*-
#Leetcode.num = 682. Baseball Game
"""
You're now a baseball game point recorder.
Given a list of strings, each string can be one of the 4 following types:
Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.
You need to return the sum of the points you could get in all the rounds.
Example 1:
Input: ["5","2","C","D","+"]
Output: 30
Explanation:
Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2's data was invalid. The sum is: 5.
Round 3: You could get 10 points (the round 2's data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.
"""


def call_points1(arr):
    stack_points = []
    for item in arr:
        if item not in ['+', 'C', 'D']:
            stack_points.append(int(item))
        elif item == 'C':
            if len(stack_points) > 0:
                stack_points.pop()
        elif item == 'D':
            if len(stack_points) > 0:
                stack_points.append(stack_points[-1]*2)
        elif item == '+':
            if len(stack_points) == 1:
                stack_points.append(stack_points[-1])
            elif len(stack_points) > 1:
                stack_points.append(stack_points[-1] + stack_points[-2])
    return sum(stack_points)


def call_points2(arr):
    stack_points = []
    dict_chars = {'+': (lambda x, y=0: x+y), 'D': (lambda x, y=0: 2*x)}
    for item in arr:
        if item not in ['+', 'C', 'D']:
            stack_points.append(int(item))
        elif item == 'C':
            if len(stack_points) > 0:
                stack_points.pop()
        else:
            if len(stack_points) > 0:
                if len(stack_points) == 1:
                    stack_points.append(dict_chars[item](stack_points[-1]))
                else:
                    stack_points.append(dict_chars[item](stack_points[-1], stack_points[-2]))
    return sum(stack_points)

def call_points3(arr):
    stack_points = []
    dict_chars = {'+': (lambda x: sum(x[-2:])), 'D': (lambda x: 2*x[-1])}
    for item in arr:
        if item not in ['+', 'C', 'D']:
            stack_points.append(int(item))
        elif item == 'C':
            if len(stack_points) > 0:
                stack_points.pop()
        else:
            if len(stack_points) > 0:
                stack_points.append(dict_chars[item](stack_points.copy()))


    return sum(stack_points)

arr2 = ["5","2","C","D","+"]
print(call_points3(arr2))