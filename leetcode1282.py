from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes) :
        #BRUTE FORCE METHOD
        dict = defaultdict(list)
        result = []
        
        for i in range(0,len(groupSizes)):
            if groupSizes[i] not in dict:
                dict[groupSizes[i]].append(i)
            else:
                dict[groupSizes[i]].append(i)
                
        for key,values in dict.items():
            for i in range(0,len(values),key):
                result.append(values[i:i+key])
                
                
        print(result)
        return result

object = Solution()
print(object.groupThePeople(groupSizes = [3,3,3,3,3,1,3]))




'''Advance method suggested by AI:
# A dictionary to act as our "Buckets"
# Key = Group Size, Value = List of people waiting
buckets = defaultdict(list)
# print(buckets)
result = []

# Iterate through every person. 
# Enumerate gives us both the person's ID and their group size. T
# hat means the index and value from an iterable.
for person_id, size in enumerate(groupSizes):
    
    # 1. Put the person in the correct bucket
    buckets[size].append(person_id)
    
    # 2. Check if the bucket is full
    if len(buckets[size]) == size:
        # The group is full! Add it to results.
        result.append(buckets[size])
        
        # Empty the bucket for the next group of this size
        buckets[size] = []
        
return result'''

