from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from genilib.solutions import generate_code, generate_solution

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate_code")
async def generate_code_endpoint(request: PromptRequest):
    """
    Endpoint to generate code from a given prompt.
    """
    code = generate_code(request.prompt)
    return {"generated_code": code}

@app.post("/generate_solution")
async def generate_solution_endpoint(request: PromptRequest):
    """
    Endpoint to generate a solution for a given question.
    """
    solution = generate_solution(request.prompt)
    return {"generated_solution": solution}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")