# Lesson 3: **Operators in Python**

## 1. What Are Operators in Python?

**Operators** are special symbols that perform operations on variables and values. They help you manipulate data, perform arithmetic, make comparisons, and work with logical values, among other tasks. Python supports several types of operators, including arithmetic, comparison, logical, assignment, bitwise, and more.

## 2. Types of Operators in Python

### **2.1 Arithmetic Operators**

Arithmetic operators are used to perform basic mathematical operations, such as addition, subtraction, multiplication, and division. Here's a list of arithmetic operators in Python:

| Operator | Description           | Example           |
|----------|-----------------------|-------------------|
| `+`      | Addition              | `3 + 2` → `5`   |
| `-`      | Subtraction           | `5 - 2` → `3`   |
| `*`      | Multiplication        | `4 * 3` → `12`  |
| `/`      | Division              | `10 / 2` → `5.0` |
| `%`      | Modulus (Remainder)   | `7 % 3` → `1`   |
| `**`     | Exponentiation        | `2 ** 3` → `8`  |
| `//`     | Floor Division        | `7 // 2` → `3`  |

### **2.2 Comparison Operators**

Comparison operators are used to compare two values and return a boolean result (`True` or `False`). Here's a list of comparison operators:

| Operator | Description          | Example            |
|----------|----------------------|--------------------|
| `==`     | Equal to             | `5 == 5` → `True` |
| `!=`     | Not equal to         | `5 != 3` → `True` |
| `>`      | Greater than         | `7 > 5` → `True`  |
| `<`      | Less than            | `3 < 6` → `True`  |
| `>=`     | Greater than or equal| `5 >= 5` → `True` |
| `<=`     | Less than or equal   | `4 <= 6` → `True` |

### **2.3 Logical Operators**

Logical operators are used to combine conditional statements. Python provides three logical operators: `and`, `or`, and `not`.

- **`and`**: Returns `True` if both statements are true.
  ```python
  (5 > 2) and (4 < 7)  # True
  ```

- **`or`**: Returns `True` if at least one statement is true.
  ```python
  (5 > 10) or (3 < 7)  # True
  ```

- **`not`**: Returns `True` if the statement is false.
  ```python
  not (5 > 2)  # False
  ```

### **2.4 Assignment Operators**

Assignment operators are used to assign values to variables. Here are some commonly used assignment operators:

| Operator | Description                  | Example          |
|----------|------------------------------|------------------|
| `=`      | Assigns a value              | `x = 5`          |
| `+=`     | Adds and assigns            | `x += 3` (→ `x = x + 3`) |
| `-=`     | Subtracts and assigns       | `x -= 2` (→ `x = x - 2`) |
| `*=`     | Multiplies and assigns      | `x *= 4` (→ `x = x * 4`) |
| `/=`     | Divides and assigns         | `x /= 2` (→ `x = x / 2`) |

### **2.5 Bitwise Operators**

Bitwise operators are used to perform operations on binary numbers. These operators include `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (bitwise left shift), and `>>` (bitwise right shift). They are typically used in low-level programming.

Example:
```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011

# Bitwise AND
result = x & y  # Output: 1 (Binary: 0001)
```

## 3. Examples of Operators in Python

Here are some examples demonstrating the use of different types of operators:

```python
# Arithmetic Operators
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.333...

# Comparison Operators
x = 5
y = 10
print(x > y)   # Output: False
print(x <= y)  # Output: True

# Logical Operators
is_sunny = True
is_weekend = False
print(is_sunny and is_weekend)  # Output: False

# Assignment Operators
num = 5
num += 10
print(num)  # Output: 15

# Bitwise Operators
c = 6  # Binary: 0110
d = 2  # Binary: 0010
print(c | d)  # Output: 6 (Binary: 0110)
```

## 4. Operator Precedence in Python

**Operator precedence** determines the order in which operators are evaluated in expressions. Operators with higher precedence are evaluated first.

For example:

```python
result = 5 + 3 * 2  # Output: 11 (Multiplication is performed before addition)
```

You can use parentheses `()` to explicitly define the order of evaluation:

```python
result = (5 + 3) * 2  # Output: 16 (Addition is performed first)
```

## Exercise

1. Write a Python program that asks the user for two numbers using the method `input()` (wich you can assign to a variable) and prints their sum, difference, product, and quotient.
2. Given three variables `a = 4`, `b = 7`, and `c = 2`, write a Python program that evaluates the expression `a + b * c` and `(a + b) * c`. Observe the difference.
3. Write a Python program that uses logical operators to check if a number is between 10 and 20 (inclusive).
4. Use assignment operators to increase the value of a variable `x` by 10, then multiply it by 3.
5. Write a Python program that performs a bitwise AND operation on two numbers provided by the user.

### **Stuck?**
Check the solution [here](exercise_solution.py)

---

By the end of this lesson, you should have a solid understanding of how to use different types of operators in Python to manipulate data, make comparisons, and control program flow. Keep practicing to gain more confidence!

'''
# Lesson 3: **Operators in Python**

## 1. What Are Operators in Python?

**Operators** are special symbols that perform operations on variables and values. They help you manipulate data, perform arithmetic, make comparisons, and work with logical values, among other tasks. Python supports several types of operators, including arithmetic, comparison, logical, assignment, bitwise, and more.

## 2. Types of Operators in Python

### **2.1 Arithmetic Operators**

Arithmetic operators are used to perform basic mathematical operations, such as addition, subtraction, multiplication, and division. Here's a list of arithmetic operators in Python:

| Operator | Description           | Example           |
|----------|-----------------------|-------------------|
| `+`      | Addition              | `3 + 2` → `5`   |
| `-`      | Subtraction           | `5 - 2` → `3`   |
| `*`      | Multiplication        | `4 * 3` → `12`  |
| `/`      | Division              | `10 / 2` → `5.0` |
| `%`      | Modulus (Remainder)   | `7 % 3` → `1`   |
| `**`     | Exponentiation        | `2 ** 3` → `8`  |
| `//`     | Floor Division        | `7 // 2` → `3`  |

### **2.2 Comparison Operators**

Comparison operators are used to compare two values and return a boolean result (`True` or `False`). Here's a list of comparison operators:

| Operator | Description          | Example            |
|----------|----------------------|--------------------|
| `==`     | Equal to             | `5 == 5` → `True` |
| `!=`     | Not equal to         | `5 != 3` → `True` |
| `>`      | Greater than         | `7 > 5` → `True`  |
| `<`      | Less than            | `3 < 6` → `True`  |
| `>=`     | Greater than or equal| `5 >= 5` → `True` |
| `<=`     | Less than or equal   | `4 <= 6` → `True` |

### **2.3 Logical Operators**

Logical operators are used to combine conditional statements. Python provides three logical operators: `and`, `or`, and `not`.

- **`and`**: Returns `True` if both statements are true.
  ```python
  (5 > 2) and (4 < 7)  # True
  ```

- **`or`**: Returns `True` if at least one statement is true.
  ```python
  (5 > 10) or (3 < 7)  # True
  ```

- **`not`**: Returns `True` if the statement is false.
  ```python
  not (5 > 2)  # False
  ```

### **2.4 Assignment Operators**

Assignment operators are used to assign values to variables. Here are some commonly used assignment operators:

| Operator | Description                  | Example          |
|----------|------------------------------|------------------|
| `=`      | Assigns a value              | `x = 5`          |
| `+=`     | Adds and assigns            | `x += 3` (→ `x = x + 3`) |
| `-=`     | Subtracts and assigns       | `x -= 2` (→ `x = x - 2`) |
| `*=`     | Multiplies and assigns      | `x *= 4` (→ `x = x * 4`) |
| `/=`     | Divides and assigns         | `x /= 2` (→ `x = x / 2`) |

### **2.5 Bitwise Operators**

Bitwise operators are used to perform operations on binary numbers. These operators include `&` (bitwise AND), `|` (bitwise OR), `^` (bitwise XOR), `~` (bitwise NOT), `<<` (bitwise left shift), and `>>` (bitwise right shift). They are typically used in low-level programming.

Example:
```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011

# Bitwise AND
result = x & y  # Output: 1 (Binary: 0001)
```

## 3. Examples of Operators in Python

Here are some examples demonstrating the use of different types of operators:

```python
# Arithmetic Operators
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.333...

# Comparison Operators
x = 5
y = 10
print(x > y)   # Output: False
print(x <= y)  # Output: True

# Logical Operators
is_sunny = True
is_weekend = False
print(is_sunny and is_weekend)  # Output: False

# Assignment Operators
num = 5
num += 10
print(num)  # Output: 15

# Bitwise Operators
c = 6  # Binary: 0110
d = 2  # Binary: 0010
print(c | d)  # Output: 6 (Binary: 0110)
```

## 4. Operator Precedence in Python

**Operator precedence** determines the order in which operators are evaluated in expressions. Operators with higher precedence are evaluated first.

For example:

```python
result = 5 + 3 * 2  # Output: 11 (Multiplication is performed before addition)
```

You can use parentheses `()` to explicitly define the order of evaluation:

```python
result = (5 + 3) * 2  # Output: 16 (Addition is performed first)
```

## Exercise

1. Write a Python program that asks the user for two numbers and prints their sum, difference, product, and quotient.
2. Given three variables `a = 4`, `b = 7`, and `c = 2`, write a Python program that evaluates the expression `a + b * c` and `(a + b) * c`. Observe the difference.
3. Write a Python program that uses logical operators to check if a number is between 10 and 20 (inclusive).
4. Use assignment operators to increase the value of a variable `x` by 10, then multiply it by 3.
5. Write a Python program that performs a bitwise AND operation on two numbers provided by the user.

### **Stuck?**
Check the solution [here](exercise_solution.py)

---

By the end of this lesson, you should have a solid understanding of how to use different types of operators in Python to manipulate data, make comparisons, and control program flow. Keep practicing to gain more confidence!
'''