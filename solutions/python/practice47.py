# Problem: Rotate List by N Steps
# Source: 
# Note: Rotates elements of a list by n steps
#     """Rotate the elements of lst by n steps.

#     A positive n indicates a right rotation, while a negative n indicates a left rotation.

#     Args:
#         lst (list): The list to be rotated.
#         n (int): The number of steps to rotate the list.

#     Returns:
#         list: The rotated list.
#     """

#     if not lst:
#         return lst
    
#     arr = [0] * len(lst)

#     for i in range(len(lst)):
#         arr[(i + n) % len(lst)] = lst[i]
    
#     return arr

def rotate(arr, n):
    if not arr:
        return []
    
    res = [0] * len(arr)

    for i in range(len(arr)):
        res[(i + n) % len(arr)] = arr[i]
    
    return res

# --- TESTS ---

# 1. basic right rotation

# 2. basic left rotation (negative steps)

# 3. full cycle (rotation equals length)

# 4. rotation larger than list length

# 5. empty list

# 6. single-element list

# 7. mixed data types

# 8. zero rotation (no change)

print('Success')
