list_1 = [1,2,3,4,5]
print(list_1[0:3])

sum = 0
for i in list_1:
    sum = sum + i
print(sum)


# for i in range(len(list_1)):
#     print(list_1[i])

# append = add the value into the last index
print ("before append",list_1)
list_1.append(6)
print("after append",list_1)

# clear = clear all, the indexes
print("before clear", list_1)
list_1.clear()
print("after clear", list_1)

# copy = copy of list to another one 

list_2 = list_1.copy()
print(list_2)

list_3 = [11,20,33,40,55,50,57,52]

# cnt = list_3.count(50)
# print("number:", cnt)
# count = 0
# for i in list_3:
#     if(i==50):
#         count = count + 1
#     else:
#         count = count
# print (count)    
even_list =[]
odd_list =[]

for i in list_3:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
        

print("even:",even_list)
print("odd:",odd_list)


print(list_3)
list_3.insert(0,69)
print("after insert:",list_3)

meow = ("abcd","djegb")
first=len(meow[0])
print(first)
