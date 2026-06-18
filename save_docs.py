from parser import extract_code_info
from generator import create_documentation

functions, classes = extract_code_info("sample.py")

docs = "# Auto Generated Documentation\n\n"

docs += create_documentation(functions)

with open("docs/README.md", "w", encoding="utf-8") as file:
    file.write(docs)

print("README Generated")