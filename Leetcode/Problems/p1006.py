# 1006. Clumsy Factorial

'''
Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.
'''


class Solution:
    def clumsy(self, N: int) -> int:
        curr = N
        res = 0
        while curr >= 1:
            if curr >= 3:
                if curr == N:
                    res += curr * (curr - 1) // (curr - 2)
                else:
                    res -= curr * (curr - 1) // (curr - 2)
                curr -= 3
                if curr >= 1:
                    res += curr
                    curr -= 1
            else:
                if curr == 2:
                    if curr == N:
                        res += 2 * 1
                    else:
                        res -= 2 * 1
                    curr -= 2
                elif curr == 1:
                    if curr == N:
                        res += 1
                    else:
                        res -= 1
                    curr -= 1
        return res
