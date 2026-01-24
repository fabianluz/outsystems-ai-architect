import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import json
from dotenv import load_dotenv

# 1. Load existing .env file if it exists
load_dotenv()

app = FastAPI(title="OutSystems AI Architect")

# Global client variable (initialized lazily)
client = None

# --- DATA STRUCTURES ---
class AppDescription(BaseModel):
    description: str

# --- SYSTEM PROMPT ---
SYSTEM_PROMPT = """
You are an expert OutSystems Data Architect and Database Administrator. 
Your goal is to convert a user's application description into a valid OutSystems Data Model Blueprint AND a T-SQL script.

Rules for Output Format:
1. Output MUST be a single JSON object with two keys: "Blueprint" and "SQL".

Rules for "Blueprint" Key:
1. This is a list of "Entities".
2. Each Entity has: "Name", "Description", "IsStatic" (boolean), and "Attributes".
3. Attributes have: "Name", "DataType" (Text, Integer, Boolean, DateTime, Currency, or [EntityName] Identifier).

Rules for "SQL" Key:
1. Generate valid T-SQL (SQL Server) 'CREATE TABLE' statements.
2. Include Primary Keys (Id) and Foreign Key constraints based on relationships.
3. Use appropriate data types (NVARCHAR for Text, BIT for Boolean, etc.).
4. Return this as a single string.
"""

# --- ENDPOINTS ---
@app.post("/generate-blueprint")
async def generate_blueprint(request: AppDescription):
    global client
    
    # Initialize OpenAI client if not already done
    if not client:
        # This will now safely pick up the key from os.environ
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="API Key not configured on server.")
        client = OpenAI()

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo", 
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Create an OutSystems data model for: {request.description}"}
            ],
            temperature=0.2,
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- KEY MANAGEMENT LOGIC ---
def configure_api_key():
    """
    Interactively handles the API Key setup.
    """
    env_file = ".env"
    current_key = os.getenv("OPENAI_API_KEY")
    
    # 1. Check if we already have a key
    if current_key:
        # Mask the key for display (Show first 8 chars...last 4 chars)
        masked_key = f"{current_key[:8]}...{current_key[-4:]}" if len(current_key) > 12 else "****"
        print(f"\n🔑 Found saved API Key: {masked_key}")
        
        use_existing = input("   Do you want to use this key? (Y/n): ").strip().lower()
        if use_existing in ["", "y", "yes"]:
            print("   ✅ Using existing key.\n")
            return

    # 2. If no key or user wants a new one
    print("\n⚙️  API Key Setup")
    new_key = input("   Please enter your OpenAI API Key: ").strip()
    
    if not new_key:
        print("   ❌ Error: Key cannot be empty. Exiting.")
        exit(1)

    # 3. Save to .env file and update current environment
    with open(env_file, "w") as f:
        f.write(f"OPENAI_API_KEY={new_key}")
    
    os.environ["OPENAI_API_KEY"] = new_key # Update memory immediately
    print(f"   ✅ Key saved to {env_file} and loaded.\n")

if __name__ == "__main__":
    # Run setup before starting the server
    configure_api_key()
    
    print("🚀 Starting Server...")
    print("👉 Open Swagger UI: http://localhost:8000/docs")