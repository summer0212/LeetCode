class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float("inf")

        for i in range(0,len(blocks)-k + 1):
            window = blocks[i : i+k]

            current_w_count = window.count('W')

            min_operations = min(min_operations,current_w_count)

        return min_operations
    
object = Solution()
print(object.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
