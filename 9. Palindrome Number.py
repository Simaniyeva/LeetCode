def isPalindrome(self,x):
    if x<0:
        return False
    if x==0:
        return True
    if x%10==0:
        return False
    original=x
    reversed=0
    while x>0:
        last=x%10
        reversed=reversed*10+last
        x//=10
    return reversed==original
    