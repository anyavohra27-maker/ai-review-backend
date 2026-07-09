from openai import OpenAI
from config import API_KEY

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
    
    prompt = f"""
You are an expert Python code reviewer.

Review the following Python code.

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

# import requests
# from config import API_KEY

# def review_code(code):
#     url = "https://jsonplaceholder.typicode.com/posts"

#     headers = {
#         "Authorization":  f"Bearer {API_KEY}"
#     }

#     prompt = f"""
# You are an expert Python code reviewer.

# Review the following Python code.

# Check for:
# - Bugs
# - Code quality
# - Best practices
# - Optimization suggestions

# Code:

# {code}
# """

#     data = {
#         "model": "gpt-4.1-mini",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": prompt 
#             }
#         ],
#         "temperature": 0.2,
#         "max_tokens": 300
#     }

#     try:
#         response = requests.post(
#             url,
#             json=data,
#             headers=headers
#         )
        
#         if response.status_code == 200:
#             result = response.json()
#             review = result["choices"][0]["message"]["content"] 

#             return {
#                 "success": True,
#                 "data": {
#                     "review": "Code received successfully",
#                     "submitted_code": result["body"],
#                     "review_id": result["id"]
#                 },
#                 "error": None
#             }
        
#         elif response.status_code == 401:
#             return {
#                 "success": False,
#                 "data": None,
#                 "error": "Invalid API key"
#             }
        
#         elif response.status_code == 429:
#             return {
#                 "success": False,
#                 "data": None,
#                 "error": "Rate limit exceeded"
#             }
        
#         elif response.status_code >= 500:
#             return {
#                 "success": False,
#                 "data": None,
#                 "error": "AI server error"
#             }
        
#         else: 
#             return {
#                 "success": False,
#                 "data": None,
#                 "error": "API Error"
#             }

#     except requests.exceptions.ConnectionError:
#         return {
#             "success": False,
#             "data": None,
#             "error": "Connection Failed"
#         }    

# Day 6
# def review_code(code):
#     feedback = []

#     if code == "":
#         return {
#             "error": "No code provided"
#         }    
    
#     lines = code.split("\n")

#     if len(lines)>10:
#         feedback.append("Code is too long")

#     if "a =" in code or "x =" in code:
#         feedback.append("Variable names are too generic")

#     if len(lines) != len(set(lines)):
#         feedback.append("Repeated lines detected")

#     if "def" not in code:
#         feedback.append("No function found")

#     if "for" in code:
#         feedback.append("Loop detected")
        
#     if "if" in code:
#         feedback.append("Condition detected")    

#     if "print" in code:
#         feedback.append("Print statement detected")

#     feedback.append("Analysis complete")

#     return {
#         "feedback": feedback
#     }




# DAY 2
# import requests

# def review_code(code):
#     data = {
#         "code": code
#     }

#     response = requests.post(
#         "API_URL",
#         json=data
#     )

#     result = response.json()

#     return result


