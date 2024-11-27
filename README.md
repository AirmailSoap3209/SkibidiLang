# SkibidiLang 

A Gen Alpha-inspired programming language that's bussin fr fr

## Features

### Variable Declaration
```
rizz x = 10  # Declare variable x with value 10
```

### Output
```
skibidi x        # Print variable x
skibidi "rizz"   # Print string
```

### Arithmetic Operations
- Addition: `fanum tax` (e.g., `x fanum tax y`)
- Subtraction: `ohio` (e.g., `x ohio y`)
- Multiplication: `gyatt` (e.g., `x gyatt y`)
- Division: `ratio` (e.g., `x ratio y`)

### Conditionals
```
no cap x greater 5:
    skibidi "big rizz"
```

Comparison operators:
- `greater`: Greater than
- `less`: Less than
- `equals`: Equal to

### Loops
```
ong x less 10:
    skibidi x
    rizz x = x fanum tax 1
```

### Functions
```
bussin add_rizz x y:
    yeet x fanum tax y

rizz result = add_rizz 10 20
```

## Functions in Detail

Functions in SkibidiLang are declared using the `bussin` keyword and can return values using `yeet`. Here's everything you need to know about functions:

### Function Declaration
```
bussin function_name param1 param2:
    # Function body here
```

### Return Values
```
bussin add x y:
    yeet x fanum tax y  # Returns sum of x and y
```

### Function Parameters
- Functions can take any number of parameters
- Parameters are accessible within the function scope
- Parameters can be numbers or variables

### Function Scope
- Functions have their own variable scope
- They can access variables from their parent scope
- Variables declared inside a function are not accessible outside

### Function Calls
```
# Direct call with numbers
rizz result = add_numbers 5 10

# Call with variables
rizz a = 5
rizz b = 10
rizz sum = add_numbers a b

# Call with expressions
rizz result = add_numbers a fanum tax 5 b ohio 2
```

### Example Functions

1. Basic Calculator
```
bussin calc x y:
    rizz sum = x fanum tax y
    rizz diff = x ohio y
    rizz prod = x gyatt y
    rizz quot = x ratio y
    yeet sum
```

2. Nested Function Calls
```
bussin double x:
    yeet x gyatt 2

bussin quadruple x:
    rizz doubled = double x
    yeet double doubled
```

3. Conditional Return
```
bussin check_rizz x:
    no cap x greater 10:
        yeet x gyatt 2  # Double the value if greater than 10
    yeet x             # Otherwise return the original value
```

4. Function with Loop
```
bussin count_to x:
    rizz i = 0
    ong i less x:
        skibidi i
        rizz i = i fanum tax 1
    yeet "done fr fr"
```

### Best Practices
1. Give your functions descriptive names
2. Keep functions focused on a single task
3. Use meaningful parameter names
4. Always include a return value with `yeet`
5. Test functions with different inputs

### Common Errors
- "Function not found fr fr": Function name is misspelled or not defined
- "Function expects different number of args fr fr": Wrong number of parameters
- "Undefined variable fr fr": Trying to use a variable that doesn't exist

## Running SkibidiLang

### Requirements
- Python 3.x

### Usage
1. Run in interactive mode:
```
python skibidi_lang.py
```

2. Execute a SkibidiLang file:
```
python skibidi_lang.py your_file.skibi
```

## Example Program
```
# Calculate sum and product
bussin calc x y:
    rizz sum = x fanum tax y
    rizz prod = x gyatt y
    yeet sum ratio prod

rizz result = calc 10 5
skibidi result

# Loop example
rizz count = 0
ong count less 5:
    skibidi count
    rizz count = count fanum tax 1
```

## Error Handling
The interpreter provides friendly error messages with Gen Alpha flair:
- Division by zero: "Can't ratio by zero fr fr"
- Undefined function: "Function not found fr fr"
- Wrong argument count: "Function expects different number of args fr fr"

## Contributing
Feel free to contribute to make SkibidiLang more bussin fr fr! Create a pull request or open an issue to suggest new features or improvements.

## License
This project is open source and available under the MIT License.
