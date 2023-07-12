import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create Telegram bot
bot_token = '6345564172:AAGFI3hSqJLalAf3rhvYaXSz3AOzZTf4l38'
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def handle_start_help(message: types.Message):
    await message.reply("Welcome! Please fill out the form.")


@dp.message_handler()
async def handle_form_submission(message: types.Message):
    # Extract form data from the message
    name = message.from_user.full_name
    email = message.from_user.username
    budget = message.text  # Replace with the appropriate form field

    # Prepare the message to be sent to the chat
    chat_id = '-1667241343'  # Replace with the actual chat ID
    response_message = f"<b>New form submission:</b>\n\n"
    response_message += f"<b>Name:</b> {name}\n"
    response_message += f"<b>Email:</b> {email}\n"
    response_message += f"<b>Budget:</b> {budget}"

    # Send the message to the chat
    await bot.send_message(chat_id, response_message, parse_mode=types.ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
