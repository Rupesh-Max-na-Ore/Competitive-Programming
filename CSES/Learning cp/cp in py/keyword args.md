# What are keyword arguments?

**Keyword arguments** are arguments passed to a function by explicitly specifying the parameter name along with its value, like func(a=1, b=2).
They allow you to assign values to specific parameters, regardless of their position in the function definition.

```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet(name="Alice", age=30)  # name and age are keyword arguments
```

### In summary:
- Keyword arguments use the syntax param=value.
- They improve code readability and allow arguments to be passed in any order.