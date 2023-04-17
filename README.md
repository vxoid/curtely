## Curtely v0.0.2 Telegram API wrapper
## Change log
- Added `message_handler` decoretor and renamed `handle_updates` to `run`
## Usage
```python
# Here is an example of an easy echo bot
import curtely

TOKEN = "your-token-here"

bot = curtely.TelegramAPI(TOKEN)

@curtely.message_handler(bot)
def message_handler(api: curtely.TelegramAPI, message: curtely.Message):
    api.send_message(message.reply(message.content()))

bot.run()
```