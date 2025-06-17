



import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()





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
        return "Please say something!", history

    import speech_recognition as sr
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
        except Exception as e:
            return f"Speech recognition failed: {e}", history

    history = history or []
    history.append(("User", text))

    prompt = PERSONA_CONTEXT + "\n"
    for human, bot in zip(history[::2], history[1::2]):
        prompt += f"User: {human[1]}\nBot: {bot[1]}\n"
    if len(history) % 2 == 1:
        prompt += f"User: {history[-1][1]}\nBot:"

    try:
        response = model.generate_content(prompt)
        answer = response.text.strip()
    except Exception as e:
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













# import gradio as gr
# from openai import OpenAI

# # Directly pass your API key here (NOT recommended for shared/public code)
# client = OpenAI(api_key="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")

# def chat_with_gpt(audio_file, history):
#     if audio_file is None:
#         return "Please say something!", history

#     # Transcribe audio using Whisper (new OpenAI SDK syntax)
#     try:
#         with open(audio_file, "rb") as f:
#             transcription = client.audio.transcriptions.create(
#                 model="whisper-1",
#                 file=f
#             )
#         text = transcription.text
#     except Exception as e:
#         return f"Transcription failed: {e}", history

#     # Build conversation history
#     history = history or []
#     history.append(("User", text))

#     messages = [
#         {"role": "system", "content": "You are Anant, a confident and curious candidate interviewing for Home.LLC's AI Agent team. Answer like you're talking directly to the CEO."}
#     ]

#     # Add previous exchanges to message history
#     for human, bot in zip(history[::2], history[1::2]):
#         messages.append({"role": "user", "content": human[1]})
#         messages.append({"role": "assistant", "content": bot[1]})
#     if len(history) % 2 == 1:
#         messages.append({"role": "user", "content": history[-1][1]})

#     # Call OpenAI ChatGPT API (new syntax)
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o",
#             messages=messages
#         )
#         answer = response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"OpenAI response failed: {e}", history

#     # Save to history
#     history.append(("Bot", answer))
#     return answer, history

# iface = gr.Interface(
#     fn=chat_with_gpt,
#     inputs=[
#         gr.Audio(sources=["microphone"], type="filepath", label="🎙️ Speak your interview question"),
#         gr.State()
#     ],
#     outputs=[
#         gr.Textbox(label="🤖 Bot's Response"),
#         gr.State()
#     ],
#     title="🏠 Home.LLC Interview Voice Bot by Anant Srivastav",
#     description="🎤 Speak a question and hear how Anant would respond in the interview. Powered by Whisper + GPT-4o."
# )

# if __name__ == "__main__":
#     iface.launch()


















