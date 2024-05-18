import openai as ai
import os

print(os.environ.get("OPENAI_API_KEY"))

client = ai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


# function to get input from user
def chat_to_gpt(prompt: str):
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("AI: ", chat_to_gpt(user_input))
