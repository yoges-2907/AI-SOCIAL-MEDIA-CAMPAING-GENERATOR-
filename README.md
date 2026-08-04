# AI Social Media Campaign Generator

## Abstract

The **AI Social Media Campaign Generator** is a full-stack, AI-powered application designed to automate the creation of platform-specific social media marketing campaigns from a single user prompt. The system combines a lightweight HTML/CSS/JavaScript frontend with a modular FastAPI REST backend. Google Gemini is used for intelligent caption generation, while Stable Diffusion XL (via the Hugging Face Inference API) is used for prompt-based AI image generation. Generated campaigns are persisted in SQLite and exposed through REST endpoints, enabling real-time interaction, campaign history retrieval, and downloadable social media assets.

The application is architected using a **service-oriented backend design**, separating API routing, AI generation, image generation, and database operations into independent modules. This approach improves maintainability, extensibility, and deployment reliability while demonstrating practical AI automation workflows suitable for modern marketing systems.

---

## 1. Introduction & Why This Project?

### The Problem

Digital marketing requires the rapid production of high-quality content across multiple platforms such as Instagram, LinkedIn, Facebook, and X. However, content creators and student teams often encounter several challenges:

1. **Manual Caption Writing** – Writing engaging, platform-specific captions is time-consuming.
2. **Visual Content Creation** – Designing matching posters or promotional images requires separate tools and design skills.
3. **Workflow Fragmentation** – Text generation, image creation, and content management are usually handled in different applications.
4. **Lack of Automation** – Repetitive campaign creation reduces productivity and consistency.

### The Solution

This project was developed to provide an **end-to-end AI automation pipeline**. A user enters a single prompt, selects the target platform and audience tone, and the system automatically:

* Generates a marketing caption using Gemini.
* Creates a corresponding AI-generated poster using Stable Diffusion XL.
* Stores the campaign in SQLite.
* Displays the result instantly in the web interface.
* Allows the generated image to be downloaded.

The goal is not only to generate text, but to automate the complete **social media campaign creation workflow**.

---

## 2. System Architecture

The application follows a **Frontend → REST API → AI Services → Database** architecture.

```text
Frontend (HTML / CSS / JavaScript)
                │
                ▼
         FastAPI REST API
                │
      ┌─────────┴─────────┐
      ▼                   ▼
 Gemini Caption      Stable Diffusion XL
    Service             Image Service
                │
                ▼
             SQLite
```

### Workflow

1. The user enters a prompt and selects a platform and tone.
2. The frontend sends a `POST /generate` request.
3. The FastAPI backend orchestrates the generation process.
4. Gemini generates the caption and hashtags.
5. Stable Diffusion XL generates a matching poster image.
6. The campaign is stored in SQLite.
7. The frontend receives the caption and image URL and updates the UI.
8. Previous campaigns are retrieved through `GET /history`.

---

## 3. Project Structure

The repository is organized as a **modular monolith** with clear separation of concerns.

```text
AI-SOCIAL-MEDIA-CAMPAIGN-GENERATOR/
│
├── backend/
│   ├── api/
│   │   ├── generate.py
│   │   └── history.py
│   │
│   ├── services/
│   │   ├── text_generator.py
│   │   └── image_generator.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   └── app.db
│   │
│   ├── storage/
│   │   └── generated/
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── .gitignore
└── README.md
```

---

## 4. Tech Stack

### Frontend

* HTML5
* CSS3
* Vanilla JavaScript

### Backend

* FastAPI
* Uvicorn
* SQLite

### AI & Image Generation

* Google Gemini API
* Stable Diffusion XL (Hugging Face Inference API)

### Supporting Libraries

* requests
* python-dotenv
* Pillow

---

## 5. Core Components

### `generate.py`

Handles the main `POST /generate` endpoint and coordinates the caption and image generation workflow.

### `text_generator.py`

Uses Google Gemini to create platform-specific marketing captions, hashtags, and calls to action.

### `image_generator.py`

Uses Stable Diffusion XL through the Hugging Face Inference API to generate prompt-dependent social media posters.

### `db.py`

Initializes SQLite, stores generated campaigns, and retrieves campaign history.

### `app.js`

Connects the frontend to the REST API using asynchronous `fetch()` calls.

---

## 6. REST API Endpoints

### Generate a Campaign

**POST** `/generate`

#### Request

```json
{
  "prompt": "Create an Instagram post for a robotics workshop",
  "platform": "instagram",
  "tone": "student"
}
```

#### Response

```json
{
  "caption": "Generated marketing caption...",
  "image_url": "/storage/generated/example.png"
}
```

---

### Retrieve History

**GET** `/history`

Returns all previously generated campaigns ordered by creation time.

---

## 7. Setup & Local Installation

### Prerequisites

* Python 3.10 or higher
* Google Gemini API Key
* Hugging Face Access Token

### Clone the Repository

```bash
git clone https://github.com/yoges-2907/AI-SOCIAL-MEDIA-CAMPAING-GENERATOR-.git
cd AI-SOCIAL-MEDIA-CAMPAING-GENERATOR-
```

### Create a Virtual Environment

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create `backend/.env`

```env
GEMINI_API_KEY=your_google_api_key
HF_TOKEN=your_huggingface_token
```

### Run the Backend

```bash
uvicorn main:app --reload
```

### Open the Frontend

Open `frontend/index.html` in your browser.

---

## 8. Example Generation

### Input

* **Prompt:** Create a poster for the Robotics Club of ABC College
* **Platform:** Instagram
* **Tone:** Student

### Output

* AI-generated caption
* AI-generated robotics-themed poster
* Stored campaign history entry

Different prompts produce different generated images because the image service uses **prompt-conditioned Stable Diffusion XL generation**.

---

## 9. Reliability & Fallback Design

The image generation module is designed with a fallback strategy. If the external image API is unavailable, the system can switch to a local Pillow-based renderer, ensuring that the campaign generation workflow remains functional during demonstrations or network failures.

This design reflects a practical production-oriented approach where **availability is prioritized over complete feature failure**.

---

## 10. Why This Architecture?

This project intentionally avoids unnecessary complexity while still demonstrating:

* REST API design
* Frontend-backend integration
* LLM integration
* AI image generation
* Persistent storage
* Modular service architecture
* Automation workflow orchestration
* Error handling and fallback strategies

The architecture is suitable for **startup AI automation roles** where shipping reliable end-to-end features is often more important than building complex agent frameworks.

---

## 11. Future Enhancements

* Google OAuth authentication
* PostgreSQL migration
* Direct publishing to LinkedIn and X
* Campaign templates
* Brand guideline enforcement
* Multi-image carousel generation
* Scheduled post publishing
* Analytics dashboard
* LangGraph-based multi-step campaign orchestration

---

## 12. Learning Outcomes

Through this project I learned:

* Building RESTful APIs with FastAPI
* Integrating Google Gemini into Python applications
* Using Stable Diffusion through the Hugging Face Inference API
* Managing SQLite persistence
* Designing modular backend services
* Connecting a JavaScript frontend to a Python backend
* Implementing asynchronous API communication
* Designing fallback and reliability mechanisms

---

## 13. Author

**Yoges**

GitHub: https://github.com/yoges-2907

---

## 14. License

This project is licensed under the **MIT License**.
