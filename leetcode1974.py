class Solution:
    def minTimeToType(self, word: str) -> int:
        seconds = 0
        current ='a'

        for target in word:
            diff = abs(ord(target) - ord(current))
            move_time = min(diff, 26 - diff)

            seconds += move_time + 1

            current = target

        return seconds
    
object = Solution()
print(object.minTimeToType(word = "ahx"))