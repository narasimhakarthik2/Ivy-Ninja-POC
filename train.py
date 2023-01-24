import openai

# Authenticate with OpenAI's API
openai.api_key ="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"

# Create the prompt with the guidelines
prompt = """
Write a highly professional statemnt of purpose with the following information.
   Degree: master's
   Course: Mechanical Engineering

SOP:

"""

# Fine-tune GPT-3 with the prompt
response = openai.Completion.create(
    prompt=prompt,
    temperature=0.5,
    model="davinci:ft-personal:ivyninja-2023-01-24-09-25-06",
    max_tokens=1950,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
)

# Print the generated text
print(response.choices[0].text)
