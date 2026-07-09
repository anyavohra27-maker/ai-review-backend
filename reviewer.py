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

