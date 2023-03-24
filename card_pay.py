import config
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

VOTE = '✅ Ovoz berish'
VOTE1 = '✅ Ovoz berdim!'
BALANCE = '💰 Hisobim'
TOP = '🏆 TOP 10'
CHECK_MON = '📥 Pulni yechib olish'
HOME = '🏠 Bosh sahifa'

PAYNET = '2114616411'
CLICK = '1807098590'

TEL = '📞 TELEFONGA'
PLASTIC = '💳 PLASTIKGA (HUMO, UZCARD)'
BACK = '🔙 ORTGA'
BACK1 = '🔙 ORTGA-'

HELLO_TEXT = """Assalomu alaykum!

Aziz foydalanuvchi siz oʼz ovozingizni berish orqali botdan 2000 so'm paynet sohibi boʼlishiz mumkin.
Unutmang sizning ovozingiz bizning mahallamizni obodonlashtirish uchun juda muhim!"""

LINK = '''https://openbudget.uz/boards-list/1/a5c12dea-03b8-4301-ad27-01d18c1a8023

OVOZ BERISH TARTIBI
1⃣ Tepadagi 👆ko'k rangli yozib ustiga bosing.⏭
2⃣Sahifa to'liq ochilgandan so'ng pastroqqa tushib "Овоз бериш" tugmasining ustiga bosing⏭
3⃣So'ralgan joyga mobil raqamingizni kiriting hamda pastidagi oson matematik hisobni to'g'ri javobini yozing va sizga kelgan 6 xonali kodni kiriting⏭
4⃣So'ng  "Oвозингиз муваффакиятли кабул килинди" yozuvi chiqsa siz shunday muborak kunlarda maktab qurishdek ulkan ishga ehson qilish hissangizni qo'shgan bo'lasiz !!!

HURMAT BILAN ANDIJON TUMANI 6-MAKTAB JAMOASI !!!
Agar hammasini tog'ri bajargan bo'lsangiz '✅ Ovoz berdim!' tugmasini bosing'''


@dp.message_handler(lambda message: message.text == VOTE1)
async def vote_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=TEL),
            types.KeyboardButton(text=HOME),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    text = '''Bergan ovozingiz uchun rahmat!\nSizga qulay to'lov turini tanlang.'''
    await message.reply(text, reply_markup=keyboard)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=VOTE),
            # types.KeyboardButton(text=BALANCE),
            types.KeyboardButton(text=TOP),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(HELLO_TEXT, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == HOME or message.text == BACK)
async def home_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=VOTE),
            # types.KeyboardButton(text=BALANCE),
            types.KeyboardButton(text=TOP),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(HOME, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == VOTE)
async def vote_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=VOTE1),
            types.KeyboardButton(text=BACK)
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply('''Har bir ovozingiz uchun hisobingizga 2000 so'm qo'shiladi.''')
    await message.reply(LINK, reply_markup=keyboard)


# @dp.message_handler(
#     lambda message: message.text == BALANCE or message.text == BACK)
# async def balance_but(message: types.Message):
#     kb = [
#         [
#             types.KeyboardButton(text=CHECK_MON),
#             types.KeyboardButton(text=HOME)
#         ],
#     ]
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb,
#         resize_keyboard=True
#     )
#     text = f'''Hozirgi balansingiz: {balance}so'm'''
#     await message.reply(text, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == TOP)
async def top_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=VOTE),
            # types.KeyboardButton(text=BALANCE),
            types.KeyboardButton(text=TOP),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("🏆 TOP 10 eng ko'p ovoz berganlar:",
                        reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == TEL)
async def tel_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=HOME),
            types.KeyboardButton(text=BACK1),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    # text = 'Paynet 2000 sum\nTel:'
    # await bot.send_message(PAYNET, text)
    await message.reply("5 Daqiqa ichida ushbu telefon no'meringizga paynet qilinadi!",
                        reply_markup=keyboard)


@dp.message_handler(
    lambda message: message.text == CHECK_MON or message.text == BACK1)
async def check_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=TEL),
            # types.KeyboardButton(text=PLASTIC),
            types.KeyboardButton(text=BACK),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    print(balance)
    text = '''Telefonga pul yechib olish uchun hisobingizda 1000 so'mdan ko'p pul bo'lishi kerak!\nHozirgi balansingiz: 0 so'm'''
    if balance < 1000:
        await message.reply(text, reply_markup=keyboard)
    else:
        await message.reply("Sizga qulay to'lov turini tanlang.",
                        reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
