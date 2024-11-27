from tokens import TokenType

class NodeVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))

class Interpreter(NodeVisitor):
    def __init__(self):
        self.global_scope = {}
        self.functions = {}

    def visit_NumberNode(self, node):
        return node.value

    def visit_StringNode(self, node):
        return node.value

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        # Try to convert strings to numbers for numeric operations
        if node.op.type in [TokenType.LT, TokenType.GT, TokenType.EQ]:
            try:
                if isinstance(left, str) and left.strip():
                    left = int(left)
                elif isinstance(left, str):
                    left = 0
                if isinstance(right, str) and right.strip():
                    right = int(right)
                elif isinstance(right, str):
                    right = 0
            except ValueError:
                pass
        
        if node.op.type == TokenType.ADD:
            # Handle string concatenation
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        elif node.op.type == TokenType.SUB:
            return left - right
        elif node.op.type == TokenType.MUL:
            return left * right
        elif node.op.type == TokenType.DIV:
            return left / right
        elif node.op.type == TokenType.EQ:
            return left == right
        elif node.op.type == TokenType.GT:
            return left > right
        elif node.op.type == TokenType.LT:
            return left < right
        else:
            raise Exception(f'Unknown operator: {node.op.type}')

    def visit_UnaryOpNode(self, node):
        op_type = node.op.type
        if op_type == TokenType.SUB:
            return -self.visit(node.expr)
        elif op_type == TokenType.NOT:
            return not self.visit(node.expr)
        return self.visit(node.expr)

    def visit_CompoundNode(self, node):
        results = []
        for child in node.children:
            result = self.visit(child)
            if result is not None:  # Only add non-None results
                results.append(result)
        return results[-1] if results else None

    def visit_AssignNode(self, node):
        var_name = node.left.value
        self.global_scope[var_name] = self.visit(node.right)

    def visit_VarNode(self, node):
        var_name = node.value
        val = self.global_scope.get(var_name)
        if val is None:
            raise NameError(f"Variable '{var_name}' is not defined")
        return val

    def visit_PrintNode(self, node):
        value = self.visit(node.expr)
        print(value)

    def visit_InputNode(self, node):
        if node.prompt:
            prompt = self.visit(node.prompt)
        else:
            prompt = ""
        try:
            # Try to convert input to number if possible
            value = input(prompt)
            try:
                return int(value)
            except ValueError:
                try:
                    return float(value)
                except ValueError:
                    return value
        except EOFError:
            return 0  # Return 0 instead of empty string for numeric contexts

    def visit_IfNode(self, node):
        if self.visit(node.condition):
            return self.visit(node.true_body)
        elif node.false_body:
            return self.visit(node.false_body)

    def visit_WhileNode(self, node):
        while self.visit(node.condition):
            self.visit(node.body)

    def visit_FunctionDefNode(self, node):
        self.functions[node.name] = node

    def visit_FunctionCallNode(self, node):
        func = self.functions.get(node.name)
        if not func:
            raise NameError(f"Function '{node.name}' is not defined")

        # Create new scope for function
        old_scope = self.global_scope.copy()
        
        # Bind arguments to parameters
        if len(node.args) != len(func.params):
            raise ValueError(f"Expected {len(func.params)} arguments, got {len(node.args)}")
        
        for param, arg in zip(func.params, node.args):
            self.global_scope[param] = self.visit(arg)

        # Execute function body
        try:
            self.visit(func.body)
            return None
        except ReturnValue as rv:
            return rv.value
        finally:
            self.global_scope = old_scope

    def visit_ReturnNode(self, node):
        raise ReturnValue(self.visit(node.expr))

    def interpret(self, tree):
        return self.visit(tree)

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value
