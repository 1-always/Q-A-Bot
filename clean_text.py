import json
import re

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

# Load raw text
with open("data/raw_text.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

all_chunks = []

for url, text in raw_data.items():
    cleaned = clean_text(text)
    chunks = chunk_text(cleaned)
    all_chunks.extend(chunks)

print(f"Total chunks: {len(all_chunks)}")
