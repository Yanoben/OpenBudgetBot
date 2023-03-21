import config
import logging
# from aiogram.types import ReplyKeyboardRemove, \
#     ReplyKeyboardMarkup, KeyboardButton, \
# InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

vote = '✅ Ovoz berish'
balance = '💰 Hisobim'
top = '🏆 TOP 10'
check_mon = '📥 Pulni yechib olish'
home = '🏠 Bosh sahifa'

hello_text = """Assalomu alaykum!

Aziz foydalanuvchi siz oʼz ovozingizni berish orqali botdan 2000 so'm paynet sohibi boʼlishiz mumkin.
Unutmang sizning ovozingiz bizning mahallamizni obodonlashtirish uchun juda muhim!"""


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=vote),
            types.KeyboardButton(text=balance),
            types.KeyboardButton(text=top),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(hello_text, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == home)
async def home_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=vote),
            types.KeyboardButton(text=balance),
            types.KeyboardButton(text=top),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(home, reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == vote)
async def vote_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=vote),
            types.KeyboardButton(text=balance)
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply('''Har bir ovozingiz uchun hisobingizga 2000 so'm qo'shiladi.''')
    await message.reply('''Ovoz berish uchun telefon raqam kiriting.\nNamuna: +998991234567''',
                        reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == balance)
async def balance_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=check_mon),
            types.KeyboardButton(text=home)
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply('''Hozirgi balansingiz: 0 so'm''',
                        reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == top)
async def top_but(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text=vote),
            types.KeyboardButton(text=balance),
            types.KeyboardButton(text=top),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("🏆 TOP 10 eng ko'p ovoz berganlar:",
                        reply_markup=keyboard)

# # buy
# @dp.message_handler(commands=['buy'])
# async def buy(message: types.Message):
#     if config.PAYMENTS_TOKEN.split(':')[1] == 'TEST':
#         await bot.send_message(message.chat.id, "Тестовый платеж!!!")
 
#     await bot.send_invoice(message.chat.id,
#                            title="Подписка на бота",
#                            description="Активация подписки на бота на 1 месяц",
#                            provider_token=config.PAYMENTS_TOKEN,
#                            currency="rub",
#                            photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
#                            photo_width=416,
#                            photo_height=234,
#                            photo_size=416,
#                            is_flexible=False,
#                            prices=[PRICE],
#                            start_parameter="one-month-subscription",
#                            payload="test-invoice-payload")
 
 
# # pre checkout  (must be answered in 10 seconds)
# @dp.pre_checkout_query_handler(lambda query: True)
# async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
#     await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
 
 
# # successful payment
# @dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
# async def successful_payment(message: types.Message):
#     print("SUCCESSFUL PAYMENT:")
#     payment_info = message.successful_payment.to_python()
#     for k, v in payment_info.items():
#         print(f"{k} = {v}")

#     await bot.send_message(message.chat.id,
#                            f"Платёж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
