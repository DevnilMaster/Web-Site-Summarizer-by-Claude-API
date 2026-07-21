
import os
import sys
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()  

MODEL = "claude-sonnet-5"
MAX_TOKENS = 300          
MAX_INPUT_CHARS = 6000    


def fetch_text(url: str) -> tuple[str, str]:
    headers = {"User-Agent": "Mozilla/5.0 (WebsiteSummarizer)"}
    resp = requests.get(url, headers=headers, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    title = soup.title.string.strip() if soup.title and soup.title.string else "No title"

   
    for tag in soup(["script", "style", "img", "nav", "footer", "header"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)
    return title, text[:MAX_INPUT_CHARS]  


def summarize(url: str) -> str:
    title, text = fetch_text(url)

    client = Anthropic()  

    message = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=(
            "You are a concise summarizer. Given a website's title and text, "
            "reply with a short 3-5 bullet point summary. No preamble."
        ),
        messages=[
            {
                "role": "user",
                "content": f"Title: {title}\n\nContent:\n{text}",
            }
        ],
    )
    
    for block in message.content:
        if getattr(block, "type", None) == "text":
            return block.text
    return "(no text returned)"


def main():
    if len(sys.argv) < 2:
        print("Usage: python summarize.py <website-url>")
        sys.exit(1)

    url = sys.argv[1]
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    print(f"\nSummarizing: {url}\n" + "-" * 40)
    try:
        print(summarize(url))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
