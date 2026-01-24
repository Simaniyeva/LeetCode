def climbStairs(n):
    if n==0 or n==1:
        return n
    first=1
    second=2
    for i in range(3,n+1):
            next=first+second
            first=second
            second=next
    return second

num=int(input())
print(climbStairs(num))     