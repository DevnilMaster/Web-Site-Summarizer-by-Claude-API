# 🌐 Website Summarizer (Claude API)

A tiny, token-efficient Python tool that summarizes **any website** into a few
bullet points using Anthropic's Claude model. Give it a link, get a clean summary.

Built with the `claude-sonnet-5` model and kept intentionally lightweight so it
does the job **without burning extra tokens**.

## ✨ Features

- **One input:** just pass a website URL.
- **Token efficient:** website text is trimmed to ~6000 chars before sending, and
  the reply is capped at `max_tokens = 300` — a good summary, low cost.
- **Clean scraping:** strips out scripts, styles, nav, header, footer & images so
  only the real content reaches the model.
- **Simple & readable:** one small script, easy to understand and extend.

## 🛠️ How it works

1. Fetch the page with `requests`.
2. Extract the title + main text with `BeautifulSoup` (junk tags removed).
3. Trim the text to keep input tokens low.
4. Send it to Claude with a short "summarize concisely" instruction.
5. Print a 3–5 bullet summary.

## 📦 Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Add your API key
cp .env.example .env
# then edit .env and paste your Anthropic key:
# ANTHROPIC_API_KEY=sk-ant-...
```

Get a key from the [Anthropic Console](https://console.anthropic.com/).

## 🚀 Usage

```bash
python summarize.py https://en.wikipedia.org/wiki/Bangladesh
```

Example output:

```
Summarizing: https://en.wikipedia.org/wiki/Bangladesh
----------------------------------------
- Bangladesh is a South Asian country bordering India and Myanmar.
- One of the world's most densely populated nations, capital is Dhaka.
- Economy is driven largely by textiles and agriculture.
- ...
```


## ⚙️ Tuning 

Open `summarize.py` and tweak the constants at the top:

| Setting           | Default | What it does                              |
| ----------------- | ------- | ----------------------------------------- |
| `MODEL`           | `claude-sonnet-5` | Which Claude model to use        |
| `MAX_TOKENS`      | `300`   | Max length of the summary (lower = cheaper) |
| `MAX_INPUT_CHARS` | `6000`  | How much page text to send (lower = cheaper) |

## 📁 Project structure

```
website-summarizer/
├── summarize.py       
├── requirements.txt   
├── .env.example       
├── .gitignore         
└── README.md
```



Made as a simple demo of using the Claude API for real-world summarization.
