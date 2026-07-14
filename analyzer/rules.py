import ast

def check_print_statements(tree):
    findings = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id == "print":
                    findings.append("Print statement detected.")

    return findings

def check_functions(tree):
    findings = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            findings.append(f"Function defined: {node.name}")

    return(findings)

def check_loops(tree):
    findings = []

    for node in ast.walk(tree):
        if isinstance(node, ast.For):
            findings.append("For loop detected.")

        elif isinstance(node, ast.While):
            findings.append("While loop detected")

    return findings

def check_empty_except(tree):
    findings = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler):
            if len(node.body) == 1 and isinstance(node.body[0], ast.Pass):
                findings.append("Empty except block detected.")  

    return findings

def check_unused_variables(tree):

    assigned = set()
    used = set()

    for node in ast.walk(tree):

        if isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):
                    assigned.add(target.id)

        elif isinstance (node, ast.Name):

            if isinstance(node.ctx, ast.Load):
                used.add(node.id)

    findings = []

    for variable in assigned - used:
        findings.append(f"Unused variable: {variable}")

    return findings

def check_unused_functions(tree):

    defined = set()
    called = set()

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            defined.add(node.name)

        elif isinstance(node, ast.Call):

            if isinstance(node.func, ast.Name):
                called.add(node.func.id)

    findings = []

    for function in defined - called:
        findings.append(
            f"Function '{function}' is defined but never called."
        )

    return findings 

def check_function_parameters(tree):
    findings = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            parameter_count = len(node.args.args)

            if parameter_count > 3:

                findings.append(
                    f"Function '{node.name}' has {parameter_count} parameters. Consider simplifying it."
                )

    return findings
                                                                                       