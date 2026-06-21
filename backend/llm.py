import os
import json
import re
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")



def build_prompt(text):
    return f"""
You are an expert ATS Resume Analyzer.

Analyze ONLY the resume content provided below.

Rules:
- Do not hallucinate information.
- Do not assume skills, education, or experience not explicitly present.
- Be objective and ATS-focused.
- Return ONLY valid JSON.
- No markdown.
- No explanations outside JSON.

Required JSON format:

{{
  "ats_score": 0,
  "overall_score": 0,
  "skills_found": [],
  "missing_skills": [],
  "strengths": [],
  "weaknesses": [],
  "improvements": [],
  "experience_analysis": "",
  "education_analysis": "",
  "final_summary": ""
}}

Resume:
\"\"\"
{text}
\"\"\"
"""


def parse_ai_response(content):


    content = re.sub(r"```json", "", content, flags=re.IGNORECASE)
    content = re.sub(r"```", "", content)

    content = content.strip()

    return json.loads(content)


def analyze_resume(text):


    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "user",
                "content": build_prompt(text)
            }
        ],
        "temperature": 0.2,
        "max_tokens": 1500
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            return {
                "error": "Groq API request failed",
                "status_code": response.status_code,
                "details": response.text
            }

        result = response.json()

        content = result["choices"][0]["message"]["content"]

        try:
            return parse_ai_response(content)

        except Exception:
            return {
                "error": "Invalid JSON returned by AI",
                "raw_response": content
            }

    except requests.exceptions.Timeout:
        return {
            "error": "Request timed out"
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }