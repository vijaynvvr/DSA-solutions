# you can either climb 1 or 2 steps at a time
# return num of ways to climb n steps

def climbingStairs(n):
    if n == 1 or n == 2: return n
    return climbingStairs(n-1) + climbingStairs(n-2)

n = 41
print(climbingStairs(n))
