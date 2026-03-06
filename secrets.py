import os

def get_secret(name):
    return os.getenv(name)

api_key = get_secret("OPENAI_API_KEY")

if api_key:
    print("API key loaded successfully")
else:
    print("API key not found. Please set it in your environment variables.")
