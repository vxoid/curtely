## Curtely v0.0.1 Telegram API wrapper
## Change log
- First release
## Usage
```python
# Here is an example of an easy echo bot
import curtely

TOKEN = "your-telegram-bot-token"

def handler(bot: curtely.TelegramAPI, message: curtely.Message):
    bot.send_message(message.reply(message.content()))

bot = curtely.TelegramAPI(TOKEN)

bot.handle_updates(handler)
```