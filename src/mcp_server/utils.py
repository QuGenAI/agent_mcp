import ast
import inspect
import json

def convert_function_to_json(func):
    source = inspect.getsource(func)
    parsed = ast.parse(source)

    func_def = parsed.body[0]
    func_name = func_def.name

    docstring = ast.get_docstring(func_def)
    doc_lines = docstring.strip().split('\n')
    
    # Extract description
    description_line = next((line for line in doc_lines if "description" in line), "")
    description = description_line.split(":", 1)[-1].strip().strip('"')

    # Extract parameter defaults from docstring
    param_descriptions = {}
    in_params = False
    for line in doc_lines:
        if "Parameters:" in line:
            in_params = True
            continue
        if in_params:
            if ':' in line and '=' in line:
                param, rest = line.split(":", 1)
                _, desc = rest.split("=")
                param_descriptions[param.strip()] = desc.strip().strip('"')

    input_schema = {
        "type": "object",
        "properties": {},
        "required": []
    }

    for arg in func_def.args.args:
        name = arg.arg
        input_schema["properties"][name] = {
            "type": "string",
            "description": param_descriptions.get(name, "")
        }
        input_schema["required"].append(name)

    result = {
        "name": func_name,
        "description": description,
        "inputSchema": input_schema
    }

    return json.dumps(result, indent=4)