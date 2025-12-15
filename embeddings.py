import json
from openai import OpenAI
import numpy as np

client = OpenAI(api_key="API_OPENAI_API_KEY")


from clean_text import all_chunks

embeddings = []

for chunk in all_chunks:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
    embeddings.append({
        "chunk": chunk,
        "embedding": response.data[0].embedding
    })

# Save embeddings
with open("data/embeddings.json", "w", encoding="utf-8") as f:
    json.dump(embeddings, f, ensure_ascii=False, indent=4)

print("Embeddings generated!")
