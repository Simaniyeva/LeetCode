import math
def checkPerfectNumber(num):
    if num<=1:
        return False
    divisor=1
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            divisor+=i
            
            if i!=num//i:
                divisor+=num//i
    return divisor==sum
            
print(checkPerfectNumber(28))