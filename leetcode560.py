class Solution:
    def subarraySum(self, nums, k: int) -> int:

        # The "Notebook": {Running_Sum (Elevation) : Count (How many times seen)}
        # We start at elevation 0, exactly 1 time before any steps are taken.
        notebook = {0: 1}
        
        current_elevation = 0  # This is our running prefix sum
        valid_trails = 0       # This is our answer counter
        
        for step in nums:
            # 1. Take a step and update our current elevation
            current_elevation += step
            
            # 2. What elevation do we need to look for in the past?
            target_elevation = current_elevation - k
            
            # 3. Check the notebook!
            if target_elevation in notebook:
                # We found past elevation(s)! Add the COUNT to our total.
                valid_trails += notebook[target_elevation]
            
            # 4. Write our NEW current elevation into the notebook for the future.
            # .get(key, 0) safely returns 0 if the elevation isn't in the notebook yet, 
            # then we add 1 to record this new visit.
            notebook[current_elevation] = notebook.get(current_elevation, 0) + 1
            
        return valid_trails
object = Solution()
object.subarraySum(nums = [1,1,1], k = 2)
        