import os

from dotenv import load_dotenv
import telebot

from voices import voice_generator

load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

voices = voice_generator.get_all_voices()
voice_buttons = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

for v in voices:
    button = telebot.types.KeyboardButton(v['name'])
    voice_buttons.add(button)

selected_voice = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привет! Я бот для создания озвучки! Выбери голос, который будет использоваться при создании озвучки:",
                 reply_markup=voice_buttons)


@bot.message_handler(func=lambda message: message.text in [v['name'] for v in voices])
def voice_selected(message):
    user_id = message.from_user.id
    selected_voice[user_id] = message.text
    bot.reply_to(message, f"Вы выбрали голос: {message.text}. Теперь введите текст для озвучки:")


@bot.message_handler(func=lambda message: True)
def generate_voice(message):
    user_id = message.from_user.id
    if user_id in selected_voice:
        voice_name = selected_voice[user_id]
        voice_id = next(v['id'] for v in voices if v['name'] == voice_name)
        audio_file = voice_generator.generate_audio(message.text, voice_id)

        with open(audio_file, 'rb') as audio:
            bot.send_voice(user_id, audio)
    else:
        bot.reply_to(message, "Сначала выберите голос командой /start")


if __name__ == '__main__':
    bot.polling(none_stop=True)
