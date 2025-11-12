import os
import httpx
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("GITHUB_TOKEN_ACCESS")

app = FastAPI()

@app.get("/api/v1/tech/{tech_name}")
async def get_tech(tech_name: str):
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {API_KEY}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    url = "https://api.github.com/search/repositories"
    try:
        res = await httpx.AsyncClient().get(url=f"{url}?q={tech_name}", headers=headers)
    except Exception as e:
        return {"error": e}
    
    return res.json()