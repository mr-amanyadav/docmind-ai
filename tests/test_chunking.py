from backend.app.services.chunking_service import split_text


def test_split_text():
    text = "A" * 2500

    chunks = split_text(
        text,
        chunk_size=1000,
        chunk_overlap=150,
    )

    assert len(chunks) > 1

    for chunk in chunks:
        assert len(chunk) <= 1000