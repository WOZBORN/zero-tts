# ZeroTTS

ZeroTTS — это проект для преобразования текста в речь с использованием современных моделей глубокого обучения.

## Особенности

- **Генерация речи:** высококачественное преобразование текста в аудио.
- **Простота использования:** понятный интерфейс для быстрого старта.
- **Модульная структура:** легко настраиваемая архитектура.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/WOZBORN/zero-tts.git
   ```
2. Перейдите в папку проекта:
   ```bash
   cd zero-tts
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4 Получите api ключ на сайте Elevenlabs:
https://elevenlabs.io/

5. Получите токен телеграм-бота у BotFather:
https://telegram.me/BotFather

5. Создайте `.env` файл:
```
touch .env
```

6. Впишите в него ваш ключ api Elevenlabs и токен бота:
```
ELEVEN_LABS_API_KEY="ключ api elevenlabs"
BOT_TOKEN="токен бота"
```

## Использование

1. Запустите основной файл:
   ```bash
   python main.py
   ```
2. Следуйте инструкциям на экране для ввода текста и получения аудиофайла.

## Структура проекта

```plaintext
zero-tts/
│
├── main.py                # Точка входа программы
├── voices/
│   └── voice_generator.py # Генерация речи
├── requirements.txt       # Зависимости проекта
├── .env                   # Его нужно создать
```

### Основные файлы

- **main.py**: выполняет запуск программы, обрабатывает текст и сохраняет результат.
- **voice_generator.py**: отвечает за синтез речи, работу с моделью и сохранение аудиофайлов.

## Пример кода

Пример использования `VoiceGenerator` для генерации аудио:

```python
from voices.voice_generator import VoiceGenerator

# Инициализация генератора
voice_gen = VoiceGenerator()

# Загрузка модели
voice_gen.load_model("path/to/model")

# Синтез текста в аудио
audio_data = voice_gen.synthesize("Привет, мир!")

# Сохранение аудио
voice_gen.save_audio(audio_data, "output.wav")
```

## Вклад

Если вы хотите внести свой вклад в проект:

1. Форкните репозиторий.
2. Создайте ветку для изменений:
   ```bash
   git checkout -b feature-name
   ```
3. Внесите изменения и сделайте коммит:
   ```bash
   git commit -m "Описание изменений"
   ```
4. Отправьте изменения:
   ```bash
   git push origin feature-name
   ```
5. Создайте Pull Request.

## Лицензия

Проект распространяется под лицензией MIT. Подробнее см. в файле `LICENSE`.
