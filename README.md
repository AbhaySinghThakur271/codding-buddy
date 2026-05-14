# Coding Buddy AI 🚀

An AI-powered frontend application generator inspired by platforms like Lovable, Bolt, and v0.

Coding Buddy AI allows users to generate beautiful frontend websites using natural language prompts. The system uses LangGraph multi-agent workflows, FastAPI, and Groq LLMs to automatically plan, architect, generate, preview, and download complete frontend applications.

---

# ✨ Features

* AI-powered website generation
* Multi-agent architecture using LangGraph
* Generates:

  * HTML
  * CSS
  * JavaScript
* Live website preview
* Download generated projects as ZIP
* Beautiful modern UI generation
* FastAPI backend
* Vercel + Render deployment ready
* Prompt-based app creation

---

# 🛠 Tech Stack

## Backend

* Python
* FastAPI
* LangGraph
* LangChain
* Groq API
* Pydantic

## Frontend

* HTML
* CSS
* JavaScript

## Deployment

* Render (Backend)
* Vercel (Frontend)
* GitHub

---

# 📁 Project Structure

```bash
coding-buddy/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── generated_project/
│   └── agent/
│       ├── graph.py
│       ├── prompts.py
│       ├── states.py
│       └── tools.py
│
└── frontend/
    ├── index.html
    ├── style.css
    └── app.js
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/coding-buddy.git
cd coding-buddy
```

---

# 🔥 Backend Setup

## 1. Navigate to backend

```bash
cd backend
```

## 2. Create virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Add environment variables

Create a `.env` file inside backend:

```env
GROQ_API_KEY=your_groq_api_key
```

## 5. Run backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```bash
http://localhost:8000
```

---

# 🎨 Frontend Setup

## 1. Open another terminal

```bash
cd frontend
```

## 2. Run frontend server

```bash
python -m http.server 5500
```

Frontend runs on:

```bash
http://localhost:5500
```

---

# 🧠 How It Works

The application uses a multi-agent workflow powered by LangGraph.

## Workflow

```text
User Prompt
   ↓
Planner Agent
   ↓
Architect Agent
   ↓
Coder Agent
   ↓
Generated Files
   ↓
Live Preview
   ↓
ZIP Download
```

---

# 🤖 Agents

## Planner Agent

Responsible for:

* Understanding user request
* Defining application structure
* Planning required files

## Architect Agent

Responsible for:

* Breaking project into implementation tasks
* Defining file responsibilities
* Managing implementation order

## Coder Agent

Responsible for:

* Generating HTML/CSS/JS
* Creating modern UI
* Writing production-ready code

---

# 🌐 Deployment

## Backend Deployment (Render)

1. Push project to GitHub
2. Create Web Service on Render
3. Root Directory = `backend`
4. Build Command:

```bash
pip install -r requirements.txt
```

5. Start Command:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

6. Add Environment Variable:

```env
GROQ_API_KEY=your_key
```

---

## Frontend Deployment (Vercel)

1. Import GitHub repository
2. Root Directory = `frontend`
3. Framework = Other
4. Deploy

---

# 🌐 Live Demo

Live Application:

[https://codding-buddy.vercel.app/](https://codding-buddy.vercel.app/)

> Note: The backend is hosted on Render free tier. The first request may take some time to load because the backend server goes into sleep mode after inactivity.

---

# 📸 Screenshots

## Homepage

[[https://images.unsplash.com/photo-1516321318423-f06f85e504b3](https://github.com/AbhaySinghThakur271/codding-buddy/blob/main/screenshort/%7B0AF49A1F-5757-4057-B848-43D8B7D8B244%7D.png)]([https://images.unsplash.com/photo-1516321318423-f06f85e504b3](https://github.com/AbhaySinghThakur271/codding-buddy/blob/main/screenshort/%7B0AF49A1F-5757-4057-B848-43D8B7D8B244%7D.png))

## AI Generation Interface

[[https://images.unsplash.com/photo-1555066931-4365d14bab8c](https://github.com/AbhaySinghThakur271/codding-buddy/blob/main/screenshort/%7B76486472-E3D3-4BDC-94CB-98C142877B96%7D.png)]([https://images.unsplash.com/photo-1555066931-4365d14bab8c](https://github.com/AbhaySinghThakur271/codding-buddy/blob/main/screenshort/%7B76486472-E3D3-4BDC-94CB-98C142877B96%7D.png))


---

# 🚀 Example Prompts

```text
Create a futuristic SaaS landing page with glassmorphism UI
```

```text
Create a modern colorful todo app with smooth animations
```

```text
Create a premium portfolio website inspired by Apple
```

---

# 🔒 Current Limitations

* Free Render tier has cold starts
* Generation speed depends on LLM response time
* Complex apps may require multiple retries
* Frontend-only generation currently supported

---

# 🧩 Future Improvements

* Monaco code editor
* Real-time streaming generation
* Auto-fix loop
* Docker sandbox execution
* Multi-framework support
* React/Tailwind support
* AI debugging assistant
* Authentication system
* Rate limiting

---

# 📚 Learning Outcomes

This project demonstrates:

* AI Engineering
* LangGraph workflows
* Multi-agent orchestration
* Prompt engineering
* FastAPI backend development
* Frontend/backend integration
* Deployment pipelines
* Dynamic file generation
* LLM application architecture

---

# 👨‍💻 Author

Developed by Abhay Singh Thakur.

---

# ⭐ Contributing

Contributions, ideas, and improvements are welcome.

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Create pull request

---

# 📄 License

This project is open-source and available under the MIT License.
