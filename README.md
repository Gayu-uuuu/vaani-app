Vaani – Your Voice, Your Power

Vaani is an AI-powered English learning app that helps users improve vocabulary, conversational skills, and pronunciation. Its unique feature: learn English through your native language, making English learning intuitive, effective, and accessible for second-language learners—something no other app currently offers.

Why Vaani?

Unique learning approach: English lessons explained through the learner’s native language.

Interactive & engaging: Voice-based practice helps learners speak naturally.

AI-powered feedback: OpenAI API provides real-time corrections, translations, and suggestions.

Boosts confidence for second-language learners: Practice pronunciation, sentence formation, and conversation effortlessly.

Learning English through your native language is made possible by AI—giving every learner the confidence to communicate globally.

Core Features

Voice-based interaction for natural learning.

Multilingual support with native language explanations.

Preloaded modules for greetings, vocabulary, and conversational phrases.

AI feedback (currently general; future: personalized and adaptive).

Lightweight and easy to use, built with Flask and Python.

Installation

Clone the repository:

git clone https://github.com/<your-username>/vaani-app.git
cd vaani-app


Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Add .env with API keys:

SECRET_KEY=your_secret_key
DEESEEK_API_KEY=your_openai_api_key

Run Locally
flask run


Open http://127.0.0.1:5000
 in your browser.

Future Plans

Personalized AI feedback adapting to each learner’s progress.

Gamification: badges, levels, and streaks to motivate users.

Expanded modules with advanced vocabulary and conversational practice.

Mobile-friendly UI and enhanced speech-to-text capabilities.

Deployment

Can be deployed on Render, Heroku, or any Python-friendly hosting.

Use pip install -r requirements.txt as build command and gunicorn app:app as start command.

Add environment variables via the hosting dashboard; do not push .env.

Contributing

Fork the repository

Submit pull requests for new modules, AI improvements, and UI enhancements
License

MIT License © 2025 Vaani Project Team

Closing Statement

Vaani is the only app that enables learners to master English through their native language, powered by AI, helping users speak, understand, and excel globally.
