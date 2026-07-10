import faiss
import numpy as np

def create_index(knowledge):

    embeddings = []

    for record in knowledge:

        embeddings.append(
            record["embedding"]
        )

    embeddings = np.array(
        embeddings,
        dtype="float32"
    )

    return embeddings