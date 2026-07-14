import ast

def parse_code(code):
    try:
        tree = ast.parse(code)
        return tree
    except SyntaxError:
        return None
    