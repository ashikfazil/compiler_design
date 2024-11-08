from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Placeholder function to simulate AST generation from Solidity code
# Placeholder function to simulate AST generation from Solidity code
def parse_solidity(code):
    ast = []
    for line in code.splitlines():
        # Rule for variable declaration
        if match := re.match(r'(\w+)\s+(\w+)\s*=\s*(.*);', line):
            var_type, var_name, var_value = match.groups()
            ast.append({
                "type": "VariableDeclaration",
                "data_type": var_type,
                "name": var_name,
                "value": var_value
            })
        # Rule for function declaration
        elif match := re.match(r'function\s+(\w+)\((.*?)\)\s*(public|private|internal|external)?\s*(view|pure|payable)?\s*(.*)', line):
            func_name, params, visibility, mutability, return_type = match.groups()
            ast.append({
                "type": "FunctionDeclaration",
                "name": func_name,
                "parameters": params.split(', ') if params else [],
                "visibility": visibility,
                "mutability": mutability,
                "return_type": return_type
            })
        elif "if" in line:
            ast.append({
                "type": "Conditional",
                "condition": line.strip()
            })
        elif "for" in line or "while" in line:
            ast.append({
                "type": "Loop",
                "statement": line.strip()
            })
        # Add more parsing rules for different constructs

    return ast


@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/styles.css')
def serve_css():
    return app.send_static_file('styles.css')

@app.route('/script.js')
def serve_js():
    return app.send_static_file('script.js')


@app.route('/parse', methods=['POST'])
def parse():
    data = request.get_json()
    code = data.get("code", "")
    print("Received Solidity code:", code)  # Debugging line
    ast = parse_solidity(code)
    print("Generated AST:", ast)  # Debugging line
    return jsonify({"ast": ast})


if __name__ == '__main__':
    app.run(debug=True)