from enum import Enum, auto

class TokenType(Enum):
    # Core language tokens
    PRINT = auto()
    VAR = auto()
    FUNCTION = auto()
    RETURN = auto()
    INPUT = auto()
    
    # Control flow tokens
    IF = auto()
    WHILE = auto()
    TRUE = auto()
    FALSE = auto()
    NOT = auto()
    
    # Arithmetic operators
    ADD = auto()
    SUB = auto()
    MUL = auto()
    DIV = auto()
    
    # Comparison operators
    GT = auto()
    LT = auto()
    EQ = auto()
    
    # Additional tokens
    NUMBER = auto()
    STRING = auto()
    IDENTIFIER = auto()
    RANDOM = auto()
    RANDOM_INT = auto()
    RANDOM_CHOICE = auto()
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    COLON = auto()
    ASSIGN = auto()
    EOL = auto()  # End of line
    EOF = auto()  # End of file

class Token:
    def __init__(self, type, value=None, line=1, column=1):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        if self.value:
            return f"Token({self.type}, {self.value})"
        return f"Token({self.type})"

KEYWORDS = {
    # Core language keywords
    'skibidi': TokenType.PRINT,
    'rizz': TokenType.VAR,
    'bussin': TokenType.FUNCTION,
    'yeet': TokenType.RETURN,
    "whats_up_unc": TokenType.INPUT,
    'goofy_ahh': TokenType.RANDOM,
    'goofy_ahh_int': TokenType.RANDOM_INT,
    'goofy_ahh_choice': TokenType.RANDOM_CHOICE,
    
    # Control flow keywords
    'no_cap': TokenType.IF,
    'ong': TokenType.WHILE,
    'fr_fr': TokenType.TRUE,
    'cap': TokenType.FALSE,
    
    # Arithmetic operators
    'fanum_tax': TokenType.ADD,
    'ohio': TokenType.SUB,
    'gyatt': TokenType.MUL,
    'ratio': TokenType.DIV,
    
    # Comparison operators
    'alpha': TokenType.GT,
    'beta': TokenType.LT,
    'sigma': TokenType.EQ
}
