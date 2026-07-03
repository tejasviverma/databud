def chunk_text(
    text,
    chunk_size=1000
):

    separators = [
        "\n\n",
        "\n",
        ". ",
        " ",
        ""
    ]

    return recursive_chunking(
        text,
        chunk_size,
        separators
    )

def merge_chunks(
    pieces,
    chunk_size
):
    
    merged_chunks = []

    current_chunk = ""

    for piece in pieces:

        # First piece
        if not current_chunk:

            current_chunk = piece
            continue

        # Will it fit?
        if len(current_chunk) + len(piece) + 2  <= chunk_size:

            current_chunk += "\n\n" + piece

        else:

            merged_chunks.append(current_chunk)

            current_chunk = piece

    # Don't forget the last chunk
    if current_chunk:

        merged_chunks.append(current_chunk)

    return merged_chunks

def recursive_chunking(
    text,
    chunk_size,
    separators
):

    # Base Case 1
    if len(text) <= chunk_size:
        return [text]

    # Base Case 2
    if not separators:

        return [
            text[i:i + chunk_size]
            for i in range(
                0,
                len(text),
                chunk_size
            )
        ]

    separator = separators[0]
    remaining = separators[1:]

    # Python cannot split on ""
    if separator == "":
        pieces = list(text)
    else:
        pieces = text.split(separator)

    split_pieces = []

    for piece in pieces:

        # Skip empty strings
        if not piece.strip():
            continue

        if len(piece) <= chunk_size:

            split_pieces.append(piece)

        else:

            split_pieces.extend(

                recursive_chunking(
                    piece,
                    chunk_size,
                    remaining
                )

            )

    return merge_chunks(
        split_pieces,
        chunk_size
    )