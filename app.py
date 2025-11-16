from flask import Flask, render_template, request, redirect, url_for, session
import os
import random
import openai

app = Flask(__name__)
app.secret_key = "vaani_secret_key"

# -----------------------------
# Set your OpenAI API Key
# -----------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")

# -----------------------------
# Preloaded Modules and Lessons
# -----------------------------
modules_data = {
    "greetings": {
        "english": "Learn basic greetings: Hello, Good Morning, How are you?",
        "Hindi": "आम शब्द सीखें: हेलो, सुप्रभात, आप कैसे हैं?",
        "Tamil": "அடிப்படை வரவேற்புகளை கற்றுக்கொள்ளுங்கள்: ஹலோ, காலை வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?"
    },
    "introductions": {
        "english": "Learn to introduce yourself and ask someone's name.",
        "Hindi": "अपने बारे में बताना और किसी का नाम पूछना सीखें।",
        "Tamil": "உங்களை அறிமுகப்படுத்தவும் ஒருவரின் பெயரை கேட்கவும் கற்றுக்கொள்ளுங்கள்."
    }
}

# -----------------------------
# Helper: Get OpenAI Feedback
# -----------------------------
def get_feedback(prompt_text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an English tutor and mindset/confidence coach. Help non-native speakers improve their English. Give clear, constructive, encouraging feedback."},
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.7,
            max_tokens=250
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI API failed:", e)
        return None  # fallback to preloaded or generic feedback


# -----------------------------
# Landing Page
# -----------------------------
@app.route('/')
def index():
    return render_template('index.html')


# -----------------------------
# Language Selection
# -----------------------------
@app.route('/language_select', methods=['GET', 'POST'])
def language_select():
    if request.method == 'POST':
        session['user_lang'] = request.form.get('language', 'Hindi')
        return redirect(url_for('language_confirm'))
    return render_template('language_select.html')


# -----------------------------
# Language Confirmation
# -----------------------------
@app.route('/language_confirm', methods=['GET', 'POST'])
def language_confirm():
    user_lang = session.get('user_lang', 'Hindi')
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('language_confirm.html', user_lang=user_lang)


# -----------------------------
# Dashboard
# -----------------------------
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# -----------------------------
# Modules Page (Dual Column)
# -----------------------------
@app.route('/module/<module_name>')
def show_module(module_name):
    user_lang = session.get('user_lang', 'Hindi')
    module = modules_data.get(module_name, {})
    english_lesson = module.get('english', "Lesson not found.")
    user_lesson = module.get(user_lang, english_lesson)
    return render_template('module_dual.html',
                           module_name=module_name,
                           english_lesson=english_lesson,
                           user_lesson=user_lesson,
                           user_lang=user_lang)


# -----------------------------
# Practice Page with OpenAI Feedback
# -----------------------------
@app.route('/practice/<module_name>', methods=['GET', 'POST'])
def practice(module_name):
    user_lang = session.get('user_lang', 'Hindi')
    module = modules_data.get(module_name, {})
    questions = [
        {"question": module.get('english', 'Practice this sentence.')},
    ]
    feedback = None

    if request.method == 'POST':
        user_answer = request.form.get('answer', '')
        # Create prompt for AI
        prompt_text = f"Question: {questions[0]['question']}\nStudent Answer: {user_answer}\nProvide feedback, corrections, and encouragement."
        ai_feedback = get_feedback(prompt_text)
        feedback = ai_feedback if ai_feedback else f"Your answer: '{user_answer}'. Keep practicing!"  # fallback

    return render_template('practice.html',
                           module_name=module_name,
                           practice_questions=questions,
                           feedback=feedback)


# -----------------------------
# VaaniTedEx with OpenAI Feedback
# -----------------------------
@app.route('/tedex', methods=['GET', 'POST'])
def tedex():
    topics = ["Introduce yourself", "Talk about your hobbies", "Describe your city"]
    topic = random.choice(topics)
    feedback = None
    user_response = None

    if request.method == 'POST':
        user_response = request.form.get('response', '')
        prompt_text = f"Topic: {topic}\nStudent Response: {user_response}\nProvide detailed, friendly feedback focusing on grammar, clarity, confidence, and fluency."
        ai_feedback = get_feedback(prompt_text)
        feedback = ai_feedback if ai_feedback else f"Feedback for your response: '{user_response}'. Good effort!"  # fallback

    return render_template('tedex.html', topic=topic, feedback=feedback, user_response=user_response)


# -----------------------------
# Diary Page
# -----------------------------
@app.route('/diary')
def diary():
    entries = session.get('diary_entries', [])
    return render_template('diary.html', entries=entries)


# -----------------------------
# Streak Page
# -----------------------------
@app.route('/streak')
def streak():
    streak_count = session.get('streak_count', 0)
    return render_template('streak.html', streak_count=streak_count)


# -----------------------------
# Run the App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
