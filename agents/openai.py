import modal
from modal import App, Image

# Setup

app = modal.App("openai")
image = Image.debian_slim().pip_install("requests")
secrets = [modal.Secret.from_name("openai-api-key")]
GPU = "T4"
MODEL_NAME = "gpt-4o-mini"

# OpenAI!

@app.function(image=image, secrets=secrets, gpu=GPU, timeout=1800)
def gpt_mini(prompt: str) -> str:
    import openai
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content




