# ============================================
# DIFFERENT WAYS TO RUN PYTHON CODE
# ============================================

print("=" * 70)
print("YES! You can run Python scripts WITHOUT a main() function")
print("=" * 70)
print()

print("Your current question1.py can be run directly because:")
print("  ✓ It has code at the module level (not inside a function)")
print("  ✓ Python executes the file from top to bottom")
print()

print("=" * 70)
print("METHOD 1: Run directly from terminal")
print("=" * 70)
print()

print("Command:")
print("  python3 question1.py")
print()
print("Or:")
print("  python question1.py")
print()

print("Steps:")
print("  1. Open terminal")
print("  2. Navigate to folder: cd 'HashedIn_practice'")
print("  3. Run: python3 question1.py")
print()

print("=" * 70)
print("METHOD 2: Using if __name__ == '__main__': (Recommended)")
print("=" * 70)
print()

print("Better practice - separate code into functions:")
print()

print('''
def two_sum(nums, target):
    """Function to find two numbers that sum to target"""
    result = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result

if __name__ == '__main__':
    nums = [5, 2, 9, 4]
    target = 7
    result = two_sum(nums, target)
    print(result)
''')

print()
print("Why use if __name__ == '__main__':?")
print("  ✓ Code only runs when script is executed directly")
print("  ✓ Can import functions from this file without running the code")
print("  ✓ Better organization and testing")
print()

print("=" * 70)
print("METHOD 3: Run from IDE/Editor (like VS Code, PyCharm)")
print("=" * 70)
print()

print("In VS Code or other IDEs:")
print("  ✓ Right-click on file → 'Run Python File in Terminal'")
print("  ✓ Click the 'Run' button (▶️)")
print("  ✓ Press F5 to debug/run")
print("  ✓ Press Ctrl+Enter (or Cmd+Enter on Mac) in some editors")
print()

print("=" * 70)
print("METHOD 4: Run in Python Interactive Mode")
print("=" * 70)
print()

print("Step 1: Open Python interactive shell")
print("  python3")
print()
print("Step 2: Import and run")
print("  >>> exec(open('question1.py').read())")
print()

print("Or use import:")
print("  >>> import question1  # Runs the file!")
print()

print("=" * 70)
print("METHOD 5: Run code directly in terminal (one-liner)")
print("=" * 70)
print()

print("Run a single line:")
print('  python3 -c "print(\'Hello World\')"')
print()

print("Run multiple lines:")
print('  python3 -c "nums=[5,2,9,4]; target=7; print([i for i in range(len(nums)) for j in range(i+1, len(nums)) if nums[i]+nums[j]==target])"')
print()

print("=" * 70)
print("METHOD 6: Using Jupyter Notebook / IPython")
print("=" * 70)
print()

print("If you have Jupyter installed:")
print("  jupyter notebook")
print("  # Then create a new notebook and paste your code")
print()

print("Or use IPython:")
print("  ipython")
print("  %run question1.py")
print()

print("=" * 70)
print("YOUR CURRENT CODE ANALYSIS")
print("=" * 70)
print()

print("Your question1.py can run directly because:")
print("  ✓ Code is at module level (not in a function)")
print("  ✓ Python executes it line by line")
print()

print("To run it:")
print("  1. python3 question1.py")
print("  2. Or: cd 'HashedIn_practice' && python3 question1.py")
print()

print("=" * 70)
print("IMPROVEMENT SUGGESTION FOR YOUR CODE")
print("=" * 70)
print()

print("Current code (works but could be better):")
print("-" * 70)
print("""
result = []
nums = [5,2,9,4]
target=7

for i in range(0,len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            result.append(i)
            result.append(j)

print(result)
""")

print()
print("Improved version with function:")
print("-" * 70)
print("""
def two_sum(nums, target):
    result = []
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append(i)
                result.append(j)
    return result

if __name__ == '__main__':
    nums = [5, 2, 9, 4]
    target = 7
    result = two_sum(nums, target)
    print(result)
""")
print()

print("Benefits of improved version:")
print("  ✓ Can reuse the function")
print("  ✓ Can test it easily")
print("  ✓ Can import from other files")
print("  ✓ Better code organization")
print()

print("=" * 70)
print("QUICK REFERENCE")
print("=" * 70)
print()

print("1. Direct run:")
print("   python3 question1.py")
print()

print("2. With full path:")
print("   python3 /path/to/question1.py")
print()

print("3. From different directory:")
print("   python3 HashedIn_practice/question1.py")
print()

print("4. In interactive Python:")
print("   python3")
print("   >>> exec(open('question1.py').read())")
print()

print("5. Make executable (Unix/Mac):")
print("   chmod +x question1.py")
print("   # Add #!/usr/bin/env python3 at top of file")
print("   ./question1.py")
print()






