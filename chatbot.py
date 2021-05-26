import os
import openai

# OPENAI_API_KEY=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
openai.api_key = os.getenv("OPENAI_API_KEY")
human_input = str(input("Human: "))
prompt = f"\nHuman: {human_input}\nAI:"

while True:
  response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["\n", " Human:", " AI:"]
  )

  print(f"AI:{response['choices'][0]['text']}")
  prompt += f'{response["choices"][0]["text"]}\nHuman: '
  human_input = str(input("\nHuman: "))
  prompt += f'{human_input}\nAI:'