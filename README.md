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
Check out `examples/projects/rpg_game.br` for a complete text-based RPG game showcasing:
- Dictionary-based character stats
- Turn-based combat system
- Inventory management
- Experience and leveling system
- Dynamic enemy scaling

## Language Features
- String concatenation using `fanum_tax`
- Full arithmetic operations
- Comparison operators
- Input/output operations with newline control
- Functions with parameters and dictionary returns
- Conditional statements
- Loops
- Immutable dictionaries
- Variables and scope

## Important Notes
- Each statement must end with a semicolon (;)
- Code blocks are enclosed in curly braces { }
- String literals are enclosed in double quotes
- Comments start with #
- Dictionary keys must be strings
- Dictionaries are immutable - create new ones to update values
- Use `skip` for newlines

## Requirements
- Python 3.6+

## Installation
1. Clone this repository
2. Run your SkibidiLang programs using the Python interpreter:
```bash
python main.py your_program.br
```

## File Extension
SkibidiLang programs use the `.br` file extension.
