def generate_description(function_name):

    words = function_name.replace("_", " ")

    return f"This function is used to {words}."


def create_documentation(functions, classes):

    docs = ""

    # Functions
    for func in functions:

        description = generate_description(
            func["name"]
        )

        docs += f"""
Function: {func['name']}

Description:
{description}

Parameters:
{', '.join(func['args'])}

--------------------------------
"""

    # Classes
    for cls in classes:

        docs += f"""
Class: {cls['name']}

Description:
This class represents {cls['name']}.

--------------------------------
"""

    return docs