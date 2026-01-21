x=int(input())
new=0
m=x
if x<0:
    m*=-1
while m>0:
    last=m%10
    m//=10
    new=new*10+last
if x<0:
    print(new*-1)
print(new)