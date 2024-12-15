from tokens import TokenType

import random

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
        
        # Handle dictionary operations
        if isinstance(left, dict):
            if node.op.type == TokenType.ADD:
                # Merge dictionaries
                result = left.copy()
                result.update(right)
                return result
            elif node.op.type == TokenType.SUB:
                # Remove keys
                result = left.copy()
                if isinstance(right, (list, tuple)):
                    for key in right:
                        result.pop(key, None)
                else:
                    result.pop(right, None)
                return result

        # Handle string concatenation
        if node.op.type == TokenType.ADD:
            if isinstance(right, str) and right == "skip":
                print(left, end="")
                return right
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

    def visit_DictNode(self, node):
        # Create a dictionary from the key-value pairs
        result = {}
        for key_node, value_node in node.items:
            key = self.visit(key_node)
            value = self.visit(value_node)
            result[key] = value
        return result

    def visit_DictAccessNode(self, node):
        # Get the dictionary and key values
        dict_obj = self.visit(node.dict_node)
        key = self.visit(node.key_node)
        
        # Check if the object is a dictionary
        if not isinstance(dict_obj, dict):
            raise Exception(f'Cannot access key {key} on non-dictionary object')
            
        # Check if the key exists
        if key not in dict_obj:
            raise Exception(f'Key not found: {key}')
            
        return dict_obj[key]

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
        if var_name == "skip":
            return "skip"
        val = self.global_scope.get(var_name)
        if val is None:
            raise NameError(f"Erm What The Sigma? Variable '{var_name}' is not defined")
        return val

    def visit_PrintNode(self, node):
        value = self.visit(node.expr)
        if isinstance(value, str) and value == "skip":
            print()  # Just print a newline
        else:
            print(value, end="")

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
            raise NameError(f"Erm What The Sigma? Function '{node.name}' is not defined")

        # Create new scope for function
        old_scope = self.global_scope.copy()
        
        # Bind arguments to parameters
        if len(node.args) != len(func.params):
            raise ValueError(f"Erm What The Sigma? Expected {len(func.params)} arguments, got {len(node.args)}")
        
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
    
    def visit_RandomNode(self, node):
        return random.random()
    
    def visit_RandomIntNode(self, node):
        min_val = int(self.visit(node.min_val))
        max_val = int(self.visit(node.max_val))
        return random.randint(min_val, max_val)
    
    def visit_RandomChoiceNode(self, node):
        choices = [self.visit(choice) for choice in node.choices]
        return random.choice(choices)

    def interpret(self, tree):
        return self.visit(tree)

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value
