from sentence_transformers import SentenceTransformer

# Load the model only once
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def generate_embedding(text):

    embedding = model.encode(
        text,
        convert_to_numpy=True
    )

    print(len(embedding))

    return embedding.tolist()