n=int(input())
digits=set()
while n!=1 and n not in digits:
    digits.add(n)
    sum=0
    while n>0:
        n,digit=divmod(n,10)
        sum+=digit*digit
    n=sum
return n==1
        
    