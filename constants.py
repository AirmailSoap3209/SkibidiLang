"""Constants used in the SkibidiLang interpreter.

This module defines all constant values used throughout the SkibidiLang implementation,
including token types, keywords mapping, and error messages.
"""

#------------------------------------------------------------------------------
# Token Types
#------------------------------------------------------------------------------

# Core language tokens
TOKEN_PRINT = 'PRINT'        # skibidi
TOKEN_VAR = 'VAR'           # rizz
TOKEN_RETURN = 'RETURN'     # yeet
TOKEN_FUNCTION = 'FUNCTION' # bussin
TOKEN_INPUT = 'INPUT'       # what's up unc
TOKEN_SKIP = 'SKIP'        # skip

# Control flow tokens
TOKEN_IF = 'IF'            # no cap
TOKEN_WHILE = 'WHILE'      # ong
TOKEN_TRUE = 'TRUE'        # fr fr
TOKEN_FALSE = 'FALSE'      # cap

# Arithmetic and comparison tokens
TOKEN_ADD = 'ADD'          # fanum
TOKEN_SUB = 'SUB'          # fanum tax
TOKEN_MUL = 'MUL'          # fanum times
TOKEN_DIV = 'DIV'          # fanum divided
TOKEN_GT = 'GT'            # more than
TOKEN_LT = 'LT'            # less than
TOKEN_EQ = 'EQ'            # same as

# Other tokens
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_NUMBER = 'NUMBER'
TOKEN_STRING = 'STRING'
TOKEN_OPERATOR = 'OPERATOR'
TOKEN_COLON = 'COLON'      # For dictionary key-value pairs
TOKEN_COMMA = 'COMMA'      # For separating dictionary items
TOKEN_LBRACKET = 'LBRACKET'  # For dictionary access
TOKEN_RBRACKET = 'RBRACKET'  # For dictionary access

#------------------------------------------------------------------------------
# Keyword Mappings
#------------------------------------------------------------------------------

KEYWORDS = {
    # Core language keywords
    'skibidi': TOKEN_PRINT,
    'rizz': TOKEN_VAR,
    'bussin': TOKEN_FUNCTION,
    'yeet': TOKEN_RETURN,
    "what's up unc": TOKEN_INPUT,
    'skip': TOKEN_SKIP,
    
    # Control flow keywords
    'no cap': TOKEN_IF,
    'ong': TOKEN_WHILE,
    'fr fr': TOKEN_TRUE,
    'cap': TOKEN_FALSE,
    
    # Arithmetic operators
    'fanum tax': TOKEN_ADD,
    'ohio': TOKEN_SUB,
    'gyatt': TOKEN_MUL,
    'ratio': TOKEN_DIV,
    
    # Comparison operators
    'alpha': TOKEN_GT,
    'beta': TOKEN_LT,
    'sigma': TOKEN_EQ
}

#------------------------------------------------------------------------------
# Error Messages
#------------------------------------------------------------------------------

ERR_FILE_NOT_FOUND = "Erm what the sigma? File '{}' not found fr fr"
ERR_DIVISION_BY_ZERO = "Erm What The Sigma? Can't ratio by zero fr fr"
ERR_FUNCTION_NOT_FOUND = "Erm What The Sigma? Function '{}' not found fr fr"
ERR_FUNCTION_ARGS = "Erm What The Sigma? Function '{}' expects {} args but got {} fr fr"
