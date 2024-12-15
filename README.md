# SkibidiLang (formerly BrainRot)

**SkibidiLang** is a modern, meme-inspired programming language that brings internet slang and humor into coding. It’s designed to make programming enjoyable while retaining the functionality of traditional programming languages. Whether you’re creating fun projects or learning to code, SkibidiLang offers a unique experience.

---

## Features at a Glance

- **Robust Programming Constructs**: Includes loops, conditionals, and functions.
- **Powerful Data Management**: Work with immutable dictionaries and type-safe structures.
- **Console I/O**: Easily handle input and output with keywords like `whats_up_unc`.
- **Project-Ready**: Build modular, scalable applications with `.br` files.

---

## SkibidiLang Syntax

### Keywords Overview


| **Category**            | **SkibidiLang Keyword** | **Traditional Equivalent** | **Syntax Example**                                                                                                                                                                      |
| ----------------------- | ----------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Printing/I/O**        | `skibidi`               | `print`                    | `skibidi "Hello, world!" fanum_tax skip;`                                                                                                                                                 |
|                         | `whats_up_unc`          | `input`                    | `rizz name = whats_up_unc "Enter your name: ";`                                                                                                                                           |
|                         | `skip`                  | `newline`                  | `skibidi skip;`                                                                                                                                                                          |
| **Variables/Functions** | `rizz`                  | `variable declaration`     | `rizz x = 5;`                                                                                                                                                                            |
|                         | `bussin`                | `function definition`      | `bussin add(x, y) { rizz sum = x fanum_tax y; yeet sum; };`                                                                                                                            |
|                         | `yeet`                  | `return`                   | `yeet result;`                                                                                                                                                                           |
| **Control Flow**        | `no_cap`                | `if`                       | `no_cap x alpha 0 { skibidi "x is positive"; };`                                                                                                                                         |
|                         | `ong`                   | `while`                    | `ong x alpha 5 { skibidi x; x = x fanum_tax 1; };`                                                                                                                                      |
|                         | `fr_fr`                 | `true`                     | `no_cap x fr_fr { skibidi "x is true"; };`                                                                                                                                               |
|                         | `cap`                   | `false`                    | `no_cap x cap { skibidi "x is false"; };`                                                                                                                                               |
| **Arithmetic**          | `fanum_tax`             | `+`                        | `rizz result = x fanum_tax y;`                                                                                                                                                           |
|                         | `ohio`                  | `-`                        | `rizz difference = x ohio y;`                                                                                                                                                           |
|                         | `gyatt`                 | `*`                        | `rizz product = x gyatt y;`                                                                                                                                                             |
|                         | `ratio`                 | `/`                        | `rizz quotient = x ratio y;`                                                                                                                                                            |
| **Comparisons**         | `alpha`                 | `>`                        | `no_cap x alpha y { skibidi "x is greater than y"; };`                                                                                                                                    |
|                         | `beta`                  | `<`                        | `no_cap x beta y { skibidi "x is less than y"; };`                                                                                                                                       |
|                         | `sigma`                 | `==`                       | `no_cap x sigma y { skibidi "x is equal to y"; };`                                                                                                                                       |
| **Random Functions**    | `goofy_ahh`             | `random float`             | `rizz basic_random = goofy_ahh(); skibidi "Random float (0-1): " fanum_tax basic_random fanum_tax skip;`                                                                                   |
|                         | `goofy_ahh_int`         | `random integer`           | `rizz dice_roll = goofy_ahh_int(1, 6); skibidi "Dice roll (1-6): " fanum_tax dice_roll fanum_tax skip;`                                                                                   |
|                         | `goofy_ahh_choice`      | `random choice from list`  | `rizz weapon = goofy_ahh_choice("sword", "axe", "bow", "staff"); skibidi "Random weapon: " fanum_tax weapon fanum_tax skip;`                                                              |


---

## Data Structures

### Dictionaries

SkibidiLang supports immutable dictionaries, encouraging clean data flow and functional programming principles. This approach reduces the risk of unintended side effects and promotes safer, more predictable code behavior.

#### Example: Dictionary Usage

```
# Creating a dictionary
rizz stats = {
    "health": 100,
    "attack": 10,
    "defense": 5
};

# Accessing values
rizz health = stats["health"];

# Updating values (create a new dictionary)
rizz new_stats = {
    "health": stats["health"] ohio 10,
    "attack": stats["attack"],
    "defense": stats["defense"]
};
```

---

## Example Programs

### Hello, World

```
skibidi "Hello, World!" fanum_tax skip;
```

### Arithmetic and Variables

```
rizz x = 10;
rizz y = 20;
rizz z = x fanum_tax y;  # z = 30
skibidi z fanum_tax skip;
```

### Functions and Return Values

```
bussin add(x, y) {
    yeet x fanum_tax y;
}

rizz result = add(5, 3);
skibidi result;  # Prints 8
```

### Control Flow with Boolean Logic

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

---

## Featured Projects

### RPG Game

Dive into `examples/projects/rpg_game.br` to explore:

- Dictionary-based character stats
- Turn-based combat
- Inventory management
- Dynamic enemy scaling

---

## SkibidiLang Language Features

### Core Features

- **Arithmetic & Comparisons**: Handle math and logic with keywords like `fanum_tax` for addition or `alpha` for greater-than comparisons.
- **Immutability**: Encourages clean coding practices by restricting in-place updates to dictionaries.

### Programming Constructs

- **Conditional Statements**: Use `no_cap` (if/else) for decision-making.
- **Loops**: Utilize `ong` (while) for iteration.
- **Functions**: Define reusable code blocks with `bussin` and return values with `yeet`.

### Data Management

- **Dictionaries**: Work with immutable, string-keyed dictionaries for structured data.
- **Dynamic Variables**: Use `rizz` to declare and manage data.

### Input/Output

- **Console Input**: Capture user input with `whats_up_unc`.
- **Formatted Output**: Print data using `skibidi` and control newlines with `skip`.

### Syntax Rules

- Statements end with `;`.
- Code blocks are enclosed in `{}`.
- Strings use double quotes (").
- Comments start with `#`.

---

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AirmailSoap3209/SkibidiLang.git
   cd SkibidiLang
   ```
2. Run SkibidiLang programs using Python:
   ```bash
   python main.py your_program.br
   ```

### Requirements

- Python 3.6 or newer

### File Extension

SkibidiLang programs use the `.br` file extension.

---

## Best Practices

- **Use Descriptive Names**: Make variables and functions meaningful.
- **Comment Complex Logic**: Ensure readability for future users.
- **Maintain Consistent Formatting**: Indentation and spacing improve clarity.
- **Break Down Functions**: Keep them small and focused.

---

## Let’s Get Skibidi!

SkibidiLang is the perfect blend of fun and functionality. Share your creations, explore exciting projects, and contribute to the SkibidiLang community—let’s make programming skibidi and bussin together! 

