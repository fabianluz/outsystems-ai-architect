# OutSystems AI Architect 🚀

An AI-powered microservice that accelerates OutSystems backend prototyping by instantly generating Entity Blueprints and SQL scripts from natural language descriptions.

![Project Status](https://img.shields.io/badge/Status-Prototype-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT4-green)

## 💡 The Problem
In rapid application development (RAD), defining the initial data model often involves repetitive manual work: creating entities, defining attributes, and setting up relationships. This slows down the "Idea-to-Prototype" phase.

## 🛠 The Solution
This tool acts as an **AI Assistant for OutSystems Architects**. It translates business requirements (e.g., *"A CRM where managers track leads and assign tasks"*) into:
1.  **JSON Blueprints:** Structured data ready for OutSystems ingestion.
2.  **Visual Models:** An interactive entity diagram.
3.  **T-SQL Scripts:** Ready-to-run database creation scripts.

## 🏗 Architecture
* **Frontend:** Streamlit (Python) - For the interactive UI.
* **Backend:** FastAPI (Python) - REST API handling request sanitization.
* **Engine:** OpenAI GPT-4 - Logic generation.

## 📸 Screenshots
<img width="3234" height="1488" alt="image" src="https://github.com/user-attachments/assets/36c05154-d1d1-445b-8115-63f366e6a123" />
<img width="3276" height="1566" alt="image" src="https://github.com/user-attachments/assets/2fedec65-9715-4f07-80d8-1c2899bb4c8b" />


## 🚀 How to Run Locally

### 1. Clone the Repo
```bash
git clone [https://github.com/YOUR_USERNAME/outsystems-ai-architect.git](https://github.com/YOUR_USERNAME/outsystems-ai-architect.git)
cd outsystems-ai-architect

```

### 2. Install Dependencies

It is recommended to use a virtual environment.

```bash
python -m venv venv
# Activate the environment:
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install libraries
pip install -r requirements.txt

```

### 3. Setup Environment Variables

Create a `.env` file in the root directory and add your OpenAI Key:

```ini
OPENAI_API_KEY=sk-proj-your-actual-key-here

```

### 4. Run the Application

You need to run both the backend and frontend terminals simultaneously.

**Terminal 1 (Backend API):**

```bash
uvicorn main:app --reload

```

**Terminal 2 (Frontend UI):**

```bash
streamlit run gui.py

```

## 🔮 Future Roadmap

* [ ] Direct `.oml` (OutSystems Module) file generation using XML parsing.
* [ ] Integration with OutSystems ODC (OutSystems Developer Cloud) API.
* [ ] User authentication and project history.

## 📄 License

MIT

