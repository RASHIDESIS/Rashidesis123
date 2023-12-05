input_1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
input_2 = []
print ()
print("Input_1")
for a in input_1:
    for b in a:
        print(b ,end =" ")
    print ()

print()
# sum = 0
print("Output_1:")
for i in input_1:
    for k in i:
        output_1 = k % 10
        print (output_1 ,end =" ")
    print ()
    # input_2.append(output_1)
    # sum = sum + output_1
output_1 = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]]
print()
print("Output_2:")
for i in input_1:
    for k in i:
        if k % 2 ==0:
            print("EVEN", end =" ")
        else:
            print("ODD", end =" ")
    print()

print()
print("Output_3:")
for i in output_1:
    sum = 0
    for j in i:
        sum = sum + j
    input_2.append(sum)
print(input_2)

print()
print("Output_4:")
for i in input_2:
    if i % 2 == 0:
        print("EVEN" , end= " ")
    else:
        print("ODD" , end =" ")
print()