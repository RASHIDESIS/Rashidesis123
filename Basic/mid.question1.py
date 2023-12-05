list_1 = [1,2,3,4,5,6,7,8]

n = len(list_1)

sum = 0
for i in list_1:
    sum = sum + i

mean = sum/n
print("Mean =",mean)

sum1 = 0
for j in list_1:
    sum1 = sum1 + (j-mean)**2
print (sum1)

x = sum1/(n-1)
print(x)

SD = x**0.5
print("Standard deviation = ",SD)