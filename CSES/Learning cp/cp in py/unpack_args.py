def add(x,y):
    return x + y

nums = {'x':15, 'y':20}
# Below 3 give same output
print(add(nums['x'],nums['y']))
print(add(x=nums['x'], y=nums['y']))
print(add(**nums))

# To understand
print(nums) # {'x': 15, 'y': 20}
# unpack keys
print(*nums) # x y
# Unpacks dictionaries into keyword arguments
# print(**nums) # TypeError: print() got an unexpected keyword argument 'x'

# print(**d) will cause an error, because print() does not accept x and y as keyword arguments.

print(list(**nums))
"""
* → expands an iterable into positional arguments.
** → expands a dict into keyword arguments.

To print the values of a dictionary using **, you can define a function that accepts keyword arguments, then print the values inside that function

Or, simply print the values directly:
"""

def show_values(**kwargs):
    print(*kwargs.values())

nums = {'x': 15, 'y': 20}
show_values(**nums)  # Output: 15 20

print(*nums.values())  # Output: 15 20

