from openai import OpenAI
from config import API_KEY
from analyzer.ast_parser import parse_code
from analyzer.rules import (
    check_print_statements, 
    check_functions,
    check_loops,
    check_empty_except,
    check_unused_variables,
    check_unused_functions, 
    check_function_parameters 
)


client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def error_response(message):
    return {
        "success": False,
        "data": None,
        "error": message
    }

def success_response(review):
    return {
        "success": True,
        "data": {
            "review": review
        },
        "error": None
    }

def review_code(code):

    if not isinstance(code, str):
        return error_response("Code must be a string")
    
    if not code.strip():
        return error_response("No code provided")
    
    tree = parse_code(code)
    
    if tree is None:
        return error_response("Invalid Python Syntax")
    
    print_findings = check_print_statements(tree)

    function_findings = check_functions(tree)

    loop_findings = check_loops(tree) 

    except_findings = check_empty_except(tree)

    unused_variable_findings = check_unused_variables(tree) 

    unused_function_findings = check_unused_functions(tree)

    parameter_findings = check_function_parameters(tree)
    
    findings = []

    findings.extend(print_findings)
    findings.extend(function_findings)
    findings.extend(loop_findings) 
    findings.extend(except_findings)
    findings.extend(unused_variable_findings)
    findings.extend(unused_function_findings)
    findings.extend(parameter_findings)

    
    # Convert the list into text
    if findings:
        findings_text = "\n".join(f"- {item}" for item in findings)
    else:
        findings_text = "No issues detected."
    
    prompt = f"""
You are an expert Python code reviewer.

A rule-based static analyzer has already analyzed this code.

Static Analysis Findings:
{findings_text}

Review the following Python code.

Use the static analysis findings if they are correct.
If you find additional issues that were not detected, include them as well.
Do not repeat the same issue multiple times.

Return your review in EXACTLY this format:

Bugs:
- ...

Correctness:
- ...

Code Quality:
- ...

Best Practices:
- ...

Optimization:
- ...

Do not invent new headings.
Do not mix languages.
Do not use Markdown code fences.
Keep the review under 150 words.
Use English only.
Do not generate words, characters, or sentences in any language other than English.
If you are unsure, omit the sentence instead of producing text in another language.
Do not invent variable names or modify existing variable names.

Code:

{code}
"""
    
    try:
       response = client.chat.completions.create(
           model="openai/gpt-oss-20b:free",
           messages=[
               {
                   "role": "user",
                   "content": prompt
               }
           ]
       )

       review = response.choices[0].message.content

       return success_response(review)
    
    except Exception as e:
        return error_response(str(e))

