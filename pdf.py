import os
from openai import OpenAI

# Initialize the client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
     api_key=st.secrets["HF_TOKEN"],   # your HF token
)

# Conversation history
messages = []

print("AI Chatbot (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    # Append user message
    messages.append({"role": "user", "content": user_input})

    # Get response from model
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b:novita",  # Hugging Face model
        messages=messages
    )

    # Extract and print assistant's reply
    reply = completion.choices[0].message.content
    print(f"Bot: {reply}")

    # Append bot reply to history
    messages.append({"role": "assistant", "content": reply})
