# Lesson 2: Variables and Data Types

## 1. What Are Variables and What Are They Used For?

1. **Variables** are a way to store data in your computer's memory. They hold values like numbers, text, or more complex data, which you can use and manipulate in your programs.
2. Variables are one of the most useful features in programming because they allow you to store data that you can reuse throughout your program. For example, instead of writing the word "Hi" multiple times, you can store it in a variable and use that variable wherever needed.

## 2. How to Declare a Variable in Python

### Declaring a Normal Variable:

To declare a normal variable in Python, use the following syntax:
```python
name = value
```
For example:
```python
a = "Hello World!"
print(a)
```
#### Explanation:
- `a = "Hello World!"` declares a variable named `a` and stores the text `"Hello World!"` in it.
- `print(a)` displays the content of the variable `a` in the console. The `print()` function is used to output information to the console.

### Declaring a Constant Variable:

To declare a constant variable in Python, use the following syntax:
```python
NAME = value
```
This is similar to declaring a normal variable, but the variable name is written in all uppercase letters. While Python does not enforce constants, using uppercase letters is a convention to indicate that the variable should not be changed.

For example:
```python
TEXT = "Hello World!"
print(TEXT)
```
#### Explanation:
- `TEXT = "Hello World!"` declares a constant variable named `TEXT` and stores the text `"Hello World!"` in it.
- `print(TEXT)` displays the content of the constant variable `TEXT` in the console.

## 3. What Are Data Types and What Are They Used For in Python?

1. **Data Types** are classifications that dictate what a variable or an object can hold and how a computer should interpret its value.
2. Data types inform the Python interpreter how to handle the data and are useful for developers to make their code more understandable by other team members.

## 4. Which Data Types Does Python Accept?

1. **Strings:** Text data type that stores plain text. In Python, you use `str` to refer to them.
   ```python
   greeting = "Hello"
   ```

2. **Integers:** Numeric data type that stores non-decimal numbers. In Python, you use `int` to refer to them.
   ```python
   age = 25
   ```

3. **Floating Point Numbers:** Numeric data type that can contain decimal numbers. In Python, you use `float` to refer to them.
   ```python
   price = 19.99
   ```

4. **Complex Numbers:** Numbers with a real and imaginary part. In Python, you use `complex` to refer to them.
   ```python
   complex_num = 3 + 4j
   ```

5. **Lists:** Mutable sequence data type that can contain any type of variable or object. In Python, you use `list` to refer to them.
   ```python
   items = [1, 2, 3, "Hi", 2.11]
   ```

6. **Tuples:** Immutable sequence data type that can contain any type of variable or object. In Python, you use `tuple` to refer to them.
   ```python
   coordinates = (10.0, 20.0)
   ```

7. **Dictionaries:** Mapping data type that contains key-value pairs. In Python, you use `dict` to refer to them.
   ```python
   person = {"name": "Alice", "age": 25}
   ```

8. **Sets:** Collection data type that cannot contain duplicate elements. In Python, you use `set` to refer to them. Sets have an immutable version called `frozenset`.
   ```python
   unique_numbers = {1, 2, 3, 4}
   ```

9. **Booleans:** Data type that can either be `True` or `False`. In Python, you use `bool` to refer to them.
   ```python
   is_active = True
   ```

10. **Binary Types:** Python includes binary types such as `bytes`, `bytearray`, and `memoryview`, which are used to handle binary data.
    ```python
    byte_data = b"Hello"
    byte_array = bytearray(5)
    memory = memoryview(byte_data)
    ```

11. **NoneType:** Represents the absence of a value. In Python, you use `None` to refer to it.
    ```python
    result = None
    ```

## 5. Python Examples of Each Data Type

```python
# String
greeting = "Hello, World!"
print(greeting)

# Integer
age = 30
print(age)

# Float
price = 19.99
print(price)

# Complex Number
complex_num = 2 + 3j
print(complex_num)

# List
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Tuple
coordinates = (10.0, 20.0)
print(coordinates)

# Dictionary
person = {"name": "Alice", "age": 25}
print(person)

# Set
unique_numbers = {1, 2, 3, 4, 4}
print(unique_numbers)  # Output: {1, 2, 3, 4}

# Boolean
is_active = True
print(is_active)

# Binary Types
byte_data = b"Hello"
print(byte_data)

byte_array = bytearray(5)
print(byte_array)

memory = memoryview(byte_data)
print(memory)

# NoneType
result = None
print(result)
```

## 6. Data Type Conversions in Python

Data type conversions allow you to change the type of a variable to another type. Python provides several functions to perform these conversions:

1. **To Integer:**
   Convert a value to an integer using `int()`.
   ```python
   num_str = "10" # you can  also use  ''
   num_int = int(num_str)
   print(num_int)  # Output: 10
   ```

2. **To Float:**
   Convert a value to a float using `float()`.
   ```python
   num_str = "10.5" # you can also use ''
   num_float = float(num_str)
   print(num_float)  # Output: 10.5
   ```

3. **To String:**
   Convert a value to a string using `str()`.
   ```python
   num = 10
   num_str = str(num)
   print(num_str)  # Output: "10"
   ```

4. **To List:**
   Convert a value to a list using `list()`.
   ```python
   tuple_data = (1, 2, 3)
   list_data = list(tuple_data)
   print(list_data)  # Output: [1, 2, 3]
   ```

5. **To Tuple:**
   Convert a value to a tuple using `tuple()`.
   ```python
   list_data = [1, 2, 3]
   tuple_data = tuple(list_data)
   print(tuple_data)  # Output: (1, 2, 3)
   ```

6. **To Set:**
   Convert a value to a set using `set()`.
   ```python
   list_data = [1, 2, 2, 3]
   set_data = set(list_data)
   print(set_data)  # Output: {1, 2, 3}
   ```

7. **To Boolean:**
   Convert a value to a boolean using `bool()`.
   ```python
   value = 1
   bool_value = bool(value)
   print(bool_value)  # Output: True
   ```

8. **To Complex:**
   Convert real and imaginary parts to a complex number using `complex()`.
   ```python
   real = 2
   imag = 3
   complex_num = complex(real, imag)
   print(complex_num)  # Output: (2+3j)
   ```

Note: Not all data type conversions are possible. Attempting an invalid conversion will result in a `ValueError`.

## Exercise
__Complete the exercise in the project you created for the first exercise__
1. Declare a string variable named "`greeting`" and assign it the value "`Hello, Python!`"
2. Answer this: "What is the data type of the following? `x = 42`" 
    ###### (int, float, str, list, tuple, dict, set, bool)
3. Create a list named "`fruits`" containing "`apple`", "`banana`", "`cherry`"
4. Create a dictionary named `person` with keys `name` and `age`, and values `Alice` and `25`
5. Convert the string `3.14` to a float and assign it to a variable named 'pi'
6. Answer this: "What is the result of the following expression? `5 > 3` and `2 < 4`"
7. Create a set named `unique_numbers` containing the values `1, 2, 3, 3, 4, 5`
8. Convert the `greeting` `string variable` to a `list`
9. Convert the `fruits` `list into` a `set`
10. Try to convert the `person` `dictionary` into a `list` and see what happens
11. Convert the `unique_numbers` `set` to a `list`
12. Print Everything out

### **Stuck?**
Check the soltuion [here](exercise_solution.py)