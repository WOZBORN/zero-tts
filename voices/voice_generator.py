import os
from dotenv import load_dotenv
from elevenlabs import save
from elevenlabs.client import ElevenLabs
import requests

load_dotenv()
client = ElevenLabs(
    api_key=os.getenv("ELEVEN_LABS_API_KEY"),
)


def get_all_voices():
    voices = client.voices.get_all()
    return [{'name': voice.name, 'id': voice.voice_id} for voice in voices.voices]


def generate_audio(text: str, voice: str):
    audio = client.generate(
        text=text,
        voice=voice,
        model="eleven_multilingual_v2"
    )

    character_count = len(text)
    print(f"Запрос потратил {character_count} символов.")

    name = "audio.mp3"
    save(audio, name)
    return name


def check_remaining_tokens():
    api_key = os.getenv("ELEVEN_LABS_API_KEY")
    url = "https://api.elevenlabs.io/v1/user/subscription"

    headers = {
        "xi-api-key": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        character_count = data['character_count']
        character_limit = data['character_limit']
        remaining_characters = character_limit - character_count

        print(f"Осталось {remaining_characters} символов из {character_limit}.")
        return remaining_characters
    else:
        print(f"Не удалось получить данные о подписке. Код ошибки: {response.status_code}")
        return None


