from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Step 1: Create a dictionary where every new key gets an empty list[] automatically
        grouped = defaultdict(list)

        for word in strs:
            # Step 2: Sort the word to get its "signature" (the Key)
            # Example: "tea" becomes "aet"
            sorted_word = "".join(sorted(word))
            
            # Step 3: Append the ORIGINAL word to the list for this signature
            # If "aet" isn't in the dict yet, defaultdict creates [] first, then appends.
            grouped[sorted_word].append(word)
            
        # Let's print the dictionary so you can see the magic:
        print("Our Dictionary:", dict(grouped))
        
        # Step 4: Extract just the values (the lists of anagrams) and return them
        return list(grouped.values())

# Testing
object = Solution()
print(object.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
        

'''Note :- You have done a fantastic job identifying the core logic: Anagrams look exactly the same when you sort them.
You are stuck because of how you designed your dictionary. Let's look at what your current dictionary looks like:
{"eat": "aet", "tea": "aet", "tan": "ant"}
The Roadblock:
    Your dictionary maps Original Word -> Sorted Word.
    To group them, you are trying to say: "Find all keys that have the value 'aet'."
    Dictionaries are not designed to be searched by Value. They are designed to be searched by Key. Trying to group them this way requires messy, slow, nested loops.

The "Aha!" Fix: Flip the Dictionary
    Instead of mapping Original -> Sorted, we need to map Sorted -> List of Originals.
    If we do it this way, the dictionary will look like this:
    {"aet":["eat", "tea", "ate"], "ant": ["tan", "nat"]}
    This is exactly where defaultdict(list) becomes your best friend!
Step-by-Step Implementation
    Initialize defaultdict(list): This creates a dictionary where if a key doesn't exist yet, it automatically creates an empty list [] for it.
    Loop through the words: Sort each word to find its "signature" (e.g., "aet").
    Append: Put the original word into the list belonging to that signature.
    Return the values: We only want the grouped lists, not the sorted keys. We can just extract .values().



anagram_dict["".join(sorted(char))] = char #{'aet': 'ate', 'ant': 'nat', 'abt': 'bat'}
'''