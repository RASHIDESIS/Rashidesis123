list1 = [10,20,46,27,48]

list2 =["abcd","hdje"]

as_ci =[]
for i in list2:
    sum = 0
    for j in i:
        asci = ord(j)
        sum = sum + asci
    as_ci.append(asci)
print(as_ci)
