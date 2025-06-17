#  AI Cover Letter Generator – Powered by Gemini

This app generates **personalized cover letters** using Google Gemini 1.5 Flash. Just paste your resume, enter a job title and company name — and receive a recruiter-ready, customized letter in seconds!

---

##  Features

-  Role-aware prompting with Gemini
-  Prompt chaining (Resume ➝ Skills ➝ Cover Letter)
-  Clear tone, motivation, and suitability
- Clean UI built using Gradio
- Uses `.env` for secure API key handling

---

##  Tech Stack

- `Gradio`
- `Google Generative AI (Gemini)`
- `python-dotenv`
- Prompt Engineering

---

##  How It Works

### Input:
- Resume (Text only)
- Job Title (e.g., Prompt Engineer)
- Company Name (e.g., Google)

### Output:
A cover letter tailored to the job and company, written in a confident and professional tone.

---

##  Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/imantasha/cover-letter-generator.git
cd cover-letter-generator
Create .env file
GEMINI_API_KEY=your_gemini_key_here



Install dependencies
pip install -r requirements.txt


Run the app
python cover_letter_app.py
