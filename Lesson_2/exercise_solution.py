# NOTE: This is the exercise solution for lesson 2, watch this only if you get stuck


greeting = "Hello, Python!" # or greeting = 'Hello, Python!'
# x = 42 is an Integer Data Type (int)
fruits = ["apple", "banana", "cherry"] # or fruits = ('apple', 'banana', 'cherry')
person = {"name": "Alice", "age": 25} # or person = dict(name="Alice", age=25)  # or person = dict({"name": "Alice", "age": 25}) or person = {'name': 'Alice', 'age': 25}
pi = float(3.14)
# 5 > 3 is True    
# 2 < 4 is False
unique_numbers = {1, 2, 3, 4, 5} # or unique_numbers = set([1, 2, 3, 4, 5])ù

print(greeting)
print(fruits)
print(person)
print(pi)
print(unique_numbers)

greeting = list(greeting)
fruits = set(fruits)
person = list(person) # Correct way = person = list(person.items())
unique_numbers = list(unique_numbers)

print(greeting)
print(fruits)
print(person)
print(pi)
print(unique_numbers)
