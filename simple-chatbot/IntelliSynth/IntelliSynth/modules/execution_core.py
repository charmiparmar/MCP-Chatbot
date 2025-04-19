from modules.utils import OPENAI_KEY, CLAUDE_KEY

def query_openai(prompt: str) -> str:
    import openai
    openai.api_key = OPENAI_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

def query_claude(prompt: str) -> str:
    from anthropic import Anthropic
    client = Anthropic(api_key=CLAUDE_KEY)
    response = client.messages.create(
        model="claude-3-opus-20240229",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    return response.content[0].text
