from aiogram import Bot, Dispatcher, F, filters, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
import asyncio
import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPEN_AI_TOKEN')
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="President of USA"), KeyboardButton(text="President of Russia"), KeyboardButton(text="President of Uzbekistan")],
    [KeyboardButton(text="Elon Musk"), KeyboardButton(text="Steve Jobs"), KeyboardButton(text="MrBeast")],
    [KeyboardButton(text="Eminem"), KeyboardButton(text="Mike Tyson"), KeyboardButton(text="Cristiano Ronaldo")]
],resize_keyboard=True)

@dp.message(filters.CommandStart())
async def start_bot(message: types.Message):
    await message.answer(text="Hello, I'm ChatGPT bot\nselect the person you want to chat with", reply_markup=kb)

@dp.message(F.text == "President of USA")
async def usa_president(message: Message):
    await message.answer(text="I'm looking for oil now, bye")

@dp.message(F.text == "President of Russia")
async def usa_president(message: Message):
    await message.answer(text="президент россии не может с тобой общаться")

@dp.message(F.text == "President of Uzbekistan")
async def usa_president(message: Message):
    await message.answer(text="Paxta bizning milliy boyligimiz")

@dp.message(F.text == "Elon Musk")
async def usa_president(message: Message):
    await message.answer(text="This is an answering machine, leave a message")

@dp.message(F.text == "Steve Jobs")
async def usa_president(message: Message):
    await message.answer(text="you need to buy an iPhone")

@dp.message(F.text == "MrBeast")
async def usa_president(message: Message):
    await message.answer(text="next video on YouTube next week")

@dp.message(F.text == "Eminem")
async def usa_president(message: Message):
    await message.answer(text="do you want to rap? go to karaoke")

@dp.message(F.text == "Mike Tyson")
async def usa_president(message: Message):
    await message.answer(text="I don't want to be your trainer bye")

@dp.message(F.text == "Cristiano Ronaldo")
async def usa_president(message: Message):
    await message.answer(text="not today next time, okay?")

@dp.message()
async def gpt_bot(message: types.Message):
    user_input = message.text
    response = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=user_input,
        max_tokens=1000,
        temperature=0.7,
    )
    await message.answer(text=f"{response.choices[0].text.strip()}")
     

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
