import faiss
import json
import numpy as np
from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# Load index and mapping
index = faiss.read_index("data/embeddings.index")
with open("data/index_to_chunk.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

def get_relevant_chunks(query, top_k=3):
    # Generate embedding for query
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )
    query_vector = np.array([response.data[0].embedding], dtype='float32')
    
    # Search in FAISS
    D, I = index.search(query_vector, top_k)
    relevant_chunks = [chunks[i] for i in I[0]]
    return relevant_chunks

def generate_answer(question):
    context = "\n".join(get_relevant_chunks(question))
    prompt = f"Answer the question based ONLY on the context below:\n\n{context}\n\nQuestion: {question}\nAnswer:"
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
