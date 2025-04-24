from fastapi import FastAPI, Request
from pydantic import BaseModel
from utils import mask_pii
from fastapi.responses import HTMLResponse
from models import classify_email

app = FastAPI()

class EmailRequest(BaseModel):
    email_body: str
@app.get("/", response_class=HTMLResponse)
def root():
    print("✅ Root path accessed")
    return """
    <h2>🚀 Email Classification API is Running!</h2>
    <p>Visit the <a href="/docs">Swagger UI</a> to test the API.</p>
    """
@app.post("/classify/")
async def classify(request: EmailRequest):
    masked_email, entities = mask_pii(request.email_body)
    category = classify_email(masked_email)

    return {
        "input_email_body": request.email_body,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }
