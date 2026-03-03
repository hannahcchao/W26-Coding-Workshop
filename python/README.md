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
Lists store values of any data type using square brackets: `nums = [1, 2, 3, 4]` or `courses = ["MATH 33A", "LS 7C", "CS 31"]`
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
Dictionaries hold key-value pairs to store and access data
```
grades = {"A": 4, "B": 3, "C": 2}

print(grades["A"])    # returns the value associated with key "A", output: 4
list(grades.keys())   # returns [“A”, “B”, “C”]
list(grades.values()) # returns [4, 3, 2]
list(grades.items())  # returns [(“A”, 4), (“B”, 3),(“C”, 2)]

```

## Math Operations
Basic math operations can be done in python using keyboard symbols. More advanced operations can be done using python math packages.
```
a = 3
b = 5

sum = a + b                # sum has value 8
difference = b - a         # difference has value 2
produce = a * b            # product has valuel 15
quotient = b/a             # quotient has the value 1.66667 (float)
integer_quotient = b // a  #integer_quotient has the value 1 (int)

c = 2
d = 3

power = c**d     # power has value 8
root = c**0.5    # root has the value √2 (taking square root without math.sqrt function)
modulo = d % c   # modulo has value 1 (remainder of 3/2)
n = 4 * (c + d)  # n has value 20

```

## Conditional Statements
Conditional statements execute a specific task when certain conditions are met. Here are some examples:
```
if score > 100 or score < 0:
  print(“Hmmm…”)
elif score > 75:
  print(“You passed!”)
else:
  print(“Lock in”)
```

Let's use boolean variables to demonstrate:
```
a = True
b = False

a or b  # True
b or b  # False
a and b # False
a and a # True
```

## For Loops
For loops can be used to iterate through items in a sequence. Here's some examples:
```
professor = “howard” 
for character in professor: 
  print(character.upper(), end=””)  # will output “HOWARD”

days = [“monday”, “tuesday”, “wednesday”]
for day in days:
  print(day[0], end=” ”)   # will output “m t w ”

for i in range(len(days)):
  print(days[i][i], end = “ ”)  # will output “m u d ”, range returns a sequence of integers from 0 to 3 [0,3), i will go from 0 → 1 → 2

grades = {“A”: 4, “B”: 3, “C”: 2}
for key, value in grades.items():
  print(f”{key}{value}”, end=” ”)  # will output “A4 B3 C2”

```

## Functions
Functions take in some input and return an output. They can be reused throughout code to perform a specific task.
```
# no input, no (function) output 
def main():
  print(“hello world”)

# takes input, returns output
def hypotenuse(a, b):
  return (a ** 2 + b ** 2) ** 0.5

hypotenuse(3,4) # calls hypotenuse function
```
---
Now that we've gone over some python fundamentals, let's work on an activity! Choose one of the following exercises to add to your branch: <br/>
- **Function Writing:** Write a function that returns the average string length of all the strings in the list.
- **DNA sequence:** Given the string `dna = "ATCTGATTACCGGGAC"`, count the number of each nucleotide present
- **Grade calculator:** Use a dictionary to store how much each component of your grade is worth, and calculate your grade in a class based on input to a function

