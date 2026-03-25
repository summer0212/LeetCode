'''Next Greater Element to the Right — Given array arr, for each index find the next greater element to its right (or -1).'''

def nextLargestElement(arr):
    result = [-1] * len(arr)
    print(result)

    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break
            # else :
            #     result.append(-1)

    return result









if __name__ == "__main__":
    arr = [6,8,0,1,3]
    result = nextLargestElement(arr)
    print(result)