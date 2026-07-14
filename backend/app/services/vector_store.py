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

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
    dimension
    )

    index.add(
        embeddings
    )

    return index