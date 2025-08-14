import requests
import uuid

SERVER_URL = "http://localhost:8080/chat"
session_id = str(uuid.uuid4())  # Unique session per run

# Ask provider at the start
while True:
    provider_choice = input("Choose provider (1 = Gemini, 2 = OpenAI): ").strip()
    if provider_choice == "1":
        provider = "gemini"
        break
    elif provider_choice == "2":
        provider = "openai"
        break
    else:
        print("❌ Invalid choice. Please type 1 or 2.")

print(f"💬 Chat session started with {provider} (sessionId: {session_id})")
print("Type your message and press Enter. Type 'exit' to quit.\n")

while True:
    try:
        message = input("You> ").strip()
        if message.lower() == "exit":
            print("👋 Goodbye!")
            break

        response = requests.post(
            SERVER_URL,
            json={
                "provider": provider,
                "sessionId": session_id,
                "message": message
            },
            timeout=10
        )

        if response.status_code != 200:
            print(f"❌ Error: {response.status_code} {response.reason}")
            continue

        data = response.json()
        print(f"{provider.capitalize()}> {data.get('reply', '(no reply)')}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        break