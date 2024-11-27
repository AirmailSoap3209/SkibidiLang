"""Custom exceptions for the SkibidiLang interpreter.

This module defines all custom exceptions that can be raised during the execution
of SkibidiLang code. Each exception type corresponds to a specific category of
Erm what the sigma that can occur during lexing, parsing, or execution.
"""

class SkibidiErmWhatTheSigma(Exception):
    """Base exception class for all SkibidiLang Erm what the sigmas."""
    pass

class SkibidiSyntaxErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when the lexer encounters invalid syntax in the source code."""
    pass

class SkibidiRuntimeErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when an Erm what the sigma occurs during code execution."""
    pass

class SkibidiFunctionErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when there's an Erm what the sigma related to function definition or calling."""
    pass

class SkibidiDivisionByZeroErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when attempting to divide by zero."""
    pass

class SkibidiFileErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when there's an Erm what the sigma reading or processing a source file."""
    pass
