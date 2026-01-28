# Eklavya.me_Assignment
AI Agent-Based Educational Content Generator
📌 Overview

This project implements a simple agent-based AI system with a UI-driven workflow.
It demonstrates how multiple AI agents can collaborate in a pipeline to generate, evaluate, and refine educational content.

The system is built using Python (Flask) for the backend and HTML/CSS for the frontend.

🎯 Objective
To design and implement:
Two AI agents with clear responsibilities,
A structured input → output pipeline,
A UI that makes the agent flow visible and easy to understand.

This project follows the requirements provided in the assessment PDF.

🧩 Agent Architecture

1️⃣ Generator Agent
Responsibility:
Generates educational content for a given grade and topic.
Key Constraints:
Language matches the grade level,
Concepts are age-appropriate and correct,
Output structure is deterministic .

2️⃣ Reviewer Agent
Responsibility:
Evaluates the Generator Agent’s output.
Input:
JSON output from the Generator Agent.
Evaluation Criteria:
Age appropriateness,
Conceptual correctness,
Clarity of explanation and questions.

🔁 Refinement Logic
If the Reviewer returns fail:
The Generator is re-run once,
Reviewer feedback is embedded into the new generation,
Only one refinement pass is allowed (as per assessment requirements).

🖥️ UI Integration
The frontend:
Triggers the agent pipeline.
Displays:
Generator output,
Reviewer feedback,
Refined output .
Clearly visualizes the agent flow:
Generator → Reviewer → Refined Output

📂 Project Structure
agent-ai-assessment/
│
├── backend.py          # Backend (Generator + Reviewer agents)
│
├── templates/
│   └── index.html      # Frontend UI
│
├── static/
│   └── style.css       # UI styling
│
└── README.md           # Project documentation

🚀 How to Run the Project
1️⃣ Navigate to the project folder
cd agent-ai-assessment

2️⃣ Run the backend
python backend.py

3️⃣ Open in browser
http://127.0.0.1:5000

🛠️ Tech Stack
Backend: Python, Flask
Frontend: HTML5, CSS3
Architecture: Agent-based design (Generator + Reviewer)
UI: Web-based 
