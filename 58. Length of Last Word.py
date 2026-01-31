s= "Today is a nice day"

#1st
# max_length_sub=0
# substrings=s.split(" ")
# for sub in substrings:
#     if max_length_sub<len(sub):
#         max_length_sub=len(sub)
# print(max_length_sub)


#2nd
i=len(s)-1
length=0
while s[i]==' ':
    i-=1
while i>=0 and s[i]!=' ':
    length+=1
    i-=1
print(length)
