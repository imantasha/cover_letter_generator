import os
import gradio as gr
from dotenv import load_dotenv
import google.generativeai as genai

# Load Gemini API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-1.5-flash")

# Prompt Chain Function
def generate_cover_letter(resume, job_title, company):
    extract_skills_prompt = f"""
You are a professional resume analyzer. From this resume, extract 4–6 relevant skills and achievements that match the job role: {job_title}.

Resume:
{resume}
"""
    try:
        # Step 1: Extract Skills
        skill_response = model.generate_content(extract_skills_prompt)
        extracted_skills = skill_response.text

        # Step 2: Generate Cover Letter
        cover_letter_prompt = f"""
You are an expert career coach.

Using the following skills:
{extracted_skills}

Write a confident, personalized cover letter for a job application to {company} for the position of {job_title}.

Keep it under 200 words. Highlight motivation and suitability.
"""
        letter_response = model.generate_content(cover_letter_prompt)
        return letter_response.text

    except Exception as e:
        return f" Error: {e}"

# Gradio UI
with gr.Blocks() as app:
    gr.Markdown("##  AI Cover Letter Generator")
    gr.Markdown("Paste your Resume, enter Job Title and Company Name. Get a custom cover letter powered by Gemini.")

    resume_input = gr.Textbox(lines=10, label=" Resume Text")
    job_title = gr.Textbox(label="Job Title")
    company_name = gr.Textbox(label=" Company Name")
    output = gr.Textbox(lines=10, label=" Generated Cover Letter")

    btn = gr.Button("Generate Cover Letter")
    btn.click(generate_cover_letter, inputs=[resume_input, job_title, company_name], outputs=output)
    gr.Markdown("---")
    gr.Markdown("© 2025 Mantasha Idrisi. All rights reserved.", elem_id="footer")

if __name__ == "__main__":
    app.launch()
