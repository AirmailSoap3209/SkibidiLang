"""Custom exceptions for the SkibidiLang interpreter."""

class SkibidiError(Exception):
    """Base exception class for SkibidiLang."""
    pass

class SkibidiSyntaxError(SkibidiError):
    """Raised when there is a syntax error in the code."""
    pass

class SkibidiRuntimeError(SkibidiError):
    """Raised when there is a runtime error during code execution."""
    pass

class SkibidiFunctionError(SkibidiError):
    """Raised when there is an error related to function calls."""
    pass

class SkibidiDivisionByZeroError(SkibidiRuntimeError):
    """Raised when attempting to divide by zero."""
    pass

class SkibidiFileError(SkibidiError):
    """Raised when there is an error with file operations."""
    pass
