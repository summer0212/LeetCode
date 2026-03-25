class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n):
            for b in range(1, n):
                mul = (a*a) + (b*b)
                print("a:", a, "b:", b, "mul:", mul)
                square_root = mul ** 0.5
                # Check if square_root is a perfect square and within range
                if square_root.is_integer() and square_root <= n:
                    count += 1
        return count  
    
obj = Solution()
print(obj.countTriples(5))  # Output: 4