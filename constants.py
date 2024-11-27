"""Constants used in the SkibidiLang interpreter."""

# Token types
TOKEN_PRINT = 'PRINT'
TOKEN_VAR = 'VAR'
TOKEN_TRUE = 'TRUE'
TOKEN_FALSE = 'FALSE'
TOKEN_IF = 'IF'
TOKEN_FUNCTION = 'FUNCTION'
TOKEN_RETURN = 'RETURN'
TOKEN_WHILE = 'WHILE'
TOKEN_ADD = 'ADD'
TOKEN_SUB = 'SUB'
TOKEN_MUL = 'MUL'
TOKEN_DIV = 'DIV'
TOKEN_GT = 'GT'
TOKEN_LT = 'LT'
TOKEN_EQ = 'EQ'
TOKEN_STRING = 'STRING'
TOKEN_NUMBER = 'NUMBER'
TOKEN_IDENTIFIER = 'IDENTIFIER'
TOKEN_OPERATOR = 'OPERATOR'

# Keywords mapping
KEYWORDS = {
    'skibidi': TOKEN_PRINT,
    'rizz': TOKEN_VAR,
    'fr fr': TOKEN_TRUE,
    'cap': TOKEN_FALSE,
    'no cap': TOKEN_IF,
    'bussin': TOKEN_FUNCTION,
    'yeet': TOKEN_RETURN,
    'ong': TOKEN_WHILE,
    'fanum tax': TOKEN_ADD,
    'ohio': TOKEN_SUB,
    'gyatt': TOKEN_MUL,
    'ratio': TOKEN_DIV,
    'greater': TOKEN_GT,
    'less': TOKEN_LT,
    'equals': TOKEN_EQ
}

# Error messages
ERR_FILE_NOT_FOUND = "Error: File '{}' not found fr fr"
ERR_DIVISION_BY_ZERO = "Can't ratio by zero fr fr"
ERR_FUNCTION_NOT_FOUND = "Function '{}' not found fr fr"
ERR_FUNCTION_ARGS = "Function '{}' expects {} args but got {} fr fr"
