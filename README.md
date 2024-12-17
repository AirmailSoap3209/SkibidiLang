# SkibidiLang

**SkibidiLang** is a meme-inspired programming language designed to incorporate internet humor while maintaining the functionality of traditional programming languages. It is intended for creating projects and learning programming.

---

## Key Features

- **Programming Constructs**: Supports loops, conditionals, and functions.
- **Data Management**: Provides immutable dictionaries and type-safe structures.
- **Console I/O**: Simplified input and output handling using keywords like `whats_up_unc`.
- **Modular Design**: Allows building scalable applications with `.br` files.

---

## Syntax Overview

### Keywords

| **Category**            | **SkibidiLang Keyword** | **Traditional Equivalent** | **Syntax Example**                                                                                                                                                                      |
| ----------------------- | ----------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Printing/I/O**        | `skibidi`               | `print`                    | `skibidi "Hello, world!" fanum_tax skip;`                                                                                                                                                 |
|                         | `whats_up_unc`          | `input`                    | `rizz name = whats_up_unc "Enter your name: ";`                                                                                                                                           |
|                         | `skip`                  | `newline`                  | `skibidi skip;`                                                                                                                                                                          |
| **Variables/Functions** | `rizz`                  | `variable declaration`     | `rizz x = 5;`                                                                                                                                                                            |
|                         | `bussin`                | `function definition`      | `bussin add(x, y) {`<br>` rizz sum = x fanum_tax y; yeet sum; `<br>`};`                                                                                                                            |
|                         | `yeet`                  | `return`                   | `yeet result;`                                                                                                                                                                           |
| **Control Flow**        | `no_cap`                | `if`                       | `no_cap x alpha 0 {`<br>` skibidi "x is positive"; `<br>`};`                                                                                                                                         |
|                         | `ong`                   | `while`                    | `ong x alpha 5 {`<br>` skibidi x; x = x fanum_tax 1; `<br>`};`                                                                                                                                      |
|                         | `fr_fr`                 | `true`                     | `no_cap x fr_fr {`<br>` skibidi "x is true"; `<br>`};`                                                                                                                                               |
|                         | `cap`                   | `false`                    | `no_cap x cap {`<br>` skibidi "x is false"; `<br>`};`                                                                                                                                               |
|                         | `sigma`                 | `==`                       | `no_cap x sigma y {`<br>` skibidi "x is equal to y"; `<br>`};`                                                                                                                                       |
|                         | `ohio`                  | `not` (unary negation)     | `rizz negated_x = ohio x;`                                                                                                                                                               |
| **Arithmetic**          | `fanum_tax`             | `+`                        | `rizz result = x fanum_tax y;`                                                                                                                                                           |
|                         | `ohio`                  | `-`                        | `rizz difference = x ohio y;`                                                                                                                                                           |
|                         | `gyatt`                 | `*`                        | `rizz product = x gyatt y;`                                                                                                                                                             |
|                         | `ratio`                 | `/`                        | `rizz quotient = x ratio y;`                                                                                                                                                            |
| **Logical Operators**   | `ohio`                  | `not`                      | `no_cap ohio x fr_fr {`<br>` skibidi "x is false"; `<br>`};`                                                                                                                                        |
|                         | `alpha`                 | `>`                        | `no_cap x alpha y {`<br>` skibidi "x is greater than y"; `<br>`};`                                                                                                                                    |
|                         | `beta`                  | `<`                        | `no_cap x beta y {`<br>` skibidi "x is less than y"; `<br>`};`                                                                                                                                       |
| **Random Functions**    | `goofy_ahh`             | `random float`             | `rizz basic_random = goofy_ahh();`<br>` skibidi "Random float (0-1): " fanum_tax basic_random fanum_tax skip;`                                                                                   |
|                         | `goofy_ahh_int`         | `random integer`           | `rizz dice_roll = goofy_ahh_int(1, 6);`<br>` skibidi "Dice roll (1-6): " fanum_tax dice_roll fanum_tax skip;`                                                                                   |
|                         | `goofy_ahh_choice`      | `random choice from list`  | `rizz weapon = goofy_ahh_choice("sword", "axe", "bow", "staff");`<br>` skibidi "Random weapon: " fanum_tax weapon fanum_tax skip;`                                                              |
| **Others**              | `mew`                  | `#` (single-line comment)  | `mew This is a comment`                                                                                                                                                                |

### Key Concepts

- **Compound Conditions**: Combine conditions using logical operators.
  ```
  no_cap (x alpha 0) cap (x sigma 10) {
      skibidi "x is between 1 and 10";
  };
  ```

- **Unary Negation**: Negate values using `ohio`.
  ```
  rizz negated_x = ohio x;
  ```

- **Random Functions**: `goofy_ahh_int` takes min and max values, `goofy_ahh_choice` selects a random value from a list.
  ```
  rizz random_value = goofy_ahh_choice("apple", "banana", "cherry");
  ```

---

## Data Structures

### Immutable Dictionaries

SkibidiLang uses immutable dictionaries, which promote functional programming principles. To update data, a new dictionary must be created to avoid side effects.

Example:
```
rizz stats = {
    "health": 100,
    "attack": 10,
    "defense": 5
};

rizz health = stats["health"];

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

### Arithmetic & Variables
```
rizz x = 10;
rizz y = 20;
rizz z = x fanum_tax y;
skibidi z fanum_tax skip;
```

### Functions & Return Values
```
bussin add(x, y) {
    yeet x fanum_tax y;
}

rizz result = add(5, 3);
skibidi result;
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

## SkibidiLang Features

- **Arithmetic & Comparisons**: Use keywords like `fanum_tax` for addition and `alpha` for comparisons.
- **Immutability**: Encourages safe, predictable programming with immutable dictionaries.
- **Control Flow**: Conditional statements (`no_cap`) and loops (`ong`) are available.
- **Data Structures**: Use immutable dictionaries and dynamic variables (`rizz`).
- **I/O**: Input with `whats_up_unc` and output with `skibidi`.

### Syntax Rules

- Statements end with `;`.
- Code blocks are enclosed in `{}`.
- Strings use double quotes.
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

- SkibidiLang programs use the `.br` extension.

---

## Best Practices

- **Descriptive Naming**: Use meaningful variable and function names.
- **Commenting**: Ensure readability for future developers.
- **Consistent Formatting**: Proper indentation improves code clarity.
- **Function Breakdown**: Keep functions small and focused.
