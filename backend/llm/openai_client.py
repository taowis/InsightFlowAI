import os
from openai import OpenAI

def generate_narrative(prompt: str, metrics_json: str) -> str:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    system = "You are a senior marketing analyst. Use only given data."
    resp = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {"role":"system","content":system},
            {"role":"user","content":prompt + "\n\n" + metrics_json}
        ]
    )
    return resp.choices[0].message.content
