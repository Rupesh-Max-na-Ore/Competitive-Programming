# Understanding * and ** in Python

## Unpacking with `*` and `**`

- `*` expands an iterable (like a list, tuple, or dict keys) into positional arguments.
- `**` expands a dictionary into keyword arguments.

---

## Examples

```python
def add(x, y):
    return x + y

nums = {'x': 15, 'y': 20}

# All three give the same output
print(add(nums['x'], nums['y']))
print(add(x=nums['x'], y=nums['y']))
print(add(**nums))  # Unpacks dict as keyword arguments
```
- print(*nums) prints the keys of the dictionary.
- print(**nums) will cause an error:
- TypeError: print() got an unexpected keyword argument 'x'
- This is because print() does not accept arbitrary keyword arguments.

```python
print(nums)      # {'x': 15, 'y': 20}
print(*nums)     # x y (unpacks keys)
```
## Printing Values of a Dictionary
You cannot use print(**nums) directly.
To print the values using **, define a function that accepts keyword arguments:
```python
def show_values(**kwargs):
    print(*kwargs.values())

nums = {'x': 15, 'y': 20}
show_values(**nums)  # Output: 15 20
```
Or, simply print the values directly:
``` python
print(*nums.values())  # Output: 15 20
```



