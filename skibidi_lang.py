import re
from dataclasses import dataclass
from typing import Any, List, Dict, Optional

@dataclass
class Token:
    type: str
    value: str

class Function:
    def __init__(self, params: List[str], body: List[str], parent_scope: Dict[str, Any]):
        self.params = params
        self.body = body
        self.parent_scope = parent_scope

class SkibidiLexer:
    def __init__(self):
        self.tokens = []
        self.keywords = {
            'skibidi': 'PRINT',
            'rizz': 'VAR',
            'fr fr': 'TRUE',
            'cap': 'FALSE',
            'no cap': 'IF',
            'bussin': 'FUNCTION',
            'yeet': 'RETURN',
            'ong': 'WHILE',
            'fanum tax': 'ADD',
            'ohio': 'SUB',
            'gyatt': 'MUL',
            'ratio': 'DIV',
            'greater': 'GT',
            'less': 'LT',
            'equals': 'EQ'
        }

    def tokenize(self, code: str) -> List[Token]:
        self.tokens = []
        words = code.split()
        i = 0
        while i < len(words):
            word = words[i]
            
            # Check for two-word keywords
            if i < len(words) - 1:
                two_words = f"{word} {words[i+1]}"
                if two_words in self.keywords:
                    self.tokens.append(Token(self.keywords[two_words], two_words))
                    i += 2
                    continue

            # Check for strings (in quotes)
            if word.startswith('"') and word.endswith('"'):
                self.tokens.append(Token('STRING', word[1:-1]))
            # Single word keywords
            elif word in self.keywords:
                self.tokens.append(Token(self.keywords[word], word))
            # Numbers
            elif word.isdigit() or (word.startswith('-') and word[1:].isdigit()):
                self.tokens.append(Token('NUMBER', word))
            # Variables/Identifiers
            elif word.isalnum():
                self.tokens.append(Token('IDENTIFIER', word))
            # Operators and special characters
            elif word in '+-*/=:':
                self.tokens.append(Token('OPERATOR', word))
            
            i += 1
        
        return self.tokens

class SkibidiInterpreter:
    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.functions: Dict[str, Function] = {}
        self.lexer = SkibidiLexer()
        self.return_value: Optional[Any] = None

    def evaluate_file(self, filename: str):
        try:
            with open(filename, 'r') as file:
                code = file.read()
                lines = code.split('\n')
                i = 0
                while i < len(lines):
                    line = lines[i].split('#')[0].strip()  # Remove comments
                    if line:
                        if line.endswith(':'):  # Block start
                            block_lines = []
                            i += 1
                            while i < len(lines) and (not lines[i].strip() or lines[i].startswith('    ')):
                                if lines[i].strip():
                                    block_lines.append(lines[i].strip())
                                i += 1
                            i -= 1  # Back up one to handle the next line properly
                            self.evaluate_block(line, block_lines)
                        else:
                            self.evaluate(line)
                    i += 1
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found fr fr")
        except Exception as e:
            print(f"Error: {str(e)}")

    def evaluate_block(self, header: str, body: List[str]):
        try:
            tokens = self.lexer.tokenize(header[:-1])  # Remove the colon
            
            if not tokens:
                return
                
            if tokens[0].type == 'IF':  # no cap
                if len(tokens) >= 4:  # Need at least: no cap var op value
                    condition = self._evaluate_condition(tokens[1:])
                    if condition:
                        for line in body:
                            self.evaluate(line)
            
            elif tokens[0].type == 'WHILE':  # ong
                if len(tokens) >= 4:  # Need at least: ong var op value
                    while self._evaluate_condition(tokens[1:]):
                        for line in body:
                            self.evaluate(line)
            
            elif tokens[0].type == 'FUNCTION':  # bussin
                if len(tokens) >= 2:  # Need at least: bussin name
                    func_name = tokens[1].value
                    params = [t.value for t in tokens[2:] if t.type == 'IDENTIFIER']
                    self.functions[func_name] = Function(params, body, dict(self.variables))
        except Exception as e:
            print(f"Error in block: {str(e)}")

    def _evaluate_condition(self, tokens: List[Token]) -> bool:
        try:
            if len(tokens) < 3:  # Need at least: value operator value
                return False

            # Find comparison operator
            comp_index = -1
            for i, token in enumerate(tokens):
                if token.type in ['GT', 'LT', 'EQ']:
                    comp_index = i
                    break
            
            if comp_index == -1:
                return False

            # Get left value
            left = tokens[0].value
            if tokens[0].type == 'IDENTIFIER':
                left = float(self.variables.get(left, 0))
            else:
                left = float(left)

            # Get right value
            right = tokens[comp_index + 1].value
            if tokens[comp_index + 1].type == 'IDENTIFIER':
                right = float(self.variables.get(right, 0))
            else:
                right = float(right)

            # Compare
            op = tokens[comp_index].type
            if op == 'GT':
                return left > right
            elif op == 'LT':
                return left < right
            elif op == 'EQ':
                return left == right
            return False
        except Exception as e:
            print(f"Error in condition: {str(e)}")
            return False

    def evaluate(self, code: str):
        try:
            tokens = self.lexer.tokenize(code)
            if not tokens:
                return
                
            i = 0
            while i < len(tokens):
                token = tokens[i]
                
                if token.type == 'PRINT':
                    if i + 1 < len(tokens):
                        i += 1
                        value = tokens[i].value
                        if tokens[i].type == 'IDENTIFIER':
                            value = self.variables.get(value, 'undefined')
                        print(value)
                
                elif token.type == 'VAR':
                    if i + 3 < len(tokens):  # Need: rizz name = value
                        i += 1
                        var_name = tokens[i].value
                        i += 2  # Skip '='
                        
                        if tokens[i].type == 'IDENTIFIER' and tokens[i].value in self.functions:
                            # Function call
                            func_name = tokens[i].value
                            i += 1
                            args = []
                            while i < len(tokens):
                                if tokens[i].type in ['NUMBER', 'IDENTIFIER']:
                                    args.append(tokens[i].value)
                                i += 1
                            value = self._call_function(func_name, args)
                        else:
                            value = tokens[i].value
                            if tokens[i].type == 'IDENTIFIER':
                                value = self.variables.get(value, 0)
                            elif tokens[i].type == 'NUMBER':
                                value = float(value)
                            
                            # Check for arithmetic
                            if i + 2 < len(tokens):
                                op_token = tokens[i + 1]
                                if op_token.type in ['ADD', 'SUB', 'MUL', 'DIV']:
                                    i += 2
                                    second_value = tokens[i].value
                                    if tokens[i].type == 'IDENTIFIER':
                                        second_value = self.variables.get(second_value, 0)
                                    value = self._perform_operation(float(value), float(second_value), op_token.type)
                        
                        self.variables[var_name] = value
                
                elif token.type == 'RETURN':
                    if i + 1 < len(tokens):
                        i += 1
                        value = tokens[i].value
                        if tokens[i].type == 'IDENTIFIER':
                            value = float(self.variables.get(value, 0))
                        elif tokens[i].type == 'NUMBER':
                            value = float(value)
                        
                        if i + 2 < len(tokens):
                            op_token = tokens[i + 1]
                            if op_token.type in ['ADD', 'SUB', 'MUL', 'DIV']:
                                i += 2
                                second_value = tokens[i].value
                                if tokens[i].type == 'IDENTIFIER':
                                    second_value = self.variables.get(second_value, 0)
                                value = self._perform_operation(float(value), float(second_value), op_token.type)
                        
                        self.return_value = value
                        return
                
                i += 1
        except Exception as e:
            print(f"Error: {str(e)}")

    def _call_function(self, func_name: str, args: List[str]) -> Any:
        try:
            if func_name not in self.functions:
                raise ValueError(f"Function '{func_name}' not found fr fr")
            
            func = self.functions[func_name]
            if len(args) != len(func.params):
                raise ValueError(f"Function '{func_name}' expects {len(func.params)} args but got {len(args)} fr fr")
            
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
            print(f"Error in function call: {str(e)}")
            return 0

    def _perform_operation(self, a: float, b: float, op_type: str) -> float:
        try:
            if op_type == 'ADD':  # fanum tax
                return a + b
            elif op_type == 'SUB':  # ohio
                return a - b
            elif op_type == 'MUL':  # gyatt
                return a * b
            elif op_type == 'DIV':  # ratio
                if b == 0:
                    raise ValueError("Can't ratio by zero fr fr")
                return a / b
            return 0
        except Exception as e:
            print(f"Error in operation: {str(e)}")
            return 0

def main():
    interpreter = SkibidiInterpreter()
    
    import sys
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
