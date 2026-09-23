# AI Recruitment & Candidate Screening Platform

An AI-powered full-stack recruitment platform designed to simplify candidate management, resume analysis, job management, and candidate screening.

## Features

### HR / Recruiter

- Create and manage job postings
- View and manage candidates
- Upload and analyze resumes
- AI-assisted resume parsing
- Candidate profile generation
- AI-powered candidate screening
- Candidate-job matching
- Centralized HR dashboard

### Candidate

- Create and manage candidate profiles
- Upload resumes
- Manage skills, education, and experience
- View available opportunities
- Track application information

### AI Features

- Resume text extraction
- Structured resume information extraction
- AI-assisted candidate analysis
- Candidate screening
- Job-candidate matching
- Structured JSON generation from resume data

## Tech Stack

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Zustand

### Backend

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

### AI / NLP

- OpenRouter API
- LLM-based resume analysis
- Structured JSON extraction
- Resume text processing

### Other Technologies

- Docker
- Docker Compose
- Git
- REST APIs

## Project Architecture


AI-Recruitment-Platform/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── ...
│   ├── package.json
│   └── ...
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── gemini.py
│   │   ├── pipeline.py
│   │   ├── screening.py
│   │   ├── documents.py
│   │   └── ...
│   ├── requirements.txt
│   └── ...
│
├── docker-compose.yml
├── .env.example
└── README.md

 Installation

### 1. Configure Environment Variables

Create a `.env` file in the project root:

    OPENROUTER_API_KEY=your_openrouter_api_key
    GEMINI_MODEL=openrouter/free
    DATABASE_URL=your_database_url

Do not commit your `.env` file or API keys to GitHub.

2. Start the Backend

Run:

    python -m uvicorn backend.app.main:app --reload

The backend will normally run at:

    http://localhost:8000

 3. Start the Frontend

Open another terminal:

    cd frontend
    npm install
    npm run dev

The frontend will normally run at:

    http://localhost:5173

## Resume Processing Workflow

    Resume Upload
          |
          v
    PDF / Document Text Extraction
          |
          v
    Extracted Resume Text
          |
          v
    LLM Processing
          |
          v
    Structured Candidate Information
          |
          v
    Candidate Profile
          |
          v
    Screening / Matching

The system can extract information such as:

- Personal information
- Education
- Work experience
- Skills
- Projects
- Certifications
- Achievements

Candidate Screening

The platform uses candidate information together with job requirements to assist with candidate screening.

The screening workflow can consider:

- Technical skills
- Experience
- Education
- Job requirements
- Candidate profile information

AI-generated results are intended to assist recruiters and should be reviewed by a human before making recruitment decisions.

 Database

The application uses PostgreSQL for storing application data including:

- Users
- Candidate profiles
- Jobs
- Applications
- Resume information
- Screening information

 Docker

Start the services:

    docker compose up

Stop the services:

    docker compose down

To remove containers and associated volumes:

    docker compose down -v

 Security

Sensitive configuration should be stored in environment variables.

Never commit the following:

    .env
    API keys
    Database passwords
    Access tokens
    Private credentials

Use `.env.example` to document the required environment variables without exposing private credentials.

My Contributions

- Configured the application for local development
- Configured the frontend and backend environment
- Integrated OpenRouter for AI processing
- Configured LLM-based resume processing
- Configured and tested the resume upload workflow
- Tested frontend and backend integration
- Updated environment configuration
- Improved handling of AI-generated responses
- Customized project branding and documentation

Future Improvements

- Improved resume parsing accuracy
- Support for additional LLM providers
- Advanced candidate matching
- Interview scheduling
- Email notifications
- Recruiter analytics
- Improved authentication and authorization
- Expanded automated testing
- Production deployment

Developer

**Chirag Kaliyar**

B.Tech Student | Software and AI/ML Enthusiast

Skills

- C
- C++
- Python
- Java
- JavaScript
- SQL
- Machine Learning
- Deep Learning
- Full-Stack Development

License

This project is intended for educational and portfolio purposes.