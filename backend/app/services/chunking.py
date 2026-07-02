def chunk_text(
    text,
    chunk_size=1000
):

    paragraphs = text.split("\n\n")

    chunks = []

    current_chunk = ""

    for paragraph in paragraphs:

        # First paragraph
        if not current_chunk:

            current_chunk = paragraph
            continue

        # Will it fit?
        if len(current_chunk) + len(paragraph) <= chunk_size:

            current_chunk += "\n\n" + paragraph

        else:

            chunks.append(current_chunk)

            current_chunk = paragraph

    # Don't forget the last chunk
    if current_chunk:

        chunks.append(current_chunk)

    return chunks