# How to Change Directory in Terminal

## Basic Command: `cd` (Change Directory)

### Navigate into a folder:
```bash
cd folder_name
```

### Navigate back out (to parent directory):
```bash
cd ..
```

### Go to home directory:
```bash
cd ~
```
or simply:
```bash
cd
```

---

## Examples for Your Project

### Your current workspace structure:
```
python_dsa/
  ├── stack_easy/
  │   └── leetcode2160.py
  ├── HashedIn_practice/
  └── other files...
```

### Navigate into `stack_easy` folder:
```bash
cd stack_easy
```

### Navigate into `HashedIn_practice` folder:
```bash
cd HashedIn_practice
```

### If folder name has spaces, use quotes:
```bash
cd "HashedIn practice"
```
or escape with backslash:
```bash
cd HashedIn\ practice
```

---

## Common Commands

### Go to specific folder (absolute path):
```bash
cd /Users/alisha/workspace/python_dsa/stack_easy
```

### Go to parent directory (one level up):
```bash
cd ..
```

### Go up multiple levels:
```bash
cd ../..  # Goes up 2 levels
```

### Go to previous directory:
```bash
cd -
```

### See current directory:
```bash
pwd
```

---

## Step-by-Step Example

### Example: Navigate from python_dsa to stack_easy

```bash
# Step 1: Check current directory
pwd
# Output: /Users/alisha/workspace/python_dsa

# Step 2: List files/folders
ls
# You'll see: stack_easy, HashedIn_practice, etc.

# Step 3: Navigate into stack_easy
cd stack_easy

# Step 4: Verify you're inside
pwd
# Output: /Users/alisha/workspace/python_dsa/stack_easy

# Step 5: List files inside
ls
# You'll see: leetcode2160.py, etc.
```

### To go back:
```bash
cd ..
pwd
# Output: /Users/alisha/workspace/python_dsa
```

---

## Quick Reference

| Command | What it does |
|---------|-------------|
| `cd folder_name` | Go into folder |
| `cd ..` | Go back one level |
| `cd ~` | Go to home directory |
| `cd /` | Go to root directory |
| `cd -` | Go to previous directory |
| `pwd` | Show current directory |
| `ls` | List files/folders in current directory |

---

## Tips

1. **Use Tab completion**: Type `cd sta` and press Tab to auto-complete `stack_easy`

2. **Spaces in names**: Use quotes `cd "folder name"` or escape `cd folder\ name`

3. **Relative vs Absolute paths**:
   - Relative: `cd stack_easy` (from current location)
   - Absolute: `cd /Users/alisha/workspace/python_dsa/stack_easy`

4. **Check if you're in the right place**: Always use `pwd` and `ls` to verify



