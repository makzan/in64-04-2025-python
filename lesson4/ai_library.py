def ask_ai(prompt, image_url=None, model="google/gemini-2.0-flash-001"):
    import requests

    with open("openrouter-api-key.txt", "r") as file:
        api_key = file.read().strip()

    url = "https://openrouter.ai/api/v1/chat/completions"

    if image_url:
        
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        }
                    }
                ]
            }
        ]
    else:
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

    payload = {
        "model": model,
        "messages": messages
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    return data["choices"][0]["message"]["content"]