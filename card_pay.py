import config
import logging
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

vote = KeyboardButton('✅ Ovoz berish')
balance = KeyboardButton('💰 Hisobim')
top = KeyboardButton('🏆 TOP 10')

greet_kb = ReplyKeyboardMarkup(
    resize_keyboard=True).add(vote).add(balance).add(top)


hello_text = """Assalomu alaykum!

Aziz foydalanuvchi siz oʻz ovozingizni berish orqali botdan 2000 so'm paynet sohibi boʼlishiz mumkin.
Unutmang sizning ovozingiz bizning mahallamizni obodonlashtirish uchun juda muhim!"""


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(hello_text, reply_markup=greet_kb)


@dp.message_handler(commands=['vote'])
async def process_vote_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=greet_kb1)

@dp.message_handler(commands=['balance'])
async def process_balance_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры", reply_markup=greet_kb2)


@dp.message_handler(commands=['top'])
async def process_top_command(message: types.Message):
    await message.reply("🏆 TOP 10 eng ko'p ovoz berganlar:", reply_markup=greet_kb)

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
