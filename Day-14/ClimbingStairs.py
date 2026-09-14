class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n

        one_step = 1
        two_steps = 2

        for i in range(3, n + 1):
            ways = one_step + two_steps

            one_step = two_steps
            two_steps = ways

        return two_steps
