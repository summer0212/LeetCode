# ============================================
# EXPLAINING THE PROBLEM WITH index() AND DUPLICATES
# ============================================

print("=" * 70)
print("PROBLEM: Why words.index(word) gives wrong answer with duplicates")
print("=" * 70)
print()

# Your test case
words = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
x = "a"

print("Input words list:")
for i, word in enumerate(words):
    print(f"  Index {i}: '{word[:10]}...' (all are identical)")
print()

print("=" * 70)
print("THE PROBLEM: How index() works")
print("=" * 70)
print()

print("words.index(word) returns the INDEX OF THE FIRST OCCURRENCE")
print()

print("What happens in your loop:")
print("-" * 70)

# Simulating the broken code
result_broken = []
for word in words:
    idx = words.index(word)
    result_broken.append(idx)
    print(f"Processing word at position {len(result_broken)-1}: '{word[:10]}...'")
    print(f"  words.index(word) = {idx}  ← Always returns 0 (first occurrence)!")
    print()

print("Result:", result_broken)
print()

print("=" * 70)
print("WHY THIS HAPPENS:")
print("=" * 70)
print()

print("When Python sees:")
print("  words.index('aaaaaaaaaaaaaaaa...')")
print()
print("It searches from the START of the list and returns the FIRST match.")
print("Since all words are identical, it ALWAYS finds the first one at index 0.")
print()

print("=" * 70)
print("SOLUTION 1: Use enumerate() to get index directly")
print("=" * 70)
print()

result_correct = []
for i, word in enumerate(words):
    if x in word:
        result_correct.append(i)
        print(f"Index {i}: Found '{x}' in word → append({i})")

print()
print("Result:", result_correct)
print()

print("=" * 70)
print("SOLUTION 2: Use range() with len()")
print("=" * 70)
print()

result_correct2 = []
for i in range(len(words)):
    if x in words[i]:
        result_correct2.append(i)
        print(f"Index {i}: Found '{x}' in words[{i}] → append({i})")

print()
print("Result:", result_correct2)
print()

print("=" * 70)
print("COMPARISON")
print("=" * 70)
print()

print("Your code (WRONG):")
print("  for word in words:")
print("      result.append(words.index(word))  ← Always returns first match!")
print(f"  Result: {result_broken}")
print()

print("Correct code (Option 1):")
print("  for i, word in enumerate(words):")
print("      result.append(i)  ← Gets actual current index")
print(f"  Result: {result_correct}")
print()

print("Correct code (Option 2):")
print("  for i in range(len(words)):")
print("      result.append(i)  ← Uses loop counter as index")
print(f"  Result: {result_correct2}")
print()

print("=" * 70)
print("EXAMPLE WITH DIFFERENT DUPLICATES")
print("=" * 70)
print()

test_words = ["apple", "banana", "apple", "cherry", "apple"]
print("words =", test_words)
print()

print("Using words.index(word) (WRONG):")
result_wrong = []
for word in test_words:
    idx = words.index(word) if word in words else -1  # For demo
    print(f"  word='{word}' → words.index('{word}') = {test_words.index(word)}")
    result_wrong.append(test_words.index(word))

print(f"  Result: {result_wrong}  ← WRONG! Should be [0,1,2,3,4]")
print()

print("Using enumerate() (CORRECT):")
result_right = []
for i, word in enumerate(test_words):
    print(f"  Index {i}: word='{word}' → append({i})")
    result_right.append(i)

print(f"  Result: {result_right}  ← CORRECT!")
print()

print("=" * 70)
print("KEY TAKEAWAY")
print("=" * 70)
print()
print("❌ words.index(word) → Returns FIRST occurrence, not current position")
print("✅ enumerate(words)  → Returns (index, value) pair - gives actual position")
print("✅ range(len(words)) → Use loop counter as index")
print()






