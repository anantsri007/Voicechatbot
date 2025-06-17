import gradio as gr
import google.generativeai as genai

# Directly set the Gemini API key
genai.configure(api_key="AIzaSyBoI-KIbYxbThZL9-2q8nqmXnzdTcnzozo")

# Initialize Gemini model (use the latest available)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

PERSONA_CONTEXT = """
You are Anant Srivastava, a Software Developer with a B.Tech in Electronics & Telecommunication from Bharati Vidyapeeth College of Engineering, Pune (GPA: 7.8). 
You have hands-on experience with C++, JavaScript, Python, Go, and frameworks like Express, Node, Django, and Gin. 
Your expertise includes MySQL, SQLite, MongoDB, Redis, and deploying scalable systems with CI/CD and AWS. 
You interned at Times Network, building AI chatbots, YouTube migration tools, WhatsApp data categorization systems, and Twitter engagement analytics. 
You are known for problem-solving, team collaboration, technical documentation, and time management.
Established in 2019, Home.LLC is dedicated to addressing challenges in the housing market. Our mission is to alleviate
the home ownership crisis in America by streamlining the process of buying, owning, and selling homes for greater efficiency and effectiveness. 
Answer all questions confidently and concisely in first person, as if speaking directly to the CEO.
"""

def chat_with_gemini(audio_file, history):
    if audio_file is None:
        return "Please upload an audio file!", history

    # Here, you would normally transcribe the audio to text.
    # Since Render doesn't allow PyAudio/SpeechRecognition, either:
    # - Use a third-party speech-to-text API (like Google Cloud Speech-to-Text), or
    # - Ask users to upload a text file instead, or
    # - (As below) just inform the user that transcription is not supported.
    return "Audio transcription is not supported in this deployment. Please provide your question as text.", history

iface = gr.Interface(
    fn=chat_with_gemini,
    inputs=[
        gr.Audio(type="filepath", label="Upload your interview question (audio file)"),
        gr.State()
    ],
    outputs=[
        gr.Textbox(label="🤖 Bot's Response"),
        gr.State()
    ],
    title="🏠 Home.LLC Interview Voice Bot by Anant Srivastava (Gemini)",
    description="🎤 Upload a question as audio (transcription not supported in this demo). Powered by Google Gemini."
)

if __name__ == "__main__":
    iface.launch()



        answer = f"Gemini API error: {e}"

    history.append(("Bot", answer))
    return answer, history

iface = gr.Interface(
    fn=chat_with_gemini,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath", label="🎙️ Speak your interview question"),
        gr.State()
    ],
    outputs=[
        gr.Textbox(label="🤖 Bot's Response"),
        gr.State()
    ],
    title="🏠 Home.LLC Interview Voice Bot by Anant Srivastava (Gemini)",
    description="🎤 Speak a question and hear how Anant would respond in the interview. Powered by Google Gemini."
)

if __name__ == "__main__":
    iface.launch()



