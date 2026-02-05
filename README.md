
# 🚀 OutSystems AI Architecht Helper

**OutSystems AI Architect** is a generative AI tool designed to accelerate the "Day 0" architecture phase of OutSystems applications. It converts natural language descriptions of app ideas into technical deliverables: a **Data Model Blueprint** and valid **SQL Server (T-SQL) scripts**.

This tool leverages **OpenAI's GPT-4 Turbo** to act as an expert OutSystems Data Architect, ensuring the output aligns with platform best practices.

## ✨ Features

* **Natural Language to Architecture:** Simply describe your app (e.g., *"A library system where users borrow books..."*), and the AI generates the necessary data structure.
* **Visual Blueprint:** Automatically renders a masonry-style visualization of your Entities and Attributes using Streamlit.
* **SQL Generation:** Produces ready-to-execute T-SQL `CREATE TABLE` scripts, including Primary Keys, Foreign Keys, and appropriate data types.
* **Dual-Interface Architecture:** Built with a clean separation between the logic (FastAPI backend) and the presentation (Streamlit frontend).

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) – For the interactive web interface.
* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) – For the REST API handling AI logic.
* **AI Engine:** [OpenAI API](https://openai.com/) (GPT-4 Turbo) – For schema generation.
* **Language:** Python 3.10+

## 📋 Prerequisites

Before running the project, ensure you have:

1. **Python 3.x** installed.
2. An **OpenAI API Key**. You can obtain one [here](https://platform.openai.com/).

## ⚙️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/fabianluz/outsystems-ai-architect.git
cd outsystems-ai-architect

```


2. **Install dependencies:**
It is recommended to use a virtual environment.
```bash
pip install -r requirements.txt

```



## 🚀 Usage

The application requires two separate processes to run: the Backend API and the Frontend UI.

### Step 1: Start the Backend (FastAPI)

The backend handles the connection to OpenAI and processes the prompt engineering.

1. Open a terminal and run:
```bash
python main.py

```


2. **First Run Configuration:** If you haven't configured your API key, the script will interactively ask for it and save it to a `.env` file automatically.
3. The server will start at `http://localhost:8000`.

### Step 2: Start the Frontend (Streamlit)

The frontend provides the visual interface to interact with the architect.

1. Open a **new** terminal window (keep the backend running).
2. Run the Streamlit app:
```bash
streamlit run gui.py

```


3. The interface will open in your default browser (usually at `http://localhost:8501`).

## 💡 How to Use

1. **Enter Description:** In the web interface, type a description of the application you want to build.
* *Example:* "A Fleet Management system where Drivers are assigned to Vehicles. Vehicles need to track Mileage, License Plate, and Last Maintenance Date."


2. **Generate:** Click the **"Generate Blueprint"** button.
3. **View Results:**
* **🏗️ Blueprint Visualizer:** Explore the entities and their attributes in a card layout.
* **💾 SQL Script:** Copy the generated T-SQL code to use in SQL Server or OutSystems.
* **📄 Raw JSON:** View the structured data response from the API.



## 📂 Project Structure

* **`main.py`**: The entry point for the backend. Contains the FastAPI app, OpenAI system prompts (`SYSTEM_PROMPT`), and API key management logic.
* **`gui.py`**: The Streamlit application. Handles user input, API requests to the backend, and rendering the results.
* **`requirements.txt`**: List of Python libraries required to run the project.
* **`.env`**: (Auto-generated) Stores your OpenAI API key locally.

## ⚠️ Notes

* **Model Cost:** This tool uses `gpt-4-turbo`. Ensure you have sufficient credits in your OpenAI account.
* **Privacy:** Your API key is stored locally in the `.env` file and is not shared.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements.

---

*Created by Fabian Luz*
