"""Custom exceptions for the SkibidiLang interpreter.

This module defines all custom exceptions that can be raised during the execution
of SkibidiLang code. Each exception type corresponds to a specific category of
error that can occur during lexing, parsing, or execution.
"""

class SkibidiErmWhatTheSigma(Exception):
    """Base exception class for all SkibidiLang errors."""
    def __init__(self, message, line=None, column=None, token=None):
        self.message = message
        self.line = line
        self.column = column
        self.token = token
        super().__init__(self._format_message())
    
    def _format_message(self):
        msg = []
        if self.line is not None:
            msg.append(f"Line {self.line}")
        if self.column is not None:
            msg.append(f"Column {self.column}")
        if self.token is not None:
            msg.append(f"at token: {self.token}")
        if msg:
            return f"Error: {self.message} ({', '.join(msg)})"
        return f"Error: {self.message}"

class SkibidiSyntaxErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when the lexer encounters invalid syntax in the source code."""
    pass

class SkibidiRuntimeErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when an error occurs during code execution."""
    pass

class SkibidiFunctionErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when there's an error related to function definition or calling."""
    pass

class SkibidiDivisionByZeroErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when attempting to divide by zero."""
    pass

class SkibidiFileErmWhatTheSigma(SkibidiErmWhatTheSigma):
    """Raised when there's an error reading or processing a source file."""
    pass
