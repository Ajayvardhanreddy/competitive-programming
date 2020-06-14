# 1342. Number of Steps to Reduce a Number to Zero

'''
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

'''


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num /= 2
            steps += 1
        return steps
