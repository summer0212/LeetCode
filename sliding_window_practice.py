int_list = [[1,2,3,4], [3,4,5,6], [7,6,5,4], [9,4,1,2]]
# 1 2 3 4 -> 1 2 3, 3 4 5, 7 6 5  -> 2 3 4, 4 5 6, 6 5 4
# 3 4 5 6 -> 3 4 5, 7 6 5, 9 4 1 -> 4 5 6, 6 5 4, 4 1 2
# 7 6 5 4 -> 
# 9 4 1 2

# 00,01,02,03
# 10,11,12,13
# 20,21,22,23

# i=0,j=0 -> [[1,2,3],[3,4,5],[7,6,5]]
# i=1,j=0 -> [[1,2,3],[3,4,5],[7,6,5]]

# i=1,j=1 -> [[]]
# i=0, j=1 -> [[]]

iteration_size = len(int_list) - 2
result = []
max_num_list = []

for i in range(iteration_size ):
    # count += 1
    # print(int_list[i])
    new_list = int_list[i : i + iteration_size + 1]
    max_num_list.append(max(new_list))
    result.append(new_list)

# print(result)
# print(max_num_list)


# ------------- Function to create 3*3 matrix--------------------------------
def matrix_creation(int_list, i, j):
    ans=[]
    matrix_size = 3
    for index in range(i,i+matrix_size):
       row = int_list[index]
       sliced_row = row[j: j+matrix_size]
       ans.append(sliced_row)
    print(ans)  
    return ans
    
i = 1
j = 0
matrix_creation(int_list,i,j)

