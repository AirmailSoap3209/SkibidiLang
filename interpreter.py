"""Main interpreter module for SkibidiLang."""

from typing import Any, Dict, List, Optional
import sys

from constants import (
    TOKEN_PRINT, TOKEN_VAR, TOKEN_TRUE, TOKEN_FALSE, TOKEN_IF, TOKEN_FUNCTION,
    TOKEN_RETURN, TOKEN_WHILE, TOKEN_ADD, TOKEN_SUB, TOKEN_MUL, TOKEN_DIV,
    TOKEN_GT, TOKEN_LT, TOKEN_EQ, TOKEN_IDENTIFIER, TOKEN_NUMBER,
    ERR_FILE_NOT_FOUND, ERR_DIVISION_BY_ZERO, ERR_FUNCTION_NOT_FOUND, ERR_FUNCTION_ARGS
)
from exceptions import (
    SkibidiError, SkibidiRuntimeError, SkibidiFunctionError,
    SkibidiDivisionByZeroError, SkibidiFileError
)
from lexer import SkibidiLexer, Token
from function import Function

class SkibidiInterpreter:
    """Main interpreter class for SkibidiLang."""
    
    def __init__(self):
        """Initialize the interpreter with empty variable and function stores."""
        self.variables: Dict[str, Any] = {}
        self.functions: Dict[str, Function] = {}
        self.lexer = SkibidiLexer()
        self.return_value: Optional[Any] = None

    def evaluate_file(self, filename: str) -> None:
        """
        Evaluate code from a file.
        
        Args:
            filename: Path to the file to evaluate.
            
        Raises:
            SkibidiFileError: If file cannot be read.
        """
        try:
            with open(filename, 'r') as file:
                code = file.read()
                lines = code.split('\n')
                i = 0
                while i < len(lines):
                    # Remove comments and whitespace
                    line = lines[i].split('#')[0].strip()
                    
                    # Skip empty lines
                    if not line:
                        i += 1
                        continue
                        
                    if line.endswith(':'):  # Block start
                        block_lines = []
                        i += 1
                        while i < len(lines) and (not lines[i].strip() or lines[i].startswith('    ')):
                            block_line = lines[i].split('#')[0].strip()
                            if block_line:
                                block_lines.append(block_line)
                            i += 1
                        i -= 1  # Back up one to handle the next line properly
                        self.evaluate_block(line, block_lines)
                    else:
                        self.evaluate(line)
                    i += 1
        except FileNotFoundError:
            raise SkibidiFileError(ERR_FILE_NOT_FOUND.format(filename))
        except Exception as e:
            raise SkibidiRuntimeError(str(e))

    def evaluate_block(self, header: str, body: List[str]) -> None:
        """
        Evaluate a block of code (if/while/function).
        
        Args:
            header: The block header line.
            body: List of code lines in the block.
        """
        try:
            tokens = self.lexer.tokenize(header[:-1])  # Remove the colon
            
            if not tokens:
                return
                
            if tokens[0].type == TOKEN_IF:
                if len(tokens) >= 4:  # Need at least: no cap var op value
                    condition = self._evaluate_condition(tokens[1:])
                    if condition:
                        for line in body:
                            self.evaluate(line)
            
            elif tokens[0].type == TOKEN_WHILE:
                if len(tokens) >= 4:  # Need at least: ong var op value
                    while self._evaluate_condition(tokens[1:]):
                        for line in body:
                            self.evaluate(line)
            
            elif tokens[0].type == TOKEN_FUNCTION:
                if len(tokens) >= 2:  # Need at least: bussin name
                    func_name = tokens[1].value
                    params = [t.value for t in tokens[2:] if t.type == TOKEN_IDENTIFIER]
                    self.functions[func_name] = Function(params, body, dict(self.variables))

        except Exception as e:
            raise SkibidiRuntimeError(f"Error in block: {str(e)}")

    def _evaluate_condition(self, tokens: List[Token]) -> bool:
        """
        Evaluate a condition in if/while statements.
        
        Args:
            tokens: List of tokens in the condition.
            
        Returns:
            Boolean result of the condition.
        """
        try:
            if len(tokens) < 3:  # Need at least: value operator value
                return False

            # Find comparison operator
            comp_index = -1
            for i, token in enumerate(tokens):
                if token.type in [TOKEN_GT, TOKEN_LT, TOKEN_EQ]:
                    comp_index = i
                    break
            
            if comp_index == -1:
                return False

            # Get left value
            left = tokens[0].value
            if tokens[0].type == TOKEN_IDENTIFIER:
                left = float(self.variables.get(left, 0))
            else:
                left = float(left)

            # Get right value
            right = tokens[comp_index + 1].value
            if tokens[comp_index + 1].type == TOKEN_IDENTIFIER:
                right = float(self.variables.get(right, 0))
            else:
                right = float(right)

            # Compare
            op = tokens[comp_index].type
            if op == TOKEN_GT:
                return left > right
            elif op == TOKEN_LT:
                return left < right
            elif op == TOKEN_EQ:
                return left == right
            return False

        except Exception as e:
            raise SkibidiRuntimeError(f"Error in condition: {str(e)}")

    def evaluate(self, code: str) -> None:
        """
        Evaluate a single line of code.
        
        Args:
            code: The line of code to evaluate.
        """
        try:
            tokens = self.lexer.tokenize(code)
            if not tokens:
                return
                
            i = 0
            while i < len(tokens):
                token = tokens[i]
                
                if token.type == TOKEN_PRINT:
                    if i + 1 < len(tokens):
                        i += 1
                        value = tokens[i].value
                        if tokens[i].type == TOKEN_IDENTIFIER:
                            value = self.variables.get(value, 'undefined')
                        print(value)
                
                elif token.type == TOKEN_VAR:
                    if i + 3 < len(tokens):  # Need: rizz name = value
                        i += 1
                        var_name = tokens[i].value
                        i += 2  # Skip '='
                        
                        if tokens[i].type == TOKEN_IDENTIFIER and tokens[i].value in self.functions:
                            # Function call
                            func_name = tokens[i].value
                            i += 1
                            args = []
                            while i < len(tokens):
                                if tokens[i].type in [TOKEN_NUMBER, TOKEN_IDENTIFIER]:
                                    args.append(tokens[i].value)
                                i += 1
                            value = self._call_function(func_name, args)
                        else:
                            value = tokens[i].value
                            if tokens[i].type == TOKEN_IDENTIFIER:
                                value = self.variables.get(value, 0)
                            elif tokens[i].type == TOKEN_NUMBER:
                                value = float(value)
                            
                            # Check for arithmetic
                            if i + 2 < len(tokens):
                                op_token = tokens[i + 1]
                                if op_token.type in [TOKEN_ADD, TOKEN_SUB, TOKEN_MUL, TOKEN_DIV]:
                                    i += 2
                                    second_value = tokens[i].value
                                    if tokens[i].type == TOKEN_IDENTIFIER:
                                        second_value = self.variables.get(second_value, 0)
                                    value = self._perform_operation(float(value), float(second_value), op_token.type)
                        
                        self.variables[var_name] = value
                
                elif token.type == TOKEN_RETURN:
                    if i + 1 < len(tokens):
                        i += 1
                        value = tokens[i].value
                        if tokens[i].type == TOKEN_IDENTIFIER:
                            value = float(self.variables.get(value, 0))
                        elif tokens[i].type == TOKEN_NUMBER:
                            value = float(value)
                        
                        if i + 2 < len(tokens):
                            op_token = tokens[i + 1]
                            if op_token.type in [TOKEN_ADD, TOKEN_SUB, TOKEN_MUL, TOKEN_DIV]:
                                i += 2
                                second_value = tokens[i].value
                                if tokens[i].type == TOKEN_IDENTIFIER:
                                    second_value = self.variables.get(second_value, 0)
                                value = self._perform_operation(float(value), float(second_value), op_token.type)
                        
                        self.return_value = value
                        return
                
                i += 1

        except Exception as e:
            raise SkibidiRuntimeError(str(e))

    def _call_function(self, func_name: str, args: List[str]) -> Any:
        """
        Call a function with the given arguments.
        
        Args:
            func_name: Name of the function to call.
            args: List of argument values.
            
        Returns:
            The return value of the function.
            
        Raises:
            SkibidiFunctionError: If function is not found or argument count mismatch.
        """
        try:
            if func_name not in self.functions:
                raise SkibidiFunctionError(ERR_FUNCTION_NOT_FOUND.format(func_name))
            
            func = self.functions[func_name]
            if len(args) != len(func.params):
                raise SkibidiFunctionError(ERR_FUNCTION_ARGS.format(func_name, len(func.params), len(args)))
            
            # Set up new scope
            old_vars = dict(self.variables)
            self.variables = dict(func.parent_scope)
            
            # Bind parameters
            for param, arg in zip(func.params, args):
                if arg.isdigit() or (arg.startswith('-') and arg[1:].isdigit()):
                    self.variables[param] = float(arg)
                else:
                    self.variables[param] = old_vars.get(arg, 0)
            
            # Execute function body
            self.return_value = None
            for line in func.body:
                self.evaluate(line)
                if self.return_value is not None:
                    break
            
            # Restore scope
            result = self.return_value if self.return_value is not None else None
            self.variables = old_vars
            return result

        except Exception as e:
            raise SkibidiFunctionError(str(e))

    def _perform_operation(self, a: float, b: float, op_type: str) -> float:
        """
        Perform an arithmetic operation.
        
        Args:
            a: First operand.
            b: Second operand.
            op_type: Type of operation (ADD, SUB, MUL, DIV).
            
        Returns:
            Result of the operation.
            
        Raises:
            SkibidiDivisionByZeroError: If attempting to divide by zero.
        """
        try:
            if op_type == TOKEN_ADD:  # fanum tax
                return a + b
            elif op_type == TOKEN_SUB:  # ohio
                return a - b
            elif op_type == TOKEN_MUL:  # gyatt
                return a * b
            elif op_type == TOKEN_DIV:  # ratio
                if b == 0:
                    raise SkibidiDivisionByZeroError(ERR_DIVISION_BY_ZERO)
                return a / b
            return 0

        except SkibidiDivisionByZeroError:
            raise
        except Exception as e:
            raise SkibidiRuntimeError(f"Error in operation: {str(e)}")

def main():
    """Main entry point for the interpreter."""
    interpreter = SkibidiInterpreter()
    
    if len(sys.argv) > 1:
        # Run file mode
        interpreter.evaluate_file(sys.argv[1])
    else:
        # Interactive mode
        print("Welcome to SkibidiLang! Type 'exit' to quit.")
        print("You can also run .skibi files with: python skibidi_lang.py your_file.skibi")
        while True:
            try:
                code = input('skibidi> ')
                if code.lower() == 'exit':
                    print("Goodbye!")
                    break
                if code.strip():  # Only evaluate non-empty lines
                    interpreter.evaluate(code)
            except EOFError:
                print("\nGoodbye!")
                break
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
