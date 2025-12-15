import json
import faiss
import numpy as np

# Load embeddings
with open("data/embeddings.json", "r", encoding="utf-8") as f:
    embeddings_data = json.load(f)

dimension = len(embeddings_data[0]["embedding"])
index = faiss.IndexFlatL2(dimension)

vectors = np.array([e["embedding"] for e in embeddings_data], dtype='float32')
index.add(vectors)

# Save index
faiss.write_index(index, "data/embeddings.index")

# Save mapping of index -> chunk
with open("data/index_to_chunk.json", "w", encoding="utf-8") as f:
    json.dump([e["chunk"] for e in embeddings_data], f, ensure_ascii=False, indent=4)

print("Vector store ready!")
