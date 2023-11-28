str1 = "mushfiq"
str2 = "rashid"
# count = 0
# for i in str1:
#     count = count +1
# print(count)

def custom_len(x,y):
    count1 = 0
    count2 = 0
    for i in x:
         count1 = count1 +1
    for j in y:
         count2 = count2 +1
    return(count1,count2)

a,b = custom_len(str1,str2)
print(a,b)