from pathlib import Path

import fitz


def get_pdf_metadata(pdf_path: Path) -> dict:
    document = fitz.open(pdf_path)

    metadata = {
        "page_count": len(document),
        "metadata": document.metadata,
    }

    document.close()

    return metadata


def extract_text_from_pdf(pdf_path: Path) -> list[dict]:
    document = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text")

        pages.append(
            {
                "page_number": page_number,
                "text": text,
                "character_count": len(text),
            }
        )

    document.close()

    return pages