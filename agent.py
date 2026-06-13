import sqlite3
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_profile():
    conn = sqlite3.connect('formagent.db')
    c = conn.cursor()
    c.execute("SELECT field, value FROM profile")
    rows = c.fetchall()
    conn.close()
    return "\n".join([f"{field}: {value}" for field, value in rows])

def fill_with_agent(fields, context=None):
    profile = get_profile()
    labelled = [f for f in fields if f['label']]
    extra = f"\nExtra context for this application: {context}" if context else ""
    
    prompt = f"""You are filling out an application form on behalf of this person.

PROFILE:
{profile}
{extra}

FORM FIELDS:
{json.dumps(labelled, indent=2)}

For each field, provide the most appropriate answer based on the profile.
Return ONLY a JSON object where keys are the field 'name' values and values are your answers.
Be specific and tailored, not generic. For open ended questions write compelling, honest answers."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    text = response.choices[0].message.content.strip()
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    
    return json.loads(text.strip())


if __name__ == "__main__":
    test_fields = [
        {'type': 'textarea', 'name': 'd4a536b4a41ce2346477c393bcff3dd9', 'label': 'Est-ce que tu parles français?', 'placeholder': '', 'required': False},
        {'type': 'textarea', 'name': 'acb0ff8e6ac868df327e55c3fd6aec96', 'label': 'Email', 'placeholder': '', 'required': False},
        {'type': 'textarea', 'name': 'd0880baab49dff5448ccc29e8f222463', 'label': 'Where can we learn more about you?', 'placeholder': '', 'required': False},
        {'type': 'textarea', 'name': 'fe52b77c6dfbb0a9b6b8ec54dbea4cbd', 'label': 'What are you building? (1 sentence)', 'placeholder': '', 'required': False},
        {'type': 'textarea', 'name': '6843a21e71b39ecee60e92386ca2db79', 'label': 'Add link to your project', 'placeholder': '', 'required': False},
    ]
    
    context = input("Any specific context for this application? (press enter to skip): ")
    answers = fill_with_agent(test_fields, context if context else None)
    
    print("\nGenerated answers:")
    for name, answer in answers.items():
        print(f"\n{name}:\n{answer}")
