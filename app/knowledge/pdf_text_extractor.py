
from pathlib import Path

import pymupdf


def extract_text_from_pdf(pdf_path: str | Path) -> str:
    with pymupdf.open(pdf_path) as document:
        pages = [
            page.get_text()
            for page in document
        ]

    return "\n\n".join(pages).strip()
