You can get the **binary representation** of a number in Python in several ways:

---

### ✅ **1. Using `bin()` function (built-in)**

```python
n = 10
binary = bin(n)          # returns '0b1010'
binary_string = bin(n)[2:]  # remove '0b' prefix
print(binary_string)     # Output: 1010
```

---

### ✅ **2. Using `format()` function**

```python
n = 10
binary = format(n, 'b')  # Output: '1010'
print(binary)
```

---

### ✅ **3. Manual method (using loop)**

```python
def to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

print(to_binary(10))  # Output: 1010
```

---

Let me know if you want to:

* Pad the binary to a fixed width (like 8 bits),
* Handle negative numbers,
* Convert back from binary to decimal.

Great! Let’s walk through **all three** extensions clearly:

---

## ✅ 1. **Pad the binary to a fixed width (e.g., 8 bits)**

You can use `zfill()` or string formatting:

```python
n = 5
binary = format(n, 'b').zfill(8)   # '00000101'
print(binary)
```

Or:

```python
binary = f'{n:08b}'  # fixed width 8, binary format
print(binary)        # Output: 00000101
```

---

## ✅ 2. **Handle negative numbers (Two’s complement representation)**

Python’s `bin()` and `format()` return **signed binary** by default. If you want **two’s complement representation** with fixed bit width:

```python
def twos_complement(n, bits=8):
    if n >= 0:
        return format(n, f'0{bits}b')
    else:
        return format((1 << bits) + n, f'0{bits}b')  # Add 2^bits to wrap around

print(twos_complement(5, 8))     # 00000101
print(twos_complement(-5, 8))    # 11111011
```

> Note: Make sure the number fits within the `bits` range (e.g., for 8 bits: -128 to 127)

---

## ✅ 3. **Convert back from binary to decimal**

For **positive binary strings**:

```python
binary = "1010"
decimal = int(binary, 2)
print(decimal)  # Output: 10
```

For **two’s complement negative numbers**:

```python
def from_twos_complement(binary):
    bits = len(binary)
    n = int(binary, 2)
    if binary[0] == '1':  # negative in two's complement
        n -= 1 << bits
    return n

print(from_twos_complement("11111011"))  # Output: -5
```

---

### 🔁 Full example:

```python
n = -5
bits = 8

# Convert to binary (two's complement)
binary = twos_complement(n, bits)
print("Binary:", binary)

# Convert back
decimal = from_twos_complement(binary)
print("Decimal:", decimal)
```

---

Let me know if you want this packed into a utility module or functions for reuse!
