# ============================================
# HOW TO CREATE SUBARRAYS FROM AN ARRAY
# ============================================

print("=" * 70)
print("CREATING SUBARRAYS IN PYTHON")
print("=" * 70)
print()

print("Subarray = A portion of an array")
print("In Python, we use SLICING to create subarrays")
print()

print("=" * 70)
print("BASIC SLICING SYNTAX")
print("=" * 70)
print()

print("Syntax: arr[start:end]")
print("  - start: Index where subarray begins (included)")
print("  - end: Index where subarray ends (NOT included)")
print()

print("Example:")
arr = [10, 20, 30, 40, 50, 60]
print(f"  Original array: {arr}")
print(f"  Indices:        {list(range(len(arr)))}")
print()

subarray1 = arr[1:4]
print(f"  arr[1:4] = {subarray1}")
print(f"  → Elements from index 1 to 3 (4 is not included!)")
print()

print("=" * 70)
print("METHOD 1: Basic Subarray (start to end)")
print("=" * 70)
print()

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Array: {arr}")
print(f"Indices: {list(range(len(arr)))}")
print()

print("Examples:")
print("-" * 70)

# Examples
examples = [
    (0, 3, "First 3 elements"),
    (2, 5, "Elements from index 2 to 4"),
    (5, 10, "Elements from index 5 to 9"),
    (0, len(arr), "Entire array"),
]

for start, end, desc in examples:
    subarr = arr[start:end]
    print(f"  arr[{start}:{end}] = {subarr}  ← {desc}")

print()

print("=" * 70)
print("METHOD 2: Subarray from Start (Omit Start Index)")
print("=" * 70)
print()

arr = [10, 20, 30, 40, 50, 60]
print(f"Array: {arr}")
print()

print("When you omit start, it starts from beginning:")
print("-" * 70)
print(f"  arr[:3] = {arr[:3]}  ← First 3 elements (indices 0, 1, 2)")
print(f"  arr[:4] = {arr[:4]}  ← First 4 elements (indices 0, 1, 2, 3)")
print(f"  arr[:] = {arr[:]}  ← Entire array (copy)")
print()

print("=" * 70)
print("METHOD 3: Subarray to End (Omit End Index)")
print("=" * 70)
print()

arr = [10, 20, 30, 40, 50, 60]
print(f"Array: {arr}")
print()

print("When you omit end, it goes to the end:")
print("-" * 70)
print(f"  arr[2:] = {arr[2:]}  ← From index 2 to end")
print(f"  arr[4:] = {arr[4:]}  ← From index 4 to end")
print(f"  arr[-2:] = {arr[-2:]}  ← Last 2 elements")
print()

print("=" * 70)
print("METHOD 4: Subarray with Step (Skip Elements)")
print("=" * 70)
print()

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Array: {arr}")
print()

print("Syntax: arr[start:end:step]")
print("  - step: How many to skip (e.g., 2 = every other)")
print()

print("Examples:")
print("-" * 70)
print(f"  arr[0:10:2] = {arr[0:10:2]}  ← Every 2nd element (0,2,4,6,8)")
print(f"  arr[1:10:2] = {arr[1:10:2]}  ← Every 2nd from index 1 (1,3,5,7,9)")
print(f"  arr[::2] = {arr[::2]}  ← Every 2nd element (entire array)")
print(f"  arr[::-1] = {arr[::-1]}  ← Reversed array")
print()

print("=" * 70)
print("METHOD 5: Negative Indices (From End)")
print("=" * 70)
print()

arr = [10, 20, 30, 40, 50, 60]
print(f"Array: {arr}")
print(f"Indices:        {list(range(len(arr)))}")
print(f"Negative index: {list(range(-len(arr), 0))}")
print()

print("Negative indices count from the end:")
print("-" * 70)
print(f"  arr[-1] = {arr[-1]}  ← Last element")
print(f"  arr[-2] = {arr[-2]}  ← Second to last")
print(f"  arr[-3:] = {arr[-3:]}  ← Last 3 elements")
print(f"  arr[:-2] = {arr[:-2]}  ← All except last 2")
print()

print("=" * 70)
print("CREATING MULTIPLE SUBARRAYS")
print("=" * 70)
print()

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Array: {arr}")
print()

print("Example: Extract subarrays of length 3:")
print("-" * 70)
subarrays = []
for i in range(len(arr) - 2):  # -2 to avoid out of bounds
    subarr = arr[i:i+3]  # Subarray of length 3
    subarrays.append(subarr)
    print(f"  Subarray starting at index {i}: arr[{i}:{i+3}] = {subarr}")

print(f"\nAll subarrays: {subarrays}")
print()

print("=" * 70)
print("COMMON PATTERNS")
print("=" * 70)
print()

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Array: {arr}")
print()

patterns = [
    ("arr[:5]", "arr[:5]", "First 5 elements"),
    ("arr[5:]", "arr[5:]", "Last 5 elements"),
    ("arr[2:7]", "arr[2:7]", "Middle portion"),
    ("arr[::2]", "arr[::2]", "Every other element"),
    ("arr[1::2]", "arr[1::2]", "Every other starting from index 1"),
    ("arr[::-1]", "arr[::-1]", "Reversed array"),
    ("arr[1:-1]", "arr[1:-1]", "All except first and last"),
]

print("Common subarray patterns:")
print("-" * 70)
for pattern, code, desc in patterns:
    result = eval(code)
    print(f"  {code:15} = {result:30} ← {desc}")

print()

print("=" * 70)
print("STEP-BY-STEP: BUILDING SUBARRAYS")
print("=" * 70)
print()

arr = [10, 20, 30, 40, 50, 60, 70]
print(f"Original array: {arr}")
print()

print("Let's create different subarrays:")
print("-" * 70)

# Step 1: First few elements
print("1. First 3 elements:")
print(f"   arr[0:3] = {arr[0:3]}")
print(f"   or arr[:3] = {arr[:3]}")
print()

# Step 2: Last few elements
print("2. Last 3 elements:")
print(f"   arr[-3:] = {arr[-3:]}")
print(f"   or arr[4:] = {arr[4:]}")
print()

# Step 3: Middle elements
print("3. Middle elements (indices 2 to 4):")
print(f"   arr[2:5] = {arr[2:5]}")
print()

# Step 4: Every other element
print("4. Every other element:")
print(f"   arr[::2] = {arr[::2]}")
print()

# Step 5: Specific range
print("5. Elements from index 1 to 5:")
print(f"   arr[1:6] = {arr[1:6]}")
print()

print("=" * 70)
print("IMPORTANT NOTES")
print("=" * 70)
print()

print("1. End index is NOT included:")
print("   arr[1:4] gives elements at indices 1, 2, 3")
print("   Index 4 is NOT included!")
print()

print("2. Slicing doesn't modify original array:")
print("   subarr = arr[1:4] creates a NEW list")
print("   Original array stays unchanged")
print()

print("3. Out of bounds is handled gracefully:")
print("   arr[1:100] will just give arr[1:]")
print("   No error, just returns what's available")
print()

print("4. Empty subarray if start >= end:")
print("   arr[3:1] = []  (empty list)")
print()

print("=" * 70)
print("PRACTICAL EXAMPLE: Extract All Possible Subarrays")
print("=" * 70)
print()

def get_all_subarrays(arr):
    """Get all possible subarrays of an array"""
    subarrays = []
    n = len(arr)
    
    # Try all possible starting positions
    for start in range(n):
        # Try all possible ending positions
        for end in range(start + 1, n + 1):
            subarr = arr[start:end]
            subarrays.append(subarr)
    
    return subarrays

arr_example = [1, 2, 3]
print(f"Array: {arr_example}")
print()

all_subarrays = get_all_subarrays(arr_example)
print("All possible subarrays:")
for subarr in all_subarrays:
    print(f"  {subarr}")

print(f"\nTotal: {len(all_subarrays)} subarrays")
print()

print("=" * 70)
print("QUICK REFERENCE CARD")
print("=" * 70)
print()

print("Basic Syntax:")
print("  arr[start:end]        → Elements from start to end-1")
print("  arr[start:]           → From start to end")
print("  arr[:end]             → From beginning to end-1")
print("  arr[:]                → Copy entire array")
print()
print("With Step:")
print("  arr[start:end:step]   → With step size")
print("  arr[::2]              → Every 2nd element")
print("  arr[::-1]             → Reversed")
print()
print("Negative Indices:")
print("  arr[-1]               → Last element")
print("  arr[-3:]              → Last 3 elements")
print("  arr[:-2]              → All except last 2")
print()

print("=" * 70)
print("PRACTICE EXERCISES")
print("=" * 70)
print()

arr_practice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Practice with: {arr_practice}")
print()

exercises = [
    ("First 4 elements", "arr_practice[:4]"),
    ("Last 3 elements", "arr_practice[-3:]"),
    ("Middle 3 elements (indices 3-5)", "arr_practice[3:6]"),
    ("Every other element", "arr_practice[::2]"),
    ("Elements from index 2 to 8", "arr_practice[2:9]"),
    ("All except first and last", "arr_practice[1:-1]"),
    ("Reversed array", "arr_practice[::-1]"),
]

print("Try to guess the result:")
print("-" * 70)
for desc, code in exercises:
    result = eval(code)
    print(f"  {desc:35} → {result}")

print()




