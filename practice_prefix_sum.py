arr = [-2, 0, 3, -5, 2, -1]
n = len(arr)

prefix_arr = [0] * n
prefix_arr[0] = arr[0]

for i in range(1,n):
    prefix_arr[i] = prefix_arr[i-1] + arr[i]

print(prefix_arr)
