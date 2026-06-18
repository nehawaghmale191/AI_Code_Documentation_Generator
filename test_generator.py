from parser import extract_code_info
from generator import create_documentation

functions, classes = extract_code_info("sample.py")

docs = create_documentation(functions)

print(docs)