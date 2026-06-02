"""
Member A — Step 2: Clean raw article text (strip HTML, boilerplate, etc.)
"""

import re
from bs4 import BeautifulSoup


def strip_html(text: str) -> str:
    """Remove HTML tags from text."""
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text(separator=" ")


def remove_boilerplate(text: str) -> str:
    """Remove common boilerplate phrases found in news articles."""
    boilerplate_patterns = [
        r"Subscribe to.*?newsletter",
        r"Sign up for.*?updates",
        r"Read more:.*",
        r"Advertisement\s*",
        r"Cookie policy.*",
        r"\[.*?\]",  # e.g. [Photo credit: ...]
    ]
    for pattern in boilerplate_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text


def normalize_whitespace(text: str) -> str:
    """Collapse multiple spaces and newlines."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def clean_article(article: dict) -> dict:
    """Full cleaning pipeline for a single article."""
    content = article.get("content", "")
    content = strip_html(content)
    content = remove_boilerplate(content)
    content = normalize_whitespace(content)
    article["content"] = content
    return article


def clean_articles(articles: list[dict]) -> list[dict]:
    """Clean a list of articles, filtering out empty ones."""
    cleaned = [clean_article(a) for a in articles]
    cleaned = [a for a in cleaned if len(a["content"]) > 100]
    print(f"[Cleaner] {len(cleaned)} articles after cleaning")
    return cleaned


if __name__ == "__main__":
    sample = [{"content": "<p>Hello <b>world</b>! Sign up for our newsletter.</p>"}]
    print(clean_articles(sample))
