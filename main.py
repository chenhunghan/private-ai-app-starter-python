from fastapi import FastAPI
import openai
from pydantic import BaseModel

class Body(BaseModel):
    prompt: str
    
app = FastAPI()

@app.post("/prompt")
async def completions(
    body: Body
):
    prompt = body.prompt
    # Add more logics here, for example, you can add the context to the prompt
    # using context augmentation retrieval methods
    response = openai.Completion.create(
        prompt=prompt,
        model="mpt-30b.ggmlv0.q4_1.bin",
        temperature=0.5
    )
    completion = response.choices[0].text
    
    return completion
