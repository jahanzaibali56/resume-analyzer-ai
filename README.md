# Resume Analyzer AI

An AI-powered Resume Analyzer built using React, Flask, and Large Language Models (LLMs). The application allows users to upload or paste resume content and receive a professional ATS-focused evaluation report with scores, skill analysis, strengths, weaknesses, and improvement recommendations.

---

## Features

### Resume Input

* Upload PDF resumes
* Upload DOCX resumes
* Paste resume text directly
* Automatic text extraction and cleaning

### AI-Powered Analysis

* ATS Compatibility Score
* Overall Resume Score
* Skills Extraction
* Missing Skills Detection
* Strengths Identification
* Weakness Detection
* Resume Improvement Suggestions
* Experience Evaluation
* Education Analysis
* Professional Summary Generation

### Interactive Dashboard

* ATS Score Meter
* Overall Score Card
* Skills Found Section
* Missing Skills Section
* Strengths Panel
* Weaknesses Panel
* Improvement Suggestions
* Experience Analysis
* Education Analysis
* Final Resume Summary

---

## Tech Stack

### Frontend

* React.js
* JavaScript
* HTML5
* CSS3

### Backend

* Flask
* Python

### AI Integration

* Groq API
* Llama 3.3 70B Versatile

### Resume Processing

* pdfplumber
* python-docx

---

## Project Structure

```text
resume-analyzer-ai/
│
├── README.md
├── .gitignore
│
├── backend/
│   ├── app.py
│   ├── llm.py
│   ├── parser.py
│   ├── utils.py
│   ├── requirements.txt
│   └── .env
│
└── frontend/
    ├── public/
    ├── src/
    ├── package.json
    └── package-lock.json
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/jahanzaibali56/resume-analyzer-ai.git
cd resume-analyzer-ai
```

---

## Backend Setup

Navigate to backend directory:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Run Flask server:

```bash
python app.py
```

Backend will start on:

```text
http://127.0.0.1:5000
```

---

## Frontend Setup

Navigate to frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start React application:

```bash
npm start
```

Frontend will start on:

```text
http://localhost:3000
```

---

## API Endpoint

### Analyze Resume

**POST**

```http
/api/analyze
```

### Request

Form Data:

```text
file : PDF or DOCX Resume
```

or

```text
text : Resume Content
```

### Sample Response

```json
{
  "ats_score": 82,
  "overall_score": 85,
  "skills_found": [
    "Python",
    "Flask",
    "React",
    "SQL"
  ],
  "missing_skills": [
    "Docker",
    "AWS"
  ],
  "strengths": [
    "Strong technical skills"
  ],
  "weaknesses": [
    "Limited cloud experience"
  ],
  "improvements": [
    "Add cloud-based projects"
  ],
  "experience_analysis": "...",
  "education_analysis": "...",
  "final_summary": "..."
}
```

---



## Future Improvements

* Job Description Matching
* Resume Ranking System
* PDF Report Export
* User Authentication
* Resume History Tracking
* Multi-Language Support
* Cloud Deployment
* Interview Question Generator

---

## Author

**Jahanzaib Ali**

Computer Engineering Student
COMSATS University Islamabad, Lahore Campus

GitHub:
https://github.com/jahanzaibali56

LinkedIn:
https://www.linkedin.com/in/jahanzaib-ali-90b6b8321

---
