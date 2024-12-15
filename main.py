import sys
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Erm What The Sigma? File '{filename}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    try:
        # Initialize components
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter()

        # Parse and interpret
        tree = parser.parse()
        interpreter.interpret(tree)

    except Exception as e:
        print(f"\nErm What The Sigma? {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
