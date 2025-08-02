from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from app.model.loader import generator
from app.utils.safety import is_safe_input
from app.utils.generator import generate_and_evaluate

app = FastAPI()

class DomainRequest(BaseModel):
    business_description: str

@app.post("/generate")
async def generate_domain(request: DomainRequest):
    desc = request.business_description

    if not is_safe_input(desc):
        return {"status": "blocked", "suggestions": [], "message": "Inappropriate content"}

    result = generate_and_evaluate(desc)
    return {
        "status": result["status"],
        "suggestions": [{"domain": result["domain"], "confidence": result["score"]}]
    }
