# AI-Powered Code Review Assistant

## Overview

AI-Powered Code Review Assistant is a Flask-based web application that reviews Python code by combining **rule-based static analysis** using Python's **Abstract Syntax Tree (AST)** with **AI-generated feedback** from an LLM.

Instead of relying only on an AI model, the application first analyzes the code structure using AST to detect common issues such as print statements, loops, unused variables, unused functions, empty exception blocks, and functions with too many parameters. These findings are then provided to the AI to generate a more comprehensive and structured code review.

---

## Features

* Static code analysis using Python AST
* Detection of:

  * Print statements
  * For loops
  * While loops
  * Empty `except` blocks
  * Unused variables
  * Unused functions
  * Functions with excessive parameters
* AI-powered code review using OpenRouter
* Structured review covering:

  * Bugs
  * Correctness
  * Code Quality
  * Best Practices
  * Optimization
* Modular project architecture following the Single Responsibility Principle (SRP)

---

## Tech Stack

* Python
* Flask
* Python AST (`ast`)
* OpenRouter API
* OpenAI Python SDK
* python-dotenv

---

## Project Structure

```text
AI-Code-Review-Assistant/
│
├── analyzer/
│   ├── ast_parser.py
│   ├── rules.py
│   └── __init__.py
│
├── reviewer/
│   ├── reviewer.py
│   └── __init__.py
│
├── app.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How It Works

1. The user submits Python code through the Flask API.
2. The code is parsed into an Abstract Syntax Tree (AST).
3. Rule-based analysis identifies common coding issues.
4. The detected findings are combined into a prompt.
5. The prompt is sent to an LLM using OpenRouter.
6. The model returns a structured code review.

---

## API Endpoint

### Review Code

**POST**

```
/review
```

### Request

```json
{
    "code": "print('Hello World')"
}
```

### Response

```json
{
    "success": true,
    "data": {
        "review": "Bugs:\n- ...\n\nCorrectness:\n- ...\n\nCode Quality:\n- ...\n\nBest Practices:\n- ...\n\nOptimization:\n- ..."
    },
    "error": null
}
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
API_KEY=YOUR_OPENROUTER_API_KEY
```

Run the application:

```bash
python app.py
```

The server starts on:

```
http://127.0.0.1:5008
```

---

## Future Improvements

* GitHub Pull Request integration
* Additional AST rules
* Multi-language support
* Severity-based issue classification
* Automatic code fixes
* Web frontend for code submission

---

## Learning Outcomes

Through this project I learned:

* Flask API development
* REST API design
* Environment variable management
* Python AST parsing
* Rule-based static code analysis
* Prompt engineering
* Integration with LLM APIs
* Modular software design using SRP
* Git and GitHub workflow
