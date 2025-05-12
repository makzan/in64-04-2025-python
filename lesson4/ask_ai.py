
def ask_ai(prompt):
    import requests

    with open("openrouter-api-key.txt", "r") as file:
        api_key = file.read().strip()

    url = "https://openrouter.ai/api/v1/chat/completions"

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    payload = {
        "model": "google/gemini-2.0-flash-001",
        "messages": messages
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    return data["choices"][0]["message"]["content"]

if __name__ == "__main__":
    input_prompot = input("Enter your prompt: ")
    response = ask_ai(input_prompot)
    print("AI Response:")
    print(response)
