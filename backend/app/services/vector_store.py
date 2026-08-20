import json
from pathlib import Path


VECTOR_DB_PATH = Path("data/vector_db/chunks.json")


def save_chunks(chunks: list[dict]) -> None:
    VECTOR_DB_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with open(
        VECTOR_DB_PATH,
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            chunks,
            file,
            ensure_ascii=False,
            indent=2,
        )


def load_chunks() -> list[dict]:
    if not VECTOR_DB_PATH.exists():
        return []

    with open(
        VECTOR_DB_PATH,
        "r",
        encoding="utf-8",
    ) as file:
        return json.load(file)