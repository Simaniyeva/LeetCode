customer=[[1,2,3],[5,8,9],[6,7,1]]
max_sum=0
for i in range(len(customer)):
    print(customer[i])
    sum=0
    for x in customer[i]:
        print(x)
        sum+=x
    print("sum:",sum)

    if sum>=max_sum:
        max_sum=sum

print("Max sum:",max_sum)


