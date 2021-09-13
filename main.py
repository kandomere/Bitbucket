from aiogram import executor, Bot, types, Dispatcher
from config import TOKEN

import os
from datetime import datetime
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile
from PIL import Image, ImageDraw, ImageFont
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
text_file = os.getcwd() + '\\' + 't.txt'
images_dir = os.getcwd() + '\\' + 'images'
font_file = os.getcwd()+'\\'+'Lobster.ttf'
REPOST_CHANNEL = -1001277471725
# 

date_photo = f'{datetime.today().strftime(f"%Y-%m-%d_%H;%M_")}'

# buttons
btn_rep = InlineKeyboardButton('Да, переслать', callback_data='rep')
inline_kb = InlineKeyboardMarkup().add(btn_rep)





def photo_name(date_photo, user_id):
    return date_photo + str(user_id) + '.jpg'


def write_text(path_image):
    with open('t.txt', 'r', encoding="utf-8") as f:
        s = f.read().split('\n')
    text = random.choice(s)

    myimage = Image.open(path_image)
    font = ImageFont.truetype(font_file, 36)
    draw = ImageDraw.Draw(myimage)
    width_image, height_image = myimage.size

    width_text, height_text = draw.textsize(text, font=font)

    draw.text(((width_image - width_text) * 0.5, (height_image / 1.1)),
              text,
              font=font,
              fill=(255, 255, 255, 255))

    myimage.save(images_dir + '\\' + path_image.split('\\')[-1])
    # return create_dir + '\\' + path_image.split('\\')[-1]
    return images_dir + '\\' + path_image.split('\\')[-1]


# font_file

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Отправь мне картинку я напишу туда текст')


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    path_image = f'{images_dir}\\{photo_name(date_photo, message.from_user.id)}'
    await message.photo[-1].download(path_image)
    # await message.answer(message)

    # -1001277471725
    p = write_text(path_image)

    photo = InputFile(p)
    await bot.send_photo(chat_id=message.chat.id, photo=photo)
    await message.answer('Переслать в другую группу?', reply_markup=inline_kb)

    @dp.callback_query_handler(lambda c: c.data == 'rep')
    async def callback_inline(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        # await bot.send_photo(chat_id=-1001277471725, photo=photo)
        # photo = InputFile(create_dir + '\\' + path_image.split('\\')[-1])
        # await bot.send_photo(chat_id=-1001277471725, photo=photo)

        await bot.forward_message(chat_id=rep_channel, from_chat_id=message.chat.id,
                                  message_id=callback_query.message.message_id-1)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
