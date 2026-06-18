import ast

def extract_code_info(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()

    tree = ast.parse(code)

    functions = []
    classes = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            functions.append({
                "name": node.name,
                "args": [arg.arg for arg in node.args.args],
                "code": ast.unparse(node)
        })

        elif isinstance(node, ast.ClassDef):

            classes.append({
                "name": node.name
            })

    return functions, classes
