# Apps_filling_agent
Got tired of filling forms during the application season. Got an agent to start doing it for me.

# FormAgent

An agentic form-filling assistant that reads any web form, extracts fields, generates tailored answers from your profile using an LLM, and fills them in automatically.

Built in one day. Handles Airtable's non-standard contenteditable DOM structure and Google Forms.

## What it does

- Reads form fields from any URL using Playwright browser automation
- Extracts labels including non-standard implementations (Airtable contenteditable, aria-labelledby patterns)
- Generates context-aware, profile-tailored answers using Groq LLaMA3
- Stores your profile and application history in SQLite
- Accepts per-application context to customise answers

## Stack

Python · Playwright · Groq API · SQLite · python-dotenv

## Setup

```bash
python3 -m venv formagent
source formagent/bin/activate
pip install google-genai playwright python-dotenv groq
playwright install
```

Add your Groq API key to `.env`:

Set up your profile:
```bash
python3 setup_profile.py
```

## Usage

```bash
python3 main.py
```

Paste any form URL when prompted. Add optional context for the specific application.

## Notes

Airtable renders form labels as React components using aria-labelledby rather than standard HTML label elements — required DOM inspection to reverse-engineer. Google Forms support in progress.
