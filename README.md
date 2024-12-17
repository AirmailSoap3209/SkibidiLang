# SkibidiLang (formerly BrainRot)

SkibidiLang is a modern programming language that uses internet slang and memes as its syntax. It's designed to be fun while maintaining the functionality of a traditional programming language.

## Keywords

```
# Printing and I/O
skibidi         -> print
whats_up_unc    -> input
skip            -> newline

# Variables and Functions
rizz            -> variable declaration
bussin          -> function definition
yeet            -> return

# Control Flow
no_cap          -> if
ong             -> while
fr_fr           -> true
cap             -> false

# Arithmetic
fanum_tax       -> addition (+)
ohio            -> subtraction (-)
gyatt           -> multiplication (*)
ratio           -> division (/)

# Comparisons
alpha           -> greater than (>)
beta            -> less than (<)
sigma           -> equals (==)
```

## Data Structures

### Dictionaries
```
# Creating a dictionary
rizz stats = {
    "health": 100,
    "attack": 10,
    "defense": 5
};

# Accessing dictionary values
rizz health = stats["health"];

# Note: Dictionaries are immutable!
# Create a new dictionary to update values:
rizz new_stats = {
    "health": stats["health"] ohio 10,
    "attack": stats["attack"],
    "defense": stats["defense"]
};
```

## Example Programs

### Hello World
```
skibidi "Hello, World!" fanum_tax skip;
```

### Variable Declaration and Arithmetic
```
rizz x = 10;
rizz y = 20;
rizz z = x fanum_tax y;  # z = 30
skibidi z fanum_tax skip;
```

### Functions with Dictionary Return
```
bussin add(x, y) {
    yeet x fanum_tax y;
}

rizz result = add(5, 3);
skibidi result;  # Prints 8
```

### Control Flow with Boolean Values
```
rizz game_over = 0;  # cap (false)

ong game_over sigma 0 {
    skibidi "Game is running" fanum_tax skip;
    rizz choice = whats_up_unc;
    
    no_cap choice sigma "quit" {
        rizz game_over = 1;  # fr_fr (true)
    };
}
```

## Featured Project: RPG Game
Check out `examples/projects/betterrpg_game.br` for a complete text-based RPG game showcasing:
- Dictionary-based character stats
- Turn-based combat system
- Inventory management
- Experience and leveling system
- Dynamic enemy scaling

## Language Features
### Core Features
- Meme-inspired syntax that makes programming fun and memorable
- Strong type system with numbers and strings
- Rich set of arithmetic operations with memorable keywords
- Clean and intuitive comparison operators
- Powerful string manipulation with concatenation

### Programming Constructs
- Function definitions with parameter support and return values
- Conditional statements (if/else) using `no_cap`
- Loop structures with `ong` for iteration
- Scope management with block-based structure

### Data Management
- Dictionary-based data structures for complex data
- Immutable design promoting clean data flow
- String-based dictionary keys for clarity
- Built-in type conversion and handling

### Input/Output
- Console-based input with `whats_up_unc`
- Formatted output with `skibidi`
- Newline control using `skip`
- Clean string formatting capabilities

### Project Support
- Modular code organization
- Clear file extension (.br) for easy recognition
- Support for large projects (see betterrpg_game and math_wizard example)
- Comprehensive error messages

## Important Notes ***
### Syntax Requirements **
- All statements must end with semicolon (;)
- Code blocks require curly braces { }
- Strings must use double quotes "text"
- Comments begin with # symbol
- Proper spacing around operators is required

### Dictionary Rules *
- All dictionary keys must be strings
- Dictionaries are immutable by design
- Create new dictionaries to update values
- Access values using square bracket notation ["key"]

### Best Practices *
- Use descriptive variable names
- Maintain consistent indentation
- Comment complex logic
- Break down complex operations into smaller functions
- Handle errors appropriately

### Common Pitfalls ***
- Remember to use semicolons at end of statements
- Don't try to modify dictionaries directly
- Ensure proper string formatting in dictionary keys
- Watch for proper operator spacing

## Requirements
- Python 3.6+

## Installation **
1. Clone this repository
2. Run your SkibidiLang programs using the Python interpreter:
```bash
python main.py your_program.br
```

## File Extension
SkibidiLang programs use the `.br` file extension.
