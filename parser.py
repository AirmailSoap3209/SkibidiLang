from tokens import TokenType, Token

class ASTNode:
    pass

class NumberNode(ASTNode):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class StringNode(ASTNode):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class UnaryOpNode(ASTNode):
    def __init__(self, op_type, expr):
        self.op = Token(op_type, op_type)
        self.expr = expr

class CompoundNode(ASTNode):
    def __init__(self):
        self.children = []

class AssignNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class VarNode(ASTNode):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class InputNode(ASTNode):
    def __init__(self, prompt=None):
        self.prompt = prompt

class IfNode(ASTNode):
    def __init__(self, condition, true_body, false_body=None):
        self.condition = condition
        self.true_body = true_body
        self.false_body = false_body

class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class FunctionDefNode(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCallNode(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class ReturnNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message='Invalid syntax'):
        raise Exception(f'{message} at token: {self.current_token}')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f'Expected {token_type}, got {self.current_token.type}')

    def program(self):
        """program : compound_statement"""
        node = self.compound_statement()
        return node

    def compound_statement(self):
        """compound_statement : statement (EOL statement)* [EOL]"""
        nodes = CompoundNode()
        
        nodes.children.append(self.statement())
        
        while self.current_token.type == TokenType.EOL:
            self.eat(TokenType.EOL)
            if self.current_token.type not in (TokenType.EOF, TokenType.RBRACE):
                nodes.children.append(self.statement())
        
        return nodes

    def block(self):
        """block : LBRACE compound_statement RBRACE"""
        self.eat(TokenType.LBRACE)
        node = self.compound_statement()
        self.eat(TokenType.RBRACE)
        return node

    def statement(self):
        """
        statement : assignment_statement
                 | print_statement
                 | input_statement
                 | if_statement
                 | while_statement
                 | function_def
                 | return_statement
                 | expr
        """
        token = self.current_token

        if token.type == TokenType.VAR:
            return self.assignment_statement()
        elif token.type == TokenType.PRINT:
            return self.print_statement()
        elif token.type == TokenType.INPUT:
            return self.input_statement()
        elif token.type == TokenType.IF:
            return self.if_statement()
        elif token.type == TokenType.WHILE:
            return self.while_statement()
        elif token.type == TokenType.FUNCTION:
            return self.function_def()
        elif token.type == TokenType.RETURN:
            return self.return_statement()
        else:
            return self.expr()

    def assignment_statement(self):
        """assignment_statement : VAR variable ASSIGN expr"""
        self.eat(TokenType.VAR)
        var = self.variable()
        token = self.current_token
        self.eat(TokenType.ASSIGN)
        right = self.expr()
        return AssignNode(var, token, right)

    def print_statement(self):
        """print_statement : PRINT expr"""
        self.eat(TokenType.PRINT)
        return PrintNode(self.expr())

    def input_statement(self):
        """input_statement : INPUT (STRING)?"""
        token = self.current_token
        self.eat(TokenType.INPUT)
        prompt = None
        if self.current_token.type == TokenType.STRING:
            prompt = StringNode(self.current_token)
            self.eat(TokenType.STRING)
        return InputNode(prompt)

    def if_statement(self):
        """if_statement : IF expr [FALSE] block"""
        self.eat(TokenType.IF)
        condition = self.expr()
        
        # Handle optional cap token for negation
        if self.current_token.type == TokenType.FALSE:
            condition = UnaryOpNode(TokenType.NOT, condition)
            self.eat(TokenType.FALSE)
            
        true_body = self.block()
        return IfNode(condition, true_body)

    def while_statement(self):
        """while_statement : WHILE expr [FALSE] block"""
        self.eat(TokenType.WHILE)
        condition = self.expr()
        
        # Handle optional cap token for negation
        if self.current_token.type == TokenType.FALSE:
            condition = UnaryOpNode(TokenType.NOT, condition)
            self.eat(TokenType.FALSE)
            
        body = self.block()
        return WhileNode(condition, body)

    def function_def(self):
        """function_def : FUNCTION ID LPAREN param_list RPAREN block"""
        self.eat(TokenType.FUNCTION)
        name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)
        self.eat(TokenType.LPAREN)
        params = self.param_list()
        self.eat(TokenType.RPAREN)
        body = self.block()
        return FunctionDefNode(name, params, body)

    def param_list(self):
        """param_list : ID (COMMA ID)*"""
        params = []
        if self.current_token.type == TokenType.IDENTIFIER:
            params.append(self.current_token.value)
            self.eat(TokenType.IDENTIFIER)
            while self.current_token.type == TokenType.COMMA:
                self.eat(TokenType.COMMA)
                params.append(self.current_token.value)
                self.eat(TokenType.IDENTIFIER)
        return params

    def return_statement(self):
        """return_statement : RETURN expr"""
        self.eat(TokenType.RETURN)
        return ReturnNode(self.expr())

    def expr(self):
        """
        expr : term ((ADD | SUB | EQ | GT | LT) term)*
        """
        node = self.term()

        while self.current_token.type in (
            TokenType.ADD, TokenType.SUB,
            TokenType.EQ, TokenType.LT, TokenType.GT
        ):
            token = self.current_token
            negate = False  # Initialize negate flag
            
            if token.type == TokenType.ADD:
                self.eat(TokenType.ADD)
            elif token.type == TokenType.SUB:
                self.eat(TokenType.SUB)
            elif token.type == TokenType.EQ:
                self.eat(TokenType.EQ)
                # Handle optional cap token for negation
                if self.current_token.type == TokenType.FALSE:
                    negate = True
                    self.eat(TokenType.FALSE)
            elif token.type == TokenType.LT:
                self.eat(TokenType.LT)
            elif token.type == TokenType.GT:
                self.eat(TokenType.GT)

            node = BinOpNode(left=node, op=token, right=self.term())
            if negate:
                # Create a unary not operation
                node = UnaryOpNode(TokenType.NOT, node)

        return node

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()

        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            token = self.current_token
            if token.type == TokenType.MUL:
                self.eat(TokenType.MUL)
            else:
                self.eat(TokenType.DIV)

            node = BinOpNode(left=node, op=token, right=self.factor())

        return node

    def factor(self):
        """factor : NUMBER | STRING | ID | LPAREN expr RPAREN | INPUT STRING?"""
        token = self.current_token

        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return NumberNode(token)
        elif token.type == TokenType.STRING:
            self.eat(TokenType.STRING)
            return StringNode(token)
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            if self.current_token.type == TokenType.LPAREN:
                self.eat(TokenType.LPAREN)
                args = []
                if self.current_token.type != TokenType.RPAREN:
                    args.append(self.expr())
                    while self.current_token.type == TokenType.COMMA:
                        self.eat(TokenType.COMMA)
                        args.append(self.expr())
                self.eat(TokenType.RPAREN)
                return FunctionCallNode(token.value, args)
            return VarNode(token)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        elif token.type == TokenType.INPUT:
            self.eat(TokenType.INPUT)
            prompt = None
            if self.current_token.type == TokenType.STRING:
                prompt = StringNode(self.current_token)
                self.eat(TokenType.STRING)
            return InputNode(prompt)
        else:
            self.error(f'Unexpected token {token.type}')

    def variable(self):
        """variable : ID"""
        node = VarNode(self.current_token)
        self.eat(TokenType.IDENTIFIER)
        return node

    def parse(self):
        node = self.program()
        if self.current_token.type != TokenType.EOF:
            self.error()
        return node
