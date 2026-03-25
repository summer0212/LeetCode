

def canPlaceFlowers(flowerbed, n) -> bool:
    flag = 0
    for i in range(n):
        for j in range(len(flowerbed)):
            if flowerbed[j] == 1:
                continue
            elif flowerbed[j-1] == 0 and flowerbed[j+1] == 0:
                flowerbed[j] = 1
                flag += 1
            elif flowerbed[j] == 0 and flowerbed[j+1] == 0:
                    flowerbed[j] = 1
                    flag += 1
    if flag == n:
        return True
    else:
        return False


flowerbed = [1,0,0,0,1]
n = 1
output = canPlaceFlowers(flowerbed, n)
print(output)