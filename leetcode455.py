class Solution:
    def findContentChildren(self, g, s) -> int:

        
        # Step 1: Sort both arrays (Smallest to Largest)
        g.sort()
        s.sort()
        
        child_i = 0
        cookie_j = 0
        
        # Step 2: Loop until we run out of children OR cookies
        while child_i < len(g) and cookie_j < len(s):
            
            # Step 3: Check if current cookie satisfies current child
            if s[cookie_j] >= g[child_i]:
                # If yes, we can move to the next child (Happy!)
                child_i += 1
            
            # Step 4: Always move to the next cookie.
            # - If we used it, it's gone.
            # - If it was too small, it's useless, so we grab the next bigger one.
            cookie_j += 1
            
        # The index child_i equals the number of children satisfied
        return child_i

object = Solution()
object.findContentChildren(g = [1,2], s = [1,2,3])
