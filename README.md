# Content Moderation API

An AI-powered REST API for moderating user-generated content using Large Language Models (LLMs). This project is built with FastAPI and currently uses Ollama as the inference provider, with an architecture designed to support multiple LLM providers in the future.

## Features

- 🤖 AI-powered content moderation
- 🚫 Detects profanity
- 🛡️ Detects SARA (Ethnicity, Religion, Race, and Inter-group issues)
- 💬 Detects harassment and abusive language
- 🧠 Context-aware moderation (not keyword matching)
- ⚡ FastAPI REST API
- 📖 Interactive Swagger documentation
- 🔌 Provider-agnostic architecture
- 🏠 Local inference using Ollama

## Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn
- Ollama
- Qwen 2.5

## Project Structure

```text
content-moderation-api/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── schemas.py
│   ├── prompts.py
│   ├── config.py
│   └── main.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nicojonathan/content-moderation-api.git
cd content-moderation-api
```

### 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com

### 5. Download the model

```bash
ollama run qwen2.5:7b
```

### 6. Configure environment variables

Create a `.env` file.

```env
OLLAMA_MODEL=qwen2.5:7b
```

### 7. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API

### POST `/moderate`

Request

```json
{
  "text": "Dasar kafir."
}
```

Example Response

```json
{
  "allowed": false,
  "category": "SARA",
  "confidence": 0.98,
  "reason_code": "RELIGIOUS_HATE"
}
```

---

## Roadmap

- [x] FastAPI project setup
- [x] Ollama integration
- [x] Qwen integration
- [x] Structured JSON responses
- [ ] Prompt optimization
- [ ] Multiple AI providers (OpenAI, Gemini)
- [ ] Docker support
- [ ] Unit & integration tests
- [ ] CI/CD pipeline
- [ ] Rate limiting
- [ ] Authentication
- [ ] Logging & monitoring

## Vision

The goal of this project is to provide a reusable, provider-agnostic moderation API that can integrate with any application. While it currently uses Ollama for local inference, the architecture is designed to support cloud-based LLMs and future fine-tuned moderation models without changing the public API.

## License

MIT License
