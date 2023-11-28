
list_1 = [[1,2,3],[4,5,6],[7,8,9]]
print(len(list_1[2]))

print((list_1[2]))

# for i in range(5):
#     for j in range(5):
#         print(i,j)


# num_of_rows = len(list_1)

# for row in range(num_of_rows):
#      col_size = len(list_1[row])
#      for col in range(col_size):
#         print(list_1[row][col])

for row in list_1:
    for col in row:
        print(col)


