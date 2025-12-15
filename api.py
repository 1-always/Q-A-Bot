from fastapi import FastAPI
from pydantic import BaseModel
from retriever import generate_answer

app = FastAPI()

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_bot(q: Question):
    answer = generate_answer(q.question)
    return {"answer": answer}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
