# ============================================
# SIMPLE EXAMPLE: Step in For Loop + Odd Subarrays
# ============================================

# Simple example - Copy and use this!

arr = [10, 20, 30, 40, 50, 60, 70, 80]

print("Original array:", arr)
print()

# Using step in for loop to get odd-indexed elements
print("Method 1: Extract elements at odd indices (1, 3, 5, ...)")
print("-" * 50)
odd_elements = []
for i in range(1, len(arr), 2):  # Start at 1, step by 2
    odd_elements.append(arr[i])
    print(f"Index {i}: {arr[i]}")

print("Result:", odd_elements)
print()

# Extract subarrays starting at odd indices
print("Method 2: Extract subarrays starting at odd indices")
print("-" * 50)
odd_subarrays = []
for i in range(1, len(arr), 2):  # Start at 1, step by 2
    if i + 2 <= len(arr):  # Check we have enough elements
        subarray = arr[i:i+2]  # Subarray of length 2
        odd_subarrays.append(subarray)
        print(f"Subarray starting at index {i}: {subarray}")

print("All subarrays:", odd_subarrays)
print()

print("=" * 50)
print("QUICK REFERENCE")
print("=" * 50)
print()

print("range(1, len(arr), 2) means:")
print("  - Start at index 1")
print("  - Go up to len(arr)")
print("  - Step by 2 (so: 1, 3, 5, 7, ...)")
print()

print("arr[i:i+2] means:")
print("  - Get elements from index i to i+2 (not including i+2)")
print("  - Creates a subarray of length 2")
print()





