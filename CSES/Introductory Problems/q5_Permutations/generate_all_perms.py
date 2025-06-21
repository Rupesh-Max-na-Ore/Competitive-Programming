def permute(nums):
    result = []
    
    def backtrack(start):
        # If we've reached the end, add a copy of the current permutation
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            # Swap the current element with the start
            nums[start], nums[i] = nums[i], nums[start]
            
            # Recurse on the next position
            backtrack(start + 1)
            
            # Backtrack (undo the swap)
            nums[start], nums[i] = nums[i], nums[start]
    
    backtrack(0)
    return result

# Example usage:
lst = [1, 2, 3]
perms = permute(lst)
for p in perms:
    print(p)
