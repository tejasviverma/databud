from app.services.embeddings import generate_embedding
import numpy as np


def retrieve(
    question,
    index,
    knowledge,
    k=3
):

    query_embedding = generate_embedding(
        question
    )

    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    query_embedding = query_embedding.reshape(
        1,
        -1
    )

    _, indices = index.search(
        query_embedding,
        k
    )

    retrieved_chunks = []

    for i in indices[0]:

        retrieved_chunks.append(
            knowledge[i]["text"]
        )

    context = "\n\n".join(
        retrieved_chunks
    )

    return context