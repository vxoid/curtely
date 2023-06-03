## Curtely v0.0.3 Telegram API wrapper
## Change log
- Added `chat_id()` to `Message`
- Renamed `TelegramAPI` on `Bot`
## Usage
```python
# Here is an example of an easy echo bot
import curtely

TOKEN = "your-token-here"

bot = curtely.Bot(TOKEN)

@curtely.message_handler(bot)
def message_handler(api: curtely.Bot, message: curtely.Message):
    api.send_message(message.reply(message.content()))

bot.run()
```