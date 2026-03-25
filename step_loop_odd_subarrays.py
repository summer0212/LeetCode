# ============================================
# EXAMPLE: Using Step in For Loop + Extracting Odd-Indexed Subarrays
# ============================================

print("=" * 70)
print("USING STEP IN FOR LOOP")
print("=" * 70)
print()

print("range() with step parameter:")
print("  range(start, stop, step)")
print()

# Basic step examples
print("Example 1: Step of 2 (odd indices)")
print("-" * 70)
arr = [10, 20, 30, 40, 50, 60, 70]

print(f"Array: {arr}")
print("Getting elements at odd indices (1, 3, 5, ...):")
print()

result = []
for i in range(1, len(arr), 2):  # Start at 1, step by 2
    result.append(arr[i])
    print(f"  Index {i}: arr[{i}] = {arr[i]}")

print(f"\nResult: {result}")
print()

print("=" * 70)
print("EXTRACTING SUBARRAYS AT ODD INDICES")
print("=" * 70)
print()

# Extract subarrays starting at odd indices
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original array: {arr2}")

print("\nMethod 1: Extract single elements at odd indices")
print("-" * 70)
odd_elements = []
for i in range(1, len(arr2), 2):
    odd_elements.append(arr2[i])
print(f"Elements at odd indices: {odd_elements}")
print()

print("Method 2: Extract subarrays of length 2 starting at odd indices")
print("-" * 70)
subarrays_odd = []
for i in range(1, len(arr2), 2):
    if i + 1 < len(arr2):  # Make sure we don't go out of bounds
        subarray = arr2[i:i+2]  # Subarray of length 2
        subarrays_odd.append(subarray)
        print(f"  Subarray starting at index {i}: {subarray}")
print(f"All subarrays: {subarrays_odd}")
print()

print("Method 3: Extract subarrays of length 3 starting at odd indices")
print("-" * 70)
subarrays_length3 = []
for i in range(1, len(arr2), 2):
    if i + 3 <= len(arr2):  # Check bounds
        subarray = arr2[i:i+3]
        subarrays_length3.append(subarray)
        print(f"  Subarray at index {i}: {subarray}")
print(f"All subarrays: {subarrays_length3}")
print()

print("=" * 70)
print("SMALL PRACTICAL EXAMPLE")
print("=" * 70)
print()

def extract_odd_subarrays(arr, subarray_length):
    """
    Extract subarrays starting at odd indices (1, 3, 5, ...)
    
    Args:
        arr: Input array
        subarray_length: Length of each subarray to extract
    Returns:
        List of subarrays
    """
    result = []
    
    # Start at index 1, step by 2 (odd indices)
    for i in range(1, len(arr), 2):
        # Check if we can extract subarray of required length
        if i + subarray_length <= len(arr):
            subarray = arr[i:i+subarray_length]
            result.append(subarray)
    
    return result

# Example usage
arr_example = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"Array: {arr_example}")
print()

print("Extract subarrays of length 2 starting at odd indices:")
result1 = extract_odd_subarrays(arr_example, 2)
for idx, subarr in enumerate(result1):
    start_idx = 1 + (idx * 2)  # Calculate original index
    print(f"  Subarray starting at index {start_idx}: {subarr}")
print(f"All: {result1}")
print()

print("Extract subarrays of length 3 starting at odd indices:")
result2 = extract_odd_subarrays(arr_example, 3)
for idx, subarr in enumerate(result2):
    start_idx = 1 + (idx * 2)
    print(f"  Subarray starting at index {start_idx}: {subarr}")
print(f"All: {result2}")
print()

print("=" * 70)
print("DIFFERENT STEP VALUES")
print("=" * 70)
print()

arr3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Array: {arr3}")
print()

print("Step = 2 (every other element starting from index 1):")
for i in range(1, len(arr3), 2):
    print(f"  Index {i}: {arr3[i]}")
print()

print("Step = 3 (every third element starting from index 1):")
for i in range(1, len(arr3), 3):
    print(f"  Index {i}: {arr3[i]}")
print()

print("Step = 2 (even indices: 0, 2, 4, ...):")
for i in range(0, len(arr3), 2):
    print(f"  Index {i}: {arr3[i]}")
print()

print("=" * 70)
print("MINI EXAMPLE - COPY AND USE")
print("=" * 70)
print()

print("Simple example you can copy:")
print("-" * 70)
print()
print("arr = [1, 2, 3, 4, 5, 6, 7, 8]")
print()
print("# Extract elements at odd indices")
print("odd_indices_elements = []")
print("for i in range(1, len(arr), 2):  # Start at 1, step by 2")
print("    odd_indices_elements.append(arr[i])")
print()
print("# Or extract subarrays starting at odd indices")
print("odd_subarrays = []")
print("for i in range(1, len(arr), 2):")
print("    if i + 2 <= len(arr):  # Check bounds")
print("        odd_subarrays.append(arr[i:i+2])  # Subarray of length 2")
print()

# Actually run it
print("Running the example:")
print("-" * 70)
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(f"arr = {arr}")
print()

odd_indices_elements = []
for i in range(1, len(arr), 2):
    odd_indices_elements.append(arr[i])

print("Elements at odd indices:")
print(f"  {odd_indices_elements}")
print()

odd_subarrays = []
for i in range(1, len(arr), 2):
    if i + 2 <= len(arr):
        odd_subarrays.append(arr[i:i+2])

print("Subarrays of length 2 starting at odd indices:")
print(f"  {odd_subarrays}")
print()

print("=" * 70)
print("KEY TAKEAWAYS")
print("=" * 70)
print()

print("1. range(start, stop, step):")
print("   - start: Where to begin (e.g., 1 for odd indices)")
print("   - stop: Where to end (usually len(arr))")
print("   - step: How many to skip (2 for every other)")
print()

print("2. For odd indices: range(1, len(arr), 2)")
print("   - Starts at index 1")
print("   - Steps by 2: 1, 3, 5, 7, ...")
print()

print("3. For even indices: range(0, len(arr), 2)")
print("   - Starts at index 0")
print("   - Steps by 2: 0, 2, 4, 6, ...")
print()

print("4. Extracting subarrays:")
print("   - Use slicing: arr[i:i+length]")
print("   - Always check bounds: i + length <= len(arr)")
print()





