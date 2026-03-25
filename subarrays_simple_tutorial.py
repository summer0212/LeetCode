# ============================================
# SIMPLE GUIDE: Creating Subarrays
# ============================================

print("=" * 70)
print("HOW TO CREATE SUBARRAYS - SIMPLE EXPLANATION")
print("=" * 70)
print()

print("Subarray = A portion of an array")
print("Python uses SLICING with square brackets []")
print()

print("=" * 70)
print("BASIC SYNTAX: arr[start:end]")
print("=" * 70)
print()

arr = [10, 20, 30, 40, 50]
print(f"Array: {arr}")
print(f"Indices: {list(range(len(arr)))}")
print()

print("Examples:")
print("-" * 70)
print(f"arr[0:3] = {arr[0:3]}  ← Elements at indices 0, 1, 2")
print(f"arr[1:4] = {arr[1:4]}  ← Elements at indices 1, 2, 3")
print(f"arr[2:5] = {arr[2:5]}  ← Elements at indices 2, 3, 4")
print()

print("KEY POINT: End index is NOT included!")
print("  arr[1:4] gives indices 1, 2, 3 (not 4!)")
print()

print("=" * 70)
print("SHORTCUTS")
print("=" * 70)
print()

arr = [10, 20, 30, 40, 50]
print(f"Array: {arr}")
print()

print("Omit start (starts from beginning):")
print(f"  arr[:3] = {arr[:3]}  ← First 3 elements")
print()

print("Omit end (goes to end):")
print(f"  arr[2:] = {arr[2:]}  ← From index 2 to end")
print()

print("Omit both (copies entire array):")
print(f"  arr[:] = {arr[:]}")
print()

print("=" * 70)
print("CREATING SUBARRAYS OF SPECIFIC LENGTH")
print("=" * 70)
print()

arr = [1, 2, 3, 4, 5, 6, 7]
print(f"Array: {arr}")
print()

print("Subarray of length 3 starting at different positions:")
print("-" * 70)

for start in range(len(arr) - 2):  # Can't start too close to end
    end = start + 3
    subarr = arr[start:end]
    print(f"  arr[{start}:{end}] = arr[{start}:{start+3}] = {subarr}")

print()

print("=" * 70)
print("CREATING ALL SUBARRAYS")
print("=" * 70)
print()

arr = [1, 2, 3, 4]
print(f"Array: {arr}")
print()

print("All possible subarrays:")
print("-" * 70)

all_subarrays = []
for start in range(len(arr)):
    for end in range(start + 1, len(arr) + 1):
        subarr = arr[start:end]
        all_subarrays.append(subarr)
        print(f"  arr[{start}:{end}] = {subarr}")

print(f"\nTotal: {len(all_subarrays)} subarrays")
print()

print("=" * 70)
print("FOR YOUR PROBLEM: ODD LENGTH SUBARRAYS")
print("=" * 70)
print()

arr = [1, 2, 3, 4, 5]
print(f"Array: {arr}")
print()

print("Odd length subarrays (length 1, 3, 5, ...):")
print("-" * 70)

odd_length_subarrays = []
for start in range(len(arr)):
    # Try different lengths: 1, 3, 5, 7, ...
    for length in range(1, len(arr) - start + 1, 2):  # Step by 2 (odd lengths)
        end = start + length
        subarr = arr[start:end]
        odd_length_subarrays.append(subarr)
        print(f"  arr[{start}:{end}] = {subarr}  (length={length})")

print(f"\nAll odd-length subarrays: {odd_length_subarrays}")
print()

print("=" * 70)
print("STEP-BY-STEP FOR YOUR CODE")
print("=" * 70)
print()

arr = [1, 2, 3, 4, 5]
print(f"Array: {arr}")
print()

print("To get all odd-length subarrays:")
print("-" * 70)
print()

print("Step 1: Loop through all starting positions")
print("  for start in range(len(arr)):")
print()

print("Step 2: For each start, try odd lengths: 1, 3, 5, ...")
print("  for length in range(1, len(arr) - start + 1, 2):")
print("      # Step by 2 gives: 1, 3, 5, 7, ...")
print()

print("Step 3: Extract subarray")
print("  subarr = arr[start:start+length]")
print()

print("Let's see it in action:")
print("-" * 70)

for start in range(len(arr)):
    print(f"\nStarting at index {start}:")
    for length in range(1, len(arr) - start + 1, 2):
        end = start + length
        subarr = arr[start:end]
        print(f"  Length {length}: arr[{start}:{end}] = {subarr}")

print()

print("=" * 70)
print("QUICK REFERENCE")
print("=" * 70)
print()

print("Creating subarray:")
print("  subarr = arr[start:end]")
print()
print("Common patterns:")
print("  arr[i:i+3]      → Subarray of length 3 starting at i")
print("  arr[:5]         → First 5 elements")
print("  arr[3:]         → From index 3 to end")
print("  arr[1:4]        → Elements at indices 1, 2, 3")
print()




