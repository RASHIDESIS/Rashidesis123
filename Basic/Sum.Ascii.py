list_1 = [[1,2,3],[4,5,6],[7,8,9]]

# char = "a"
# print( "the ascii value of " , char ,"is", ord(char))

rows= len(list_1)
for a in range(rows):
    col_size = len(list_1[rows])
    for col in range(col_size):
        print(list_1[rows][col])