# Python Fundamentals

This README.md contains the following fundamentals of python programming:
- data types
- math operations
- conditional statements
- for loops
- functions

Here's a helpful resource for beginners in python: https://www.w3schools.com/python/default.asp

---

## Data Types
Variables in python can store different data types. Here are some examples of a few. <br/>
### Basic Data Types
- **int:** integers `a = 6`
- **float:** values with decimals `b = 3.4`
- **bool:** true or false values `happy = True`
- **string:** variables with text `prof = "howard"` or `'prof = 'howard'`

### Lists
store values of any data type `nums = [1, 2, 3, 4]` or `courses = ["MATH 33A", "LS 7C", "CS 31"]`
#### Properties of lists
```
days = ["monday", "tuesday", "wednesday"]

print(days[0])         # lists in python are zero-indexed, output: "monday"
print(len(days))       # len checks length of list, output: 3
print(len(days[1]))    # check length of a specific item in list, output: 7
```

#### Updating Lists
```
days = ["monday", "tuesday", "wednesday"]

days.append("thursday")    # add item to list, days --> ["monday", "tuesday", "wednesday", "thursday"]
days.remove("thursday")    # remove item from list, days --> ["monday", "tuesday", "wednesday"]
days.pop()                 # removes last item from list if no index given, days --> ["monday", "tuesday"]
days[0] = "MONDAY"         # changes value at position 0, days --> ["MONDAY", "tuesday"]
```

### Dictionaries
holds key-value pairs to store and access data
```
grades = {"A": 4, "B": 3, "C": 2}

print(grades["A"])    # returns the value associated with key "A", output: 4
list(grades.keys())   # returns [“A”, “B”, “C”]
list(grades.values()) # returns [4, 3, 2]
list(grades.items())  # returns [(“A”, 4), (“B”, 3),(“C”, 2)]

```

