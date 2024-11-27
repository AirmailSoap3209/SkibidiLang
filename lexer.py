from tokens import Token, TokenType, KEYWORDS

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = text[0] if text else None
        self.line = 1
        self.column = 1

    def error(self):
        raise Exception(f'Invalid character "{self.current_char}" at line {self.line}, column {self.column}')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            if self.current_char == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.current_char = self.text[self.pos]

    def peek(self, n=1):
        peek_pos = self.pos + n
        if peek_pos > len(self.text) - 1:
            return None
        return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char and self.current_char != '\n':
            self.advance()
        if self.current_char:
            self.advance()

    def number(self):
        result = ''
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            result += self.current_char
            self.advance()
        
        try:
            return float(result) if '.' in result else int(result)
        except ValueError:
            self.error()

    def string(self):
        result = ''
        # Skip the opening quote
        self.advance()
        
        while self.current_char and self.current_char != '"':
            if self.current_char == '\\':
                self.advance()
                if self.current_char == 'n':
                    result += '\n'
                elif self.current_char == 't':
                    result += '\t'
                else:
                    result += self.current_char
            else:
                result += self.current_char
            self.advance()
            
        if not self.current_char:
            raise Exception('Unterminated string')
            
        # Skip the closing quote
        self.advance()
        return result

    def read_identifier(self):
        # First check for multi-word keywords
        for keyword in sorted(KEYWORDS.keys(), key=len, reverse=True):
            if self.text[self.pos:].startswith(keyword):
                # Make sure it's a complete word (followed by whitespace, punctuation, or EOF)
                end_pos = self.pos + len(keyword)
                if end_pos >= len(self.text) or not self.text[end_pos].isalnum():
                    # Advance the position
                    for _ in range(len(keyword)):
                        self.advance()
                    return keyword

        # If no keyword match, read as normal identifier
        result = ''
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char:
            # Skip whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # Skip comments
            if self.current_char == '#':
                self.skip_comment()
                continue

            # Numbers
            if self.current_char.isdigit():
                return Token(TokenType.NUMBER, self.number(), self.line, self.column)

            # Strings
            if self.current_char == '"':
                return Token(TokenType.STRING, self.string(), self.line, self.column)

            # Special characters
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(', self.line, self.column)
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')', self.line, self.column)
            if self.current_char == '{':
                self.advance()
                return Token(TokenType.LBRACE, '{', self.line, self.column)
            if self.current_char == '}':
                self.advance()
                return Token(TokenType.RBRACE, '}', self.line, self.column)
            if self.current_char == ',':
                self.advance()
                return Token(TokenType.COMMA, ',', self.line, self.column)
            if self.current_char == '=':
                self.advance()
                return Token(TokenType.ASSIGN, '=', self.line, self.column)
            if self.current_char == ';':
                self.advance()
                return Token(TokenType.EOL, ';', self.line, self.column)

            # Identifiers and keywords
            if self.current_char.isalpha() or self.current_char == '_':
                identifier = self.read_identifier()
                # Check for keywords
                token_type = KEYWORDS.get(identifier)
                if token_type:
                    return Token(token_type, identifier, self.line, self.column)
                return Token(TokenType.IDENTIFIER, identifier, self.line, self.column)

            self.error()

        return Token(TokenType.EOF, None, self.line, self.column)
