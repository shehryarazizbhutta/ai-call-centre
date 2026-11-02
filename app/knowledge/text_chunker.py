
def chunk_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be non-negative and smaller than chunk_size"
        )

    text = text.strip()

    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))

        if end < len(text):
            split_at = text.rfind(" ", start, end)

            if split_at > start:
                end = split_at

        chunks.append(text[start:end].strip())

        if end == len(text):
            break

        start = end - chunk_overlap

        while start > 0 and text[start] != " ":
            start -= 1

    return [chunk for chunk in chunks if chunk]
