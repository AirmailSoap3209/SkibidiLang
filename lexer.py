from tokens import TokenType, Token, KEYWORDS
from exceptions import SkibidiSyntaxErmWhatTheSigma

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0] if text else None
        self.line = 1
        self.column = 1

    def error(self, message='Invalid character'):
        raise SkibidiSyntaxErmWhatTheSigma(
            message,
            line=self.line,
            column=self.column,
            token=self.current_char
        )

    def advance(self):
        if self.current_char == '\n':
            self.line += 1
            self.column = 0
        else:
            self.column += 1
            
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def peek(self):
        peek_pos = self.pos + 1
        return self.text[peek_pos] if peek_pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char and self.current_char != '\n':
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
        self.advance()  # Skip opening quote
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
        if self.current_char == '"':
            self.advance()  # Skip closing quote
            return result
        self.error()

    def identifier(self):
        result = ''
        while self.current_char and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def get_next_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '#':
                self.skip_comment()
                continue

            if self.current_char.isdigit():
                return Token(TokenType.NUMBER, self.number(), self.line, self.column)

            if self.current_char == '"':
                return Token(TokenType.STRING, self.string(), self.line, self.column)

            if self.current_char.isalpha() or self.current_char == '_':
                identifier = self.identifier()
                token_type = KEYWORDS.get(identifier)
                if token_type:
                    return Token(token_type, identifier, self.line, self.column)
                return Token(TokenType.IDENTIFIER, identifier, self.line, self.column)

            if self.current_char == '=':
                self.advance()
                return Token(TokenType.ASSIGN, '=', self.line, self.column)

            if self.current_char == '{':
                self.advance()
                return Token(TokenType.LBRACE, '{', self.line, self.column)

            if self.current_char == '}':
                self.advance()
                return Token(TokenType.RBRACE, '}', self.line, self.column)

            if self.current_char == '[':
                self.advance()
                return Token(TokenType.LBRACKET, '[', self.line, self.column)

            if self.current_char == ']':
                self.advance()
                return Token(TokenType.RBRACKET, ']', self.line, self.column)

            if self.current_char == ':':
                self.advance()
                return Token(TokenType.COLON, ':', self.line, self.column)

            if self.current_char == ',':
                self.advance()
                return Token(TokenType.COMMA, ',', self.line, self.column)

            if self.current_char == ';':
                self.advance()
                return Token(TokenType.EOL, ';', self.line, self.column)

            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(', self.line, self.column)

            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')', self.line, self.column)

            self.error()

        return Token(TokenType.EOF, None, self.line, self.column)
