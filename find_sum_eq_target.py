arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10

result = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):#inside range the first element is from where to start and the second is till where.
        if arr[i] + arr[j] == target:
            result.append((arr[i],arr[j]))
            # Note : result = result.append((arr[i], arr[j])) is that the append() method in Python does not return any value (it returns None)
print(result)
    