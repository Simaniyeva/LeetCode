count=int(input())
result=[]
for i in range(1,count+1):
    if i%3==0 and i%5==0:
        result.append("FizzBuzz")
    elif i%5==0:
        result.append('Buzz')
    elif i%3==0:
        result.append('Fizz')
    else:
        i=str(i)
        result.append(i)
print(result)
