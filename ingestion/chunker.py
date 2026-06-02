"""
Member A — Step 3: Chunk articles into 300-500 token segments with 50-token overlap
"""

import uuid
from langchain.text_splitter import RecursiveCharacterTextSplitter


CHUNK_SIZE = 400    # tokens (approx chars / 4)
CHUNK_OVERLAP = 50


def chunk_article(article: dict) -> list[dict]:
    """Split a single article into overlapping chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE * 4,      # chars approx
        chunk_overlap=CHUNK_OVERLAP * 4,
        separators=["\n\n", "\n", ". ", " "],
    )

    texts = splitter.split_text(article["content"])
    chunks = []
    for i, text in enumerate(texts):
        chunks.append({
            "chunk_id": str(uuid.uuid4()),
            "article_id": article.get("article_id", str(uuid.uuid4())),
            "chunk_index": i,
            "text": text,
            "title": article.get("title", ""),
            "source": article.get("source", ""),
            "date": article.get("date", ""),
            "url": article.get("url", ""),
        })
    return chunks


def chunk_all_articles(articles: list[dict]) -> list[dict]:
    """Chunk all articles and return flat list of chunks."""
    # Assign article IDs if missing
    for article in articles:
        if "article_id" not in article:
            article["article_id"] = str(uuid.uuid4())

    all_chunks = []
    for article in articles:
        all_chunks.extend(chunk_article(article))

    print(f"[Chunker] {len(articles)} articles → {len(all_chunks)} chunks")
    return all_chunks


if __name__ == "__main__":
    sample = [{
        "title": "AI News",
        "source": "TechCrunch",
        "date": "2026-06-01",
        "url": "https://example.com",
        "content": "This is a test article. " * 100,
    }]
    chunks = chunk_all_articles(sample)
    print(f"Chunks: {len(chunks)}, first: {chunks[0]['text'][:80]}")
