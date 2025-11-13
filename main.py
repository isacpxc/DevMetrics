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
        async with httpx.AsyncClient() as client:
            params = {
                "q": f"topic:{tech_name}",
                "sort": "stars"
            }
            
            res = await client.get(url=url, params=params, headers=headers)
            
            res.raise_for_status() 
            return res.json()
    except httpx.HTTPStatusError as e:  
        return {"error": "API fail connection", "status": e.response.status_code}
    except httpx.RequestError as e:
        return {"error": "network error", "message": e}
    
    