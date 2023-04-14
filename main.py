from datetime import timedelta, date
import requests
import asyncio
import aiohttp
import re
import sqlite3
import json
import random


from datetime import date
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from keyboards import *
from config import *
from pagination import InlinePagination, InlinePagination2, FavoritesPagination, NewsPagination
from db import Sqliter
import asyncio
import functools
import itertools
import logging
import time
import typing

import aiohttp
from aiohttp.helpers import sentinel

bot = Bot(token=TOKEN)#, parse_mode='HTML'
admin_id = admins
chatid = chat
storage = MemoryStorage()
dp = Dispatcher(bot)#, storage=storage
scheduler = AsyncIOScheduler()
db = Sqliter('database.db')
temp_film = []
temp_series = []
temp_chanel = []
@dp.message_handler(content_types=['photo'])
async def scan_message(msg: types.Message):
    document_id = msg.photo[0].file_id
    file_info = await bot.get_file(document_id)
    print(f'file_id: {file_info.file_id}')
    print(f'file_path: {file_info.file_path}')
    print(f'file_size: {file_info.file_size}')
    print(f'file_unique_id: {file_info.file_unique_id}')
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def process_photo(message: types.Message):
    # Получаем список фотографий в сообщении
    photos = message.photo

    # Перебираем фотографии и обрабатываем их
    for photo in photos:
        # Скачиваем фотографию
        await photo.download()
        # Обрабатываем фотографию (например, сохраняем ее в базу данных)
        #process_photo(photo.file)
category_list = {'films': 'Фильмы', 'serials' : 'Сериалы','series' : 'Сериалы', 'cartoons':'Мультфильмы', 'cartoon':'Мультфильмы', 'cartoon-serials' : 'Мультсериалы', 'cartoon-series': 'Мультсериалы', 'anime-film': 'Аниме-фильмы', 'anime' : 'Аниме-фильмы', 'anime-serials' : 'Аниме-сериалы', 'anime-series' : 'Аниме-сериалы', 'tv-shows' : 'ТВ-Шоу', 'tv-show': 'ТВ-Шоу', 'film': 'Фильмы'}
last_domain = ''

'''
@dp.message_handler(content_types=['photo'])
async def handle_text(message: types.Message, state: FSMContext):
    #temp_film.append(message.text)
    print("YESsss")
    img_id =  message.photo[-1].file_id
    await bot.send_message(message.from_user.id, 'Фильм успешно добавлен', reply_markup=AdminError)
    #await message.photo[-1].download(destination_file=f'D:/Рабочий стол/images/test.jpg')
    try:
        #db.add_film(temp_film)
        await bot.send_message(message.from_user.id, 'Фильм успешно добавлен',reply_markup=AdminError)
    except:
        await bot.send_message(message.from_user.id, 'Неверно введены данные',reply_markup=series_back)'''
class GetUserInfo(StatesGroup):
    us_zapros_video = State()
    us_zapros_film = State()
    us_zapros_serial = State()
    us_zapros_animefilm = State()
    us_zapros_animeser = State()
    us_zapros_cartoon = State()
    us_zapros_cartoonser = State()
    us_zapros_tv = State()
    us_zapros_film_number = State()
    us_zapros_serial_number = State()
    us_zapros_animefilm_number = State()
    us_zapros_animeser_number = State()
    us_zapros_cartoon_number = State()
    us_zapros_cartoonser_number = State()
    us_zapros_tv_number = State()
    us_add_film = State()
    us_add_series = State()
    us_add_admin = State()
    us_add_chanel = State()
    us_del_film = State()
    us_del_series = State()
    us_del_admin = State()
    us_del_chanel = State()
    us_add_film1 = State()
    us_add_film2 = State()
    us_add_film3 = State()
    us_add_film4 = State()
    us_add_film5 = State()
    us_add_film6 = State()
    us_add_series1 = State()
    us_add_series2 = State()
    us_add_series3 = State()
    us_add_series4 = State()
    us_add_series5 = State()
    us_add_series6 = State()
    us_add_chanel1 = State()
    us_add_chanel2 = State()
    us_add_chanel3 = State()
    search_film = State()
    search_series = State()



database = open("users_id.txt", "r", encoding="utf-8")
datausers = set()
for line in database:
    datausers.add(line.strip())
database.close()

@dp.callback_query_handler(text="about", state="*")
async def send(call: types.CallbackQuery):
  await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= '<a href="https://bot.kinozzz.ru/poster/about.png">🎞️</a> <b><u>Kinozzz Bot</u></b> — <b>первый онлайн-кинотеатр</b> в Telegram, который предоставляет возможность <b><u>бесплатно</u></b> наслаждаться новинками <b>Российского</b> и <b>зарубежного</b> кинематографа.\n\n💡 <b>Основные возможности бота:</b>\n— Удобный поиск фильмов, сериалов, ТВ-шоу, мультфильмов и т.п. по названию;\n— <b>Подборки</b> видеоматериалов;\n— Функция <b>«Мои закладки»</b>, чтобы любимые фильмы и сериалы были всегда рядом;\n— Удобный плеер;\n— Высокое качество каждого видеоматериала;\n— Ежедневное пополнение новинками кино.', reply_markup=about)

@dp.callback_query_handler(text="contacts", state="*")
async def send(call: types.CallbackQuery):
  await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= 'По поводу рекламы писать https://t.me/Informis_mors', reply_markup=AdminError)

async def check_sub_channel(chanels,user_id):
    for chanel in chanels:
        chat_member = await bot.get_chat_member(chat_id=chanel[1],user_id=user_id)
        if chat_member['status'] == 'left':
            return False
    return True



@dp.callback_query_handler(text = 'subchanneldone')
async def subchanneldone(message:types.Message):
    CHANNELS = db.get_chanels()
    if await check_sub_channel(CHANNELS, message.from_user.id):
        await bot.send_message(message.from_user.id, "Вы успешно подписались на все каналы!")
        await bot.send_message(chat_id=message.from_user.id,
                                    text='🏠 Вы вернулись в <b>главное меню</b>.\n\n<a href="https://bot.kinozzz.ru/poster/general.png">🎦</a> Здесь вы можете выбрать <b>раздел</b>, в котором желаете найти или выбрать видеоматериал для просмотра.',
                                    reply_markup=inlinekeyboard)

    else:
        await bot.send_message(chat_id=message.from_user.id, text="Вы подписались не на все каналы!", reply_markup=get_chanels())

@dp.message_handler(commands = ['start'])
async def start(message:types.Message):
    if message.chat.type == 'private':
        temp = get_chanels()
        await bot.send_message(chat_id=message.from_user.id, text="Привет! Чтобы пользоваться данным ботом надо подписаться на следующие каналы",reply_markup=temp)

@dp.callback_query_handler(text="poisk", state="*")
async def send(call: types.CallbackQuery):
    CHANNELS = db.get_chanels()
    if not await check_sub_channel(CHANNELS, call.message.chat.id):
        await bot.send_message(chat_id=call.message.chat.id, text="Вы подписались не на все каналы!",reply_markup=get_chanels())
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= '<a href="https://bot.kinozzz.ru/poster/poisk.png">🔍</a> Вы перешли в раздел <b>«Поиск по коду»</b>, пожалуйста, выберите поиск сериала или фильма.', reply_markup=search)

#поиск сериала по коду
@dp.callback_query_handler(text="search_series", state="*")
async def send(call: types.CallbackQuery):
    CHANNELS = db.get_chanels()
    if not await check_sub_channel(CHANNELS, call.message.chat.id):
        await bot.send_message(chat_id=call.message.chat.id, text="Вы подписались не на все каналы!",reply_markup=get_chanels())
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Введите код сериала.')
        await GetUserInfo.search_series.set()
        await call.answer()
        @dp.message_handler(state=GetUserInfo.search_series)
        async def handle_text(message: types.Message, state: FSMContext):
            series = db.get_series(message.text)
            if(series):
                s = f'Название сериала:{series[0][1]}\n\nДлительность: {series[0][3]} минут\n\nГод выпуска: {series[0][2]}\n\nОписание:\n{series[0][4]}\n\n'
                await bot.send_photo(chat_id=message.from_user.id, caption=s, photo=series[0][5])
                await bot.send_message(message.from_user.id, 'Хотите вернуться к поиск?', reply_markup=search_back)
            else:
                await bot.send_message(message.from_user.id, 'Сериала с таким кодом не найдено', reply_markup=search_back)
            await state.finish()
#поиск фильма по коду
@dp.callback_query_handler(text="search_films", state="*")
async def send(call: types.CallbackQuery):
    CHANNELS = db.get_chanels()
    if not await check_sub_channel(CHANNELS, call.message.chat.id):
        await bot.send_message(chat_id=call.message.chat.id, text="Вы подписались не на все каналы!",
                               reply_markup=get_chanels())
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Введите код фильма.')
        await GetUserInfo.search_film.set()
        await call.answer()
        @dp.message_handler(state=GetUserInfo.search_film)
        async def handle_text(message: types.Message, state: FSMContext):

            film = db.get_film(message.text)
            if(film):
                s = f'Название фильма:{film[0][1]}\n\nДлительность: {film[0][3]} минут\n\nГод выпуска: {film[0][2]}\n\nОписание:\n{film[0][4]}\n\n'
                await bot.send_photo(chat_id=message.from_user.id,caption=s, photo=film[0][5])
                await bot.send_message(message.from_user.id, 'Хотите вернуться к поиск?', reply_markup=search_back)
            else:
                await bot.send_message(message.from_user.id, 'Фильма с таким кодом не найдено')
            await state.finish()
@dp.message_handler(commands=["admin"])
async def send_all(message):
  admins = db.get_admins()
  if message.from_user.id not in admins:
    await bot.send_message(message.from_user.id, "Вы не являетесь администратором", reply_markup=AdminError)
  else:
      await bot.send_message(message.from_user.id, "Выберите, что вы хотите сделать", reply_markup=Admin)

@dp.callback_query_handler(text=["add_film"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    temp_film = []
    await bot.send_message(call.message.chat.id, "Напишите код фильма",reply_markup=Admin_back1)
    await GetUserInfo.us_add_film1.set()
    await call.answer()

    @dp.message_handler(state=GetUserInfo.us_add_film1)
    async def handle_text(message: types.Message, state: FSMContext):
        temp_film.append(message.text)
        await bot.send_message(message.from_user.id,"Напишите название фильма",reply_markup=Admin_back1)
        await state.finish()
        await GetUserInfo.us_add_film2.set()

        @dp.message_handler(state=GetUserInfo.us_add_film2)
        async def handle_text(message: types.Message, state: FSMContext):
            temp_film.append(message.text)
            await bot.send_message(message.from_user.id, "Напишите дату выхода фильма", reply_markup=Admin_back1)
            await state.finish()
            await GetUserInfo.us_add_film3.set()


            @dp.message_handler(state=GetUserInfo.us_add_film3)
            async def handle_text(message: types.Message, state: FSMContext):
                temp_film.append(message.text)
                await bot.send_message(message.from_user.id, "Напишите длительность фильма в минутах", reply_markup=Admin_back1)
                await state.finish()
                await GetUserInfo.us_add_film4.set()


                @dp.message_handler(state=GetUserInfo.us_add_film4)
                async def handle_text(message: types.Message, state: FSMContext):
                    temp_film.append(message.text)
                    await bot.send_message(message.from_user.id, "Напишите описание фильма", reply_markup=Admin_back1)
                    await state.finish()
                    await GetUserInfo.us_add_film5.set()

                    @dp.message_handler(state=GetUserInfo.us_add_film5)
                    async def handle_text(message: types.Message, state: FSMContext):
                        temp_film.append(message.text)
                        await bot.send_message(message.from_user.id, "Напишите Url к картинке", reply_markup=Admin_back1)
                        await state.finish()
                        await GetUserInfo.us_add_film6.set()

                        @dp.message_handler(content_types=types.ContentTypes.PHOTO, state=GetUserInfo.us_add_film6)
                        async def handle_photo_message(message: types.Message, state: FSMContext):
                            # process the photo message here
                            print("Received a photo message")

                            await state.finish()


    #await state.finish()


@dp.callback_query_handler(text=["add_series"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    temp_film = []
    await bot.send_message(call.message.chat.id, "Напишите код сериала",reply_markup=Admin_back1)
    await GetUserInfo.us_add_series1.set()
    await call.answer()

    @dp.message_handler(state=GetUserInfo.us_add_series1)
    async def handle_text(message: types.Message, state: FSMContext):
        temp_film.append(message.text)
        await bot.send_message(message.from_user.id,"Напишите название сериала",reply_markup=Admin_back1)
        await state.finish()
        await GetUserInfo.us_add_series2.set()

        @dp.message_handler(state=GetUserInfo.us_add_series2)
        async def handle_text(message: types.Message, state: FSMContext):
            temp_film.append(message.text)
            await bot.send_message(message.from_user.id, "Напишите дату выхода сериала", reply_markup=Admin_back1)
            await state.finish()
            await GetUserInfo.us_add_series3.set()


            @dp.message_handler(state=GetUserInfo.us_add_series3)
            async def handle_text(message: types.Message, state: FSMContext):
                temp_film.append(message.text)
                await bot.send_message(message.from_user.id, "Напишите длительность сериала в минутах", reply_markup=Admin_back1)
                await state.finish()
                await GetUserInfo.us_add_series4.set()


                @dp.message_handler(state=GetUserInfo.us_add_series4)
                async def handle_text(message: types.Message, state: FSMContext):
                    temp_film.append(message.text)
                    await bot.send_message(message.from_user.id, "Напишите описание сериала", reply_markup=Admin_back1)
                    await state.finish()
                    await GetUserInfo.us_add_series5.set()

                    @dp.message_handler(state=GetUserInfo.us_add_series5)
                    async def handle_text(message: types.Message, state: FSMContext):
                        temp_film.append(message.text)
                        await bot.send_message(message.from_user.id, "Напишите Url к картинке", reply_markup=Admin_back1)
                        await state.finish()
                        await GetUserInfo.us_add_series6.set()

                        @dp.message_handler(state=GetUserInfo.us_add_series6)
                        async def handle_text(message: types.Message, state: FSMContext):
                            temp_film.append(message.text)
                            try:
                                db.add_series(temp_film)
                                await bot.send_message(message.from_user.id, 'Сериал успешно добавлен',reply_markup=AdminError)
                            except:
                                await bot.send_message(message.from_user.id, 'Неверно введены данные',reply_markup=series_back)
                            await state.finish()

@dp.callback_query_handler(text=["add_chanel"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    temp_film = []
    await bot.send_message(call.message.chat.id, "Напишите название канала",reply_markup=Admin_back1)
    await GetUserInfo.us_add_chanel1.set()
    await call.answer()

    @dp.message_handler(state=GetUserInfo.us_add_chanel1)
    async def handle_text(message: types.Message, state: FSMContext):
        temp_film.append(message.text)
        await bot.send_message(message.from_user.id,"Напишите id канала",reply_markup=Admin_back1)
        await state.finish()
        await GetUserInfo.us_add_chanel2.set()

        @dp.message_handler(state=GetUserInfo.us_add_chanel2)
        async def handle_text(message: types.Message, state: FSMContext):
            temp_film.append(message.text)
            await bot.send_message(message.from_user.id, "Напишите Url канала", reply_markup=Admin_back1)
            await state.finish()
            await GetUserInfo.us_add_chanel3.set()


            @dp.message_handler(state=GetUserInfo.us_add_chanel3)
            async def handle_text(message: types.Message, state: FSMContext):
                temp_film.append(message.text)
                try:
                    db.add_chanel(temp_film)
                    await bot.send_message(message.from_user.id, 'Канал успешно добавлен', reply_markup=AdminError)
                except:
                    await bot.send_message(message.from_user.id, 'Неверно введены данные', reply_markup=Admin_back)
                await state.finish()


@dp.callback_query_handler(text=["add_admin"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    await bot.send_message(call.message.chat.id, "Напишите id нового админа",reply_markup=Admin_back1)
    await GetUserInfo.us_add_admin.set()
    await call.answer()
    @dp.message_handler(state=GetUserInfo.us_add_admin)
    async def handle_text(message: types.Message, state: FSMContext):
        data = []
        data.append(message.text)
        try:
            db.add_admin(data)
            await bot.send_message(message.from_user.id, 'Админ успешно добавлен', reply_markup=AdminError)
        except:
            await bot.send_message(message.from_user.id, 'Неверно введены данные', reply_markup=Admin_back)
        await state.finish()



@dp.callback_query_handler(text=["del_film"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    await bot.send_message(call.message.chat.id, "Введите код фильма,которого хотите удалить",reply_markup=Admin_back1)
    await GetUserInfo.us_del_film.set()
    await call.answer()
    @dp.message_handler(state=GetUserInfo.us_del_film)
    async def handle_text(message: types.Message, state: FSMContext):
        try:
            db.del_film(message.text)
            await bot.send_message(call.message.chat.id, "Вы успешно удалили фильм", reply_markup=AdminError)
        except:
            await bot.send_message(call.message.chat.id, "Кода c таким фильма нет",reply_markup=film_back1)
        await state.finish()

@dp.callback_query_handler(text=["del_series"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    await bot.send_message(call.message.chat.id, "Введите код сериала,которого хотите удалить",reply_markup=Admin_back1)
    await GetUserInfo.us_del_series.set()
    await call.answer()
    @dp.message_handler(state=GetUserInfo.us_del_series)
    async def handle_text(message: types.Message, state: FSMContext):
        try:
            db.del_series(message.text)
            await bot.send_message(call.message.chat.id, "Вы успешно удалили сериал", reply_markup=AdminError)
        except:
            await bot.send_message(call.message.chat.id, "Кода c таким сериалом нет",reply_markup=series_back1)
        await state.finish()

@dp.callback_query_handler(text=["del_admin"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    await bot.send_message(call.message.chat.id, "Введите id админа,которого хотите удалить",reply_markup=Admin_back1)
    await GetUserInfo.us_del_admin.set()
    await call.answer()
    @dp.message_handler(state=GetUserInfo.us_del_admin)
    async def handle_text(message: types.Message, state: FSMContext):
        try:
            db.del_admin(message.text)
            await bot.send_message(call.message.chat.id, "Вы успешно удалили админа", reply_markup=AdminError)
        except:
            await bot.send_message(call.message.chat.id, "Админа с таким id нет",reply_markup=series_back1)
        await state.finish()

@dp.callback_query_handler(text=["del_chanel"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    await bot.send_message(call.message.chat.id, "Введите id канала,которого хотите удалить",reply_markup=Admin_back1)
    await GetUserInfo.us_del_chanel.set()
    await call.answer()
    @dp.message_handler(state=GetUserInfo.us_del_chanel)
    async def handle_text(message: types.Message, state: FSMContext):
        try:
            db.del_chanel(message.text)
            await bot.send_message(call.message.chat.id, "Вы успешно удалили канал", reply_markup=AdminError)
        except:
            await bot.send_message(call.message.chat.id, "Канала с таким id нет",reply_markup=chanel_back1)
        await state.finish()

@dp.callback_query_handler(text=["get_film"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    films = db.get_film1()
    s = "Имеющийся фильмы:\n"
    i = 1
    for film in films:
        s+=f'{i}) Код фильма: {film[0]}\nНазвание: {film[1]}\nДата выхода: {film[2]}\nДлительность: {film[3]}\nОписание: {film[4]}\n\n'
    await bot.send_message(call.message.chat.id, s, reply_markup=gotohome)
    #await bot.send_photo(call.message.chat.id, photo=films[1][5])

@dp.callback_query_handler(text=["get_series"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    series = db.get_series1()
    s = "Имеющийся сериалы:\n"
    i = 1
    for film in series:
        s+=f'{i}) Код сериала: {film[0]}\nНазвание: {film[1]}\nДата выхода: {film[2]}\nДлительность: {film[3]}\nОписание: {film[4]}\n\n'
    await bot.send_message(call.message.chat.id, s, reply_markup=gotohome)

@dp.callback_query_handler(text=["get_admin"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    admins = db.get_admins()
    s = "Имеющийся Админы:\n"
    i = 1
    for admin in admins:
        s+=f'{i}) Id Админа: {admin}\n'
    await bot.send_message(call.message.chat.id, s, reply_markup=gotohome)

@dp.callback_query_handler(text=["get_chanel"])
async def add_(call: types.CallbackQuery):
  admins = db.get_admins()
  if call.message.chat.id not in admins:
    await bot.send_message(call.message.chat.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)
  else:
    chanels = db.get_chanels()
    s = "Имеющийся каналы:\n"
    i = 1
    for chanel in chanels:
        s+=f'{i}) Название канала: {chanel[0]}\n: Id канала: {chanel[1]}\nUrl канала: {chanel[2]}\n\n'
    await bot.send_message(call.message.chat.id, s, reply_markup=gotohome)

@dp.callback_query_handler(text="random", state="*")
async def back(call: types.CallbackQuery, state: FSMContext):
    CHANNELS = db.get_chanels()
    if not await check_sub_channel(CHANNELS, call.message.chat.id):
        await bot.send_message(chat_id=call.message.chat.id, text="Вы подписались не на все каналы!",
                               reply_markup=get_chanels())
    else:
        mas = db.get_series1()
        mas1 = db.get_film1()
        type = random.randint(1,2)
        if len(mas) == 0:
            type = 2
        elif len(mas1) == 0:
            type = 2
        elif len(mas1) == 0 and len(mas):
            await bot.send_message(chat_id=call.message.chat.id,text="Пока что не добавлена ни фильма,ни сериала")
        if type == 1:
            series = random.choice(mas)
            s = f'Название сериала:{series[1]}\n\nДлительность: {series[3]} минут\n\nГод выпуска: {series[2]}\n\nОписание:\n{series[4]}\n\n'
            await bot.send_photo(chat_id=call.message.chat.id, caption=s, photo=series[5])
        else:
            series = random.choice(mas1)
            s = f'Название фильма:{series[1]}\n\nДлительность: {series[3]} минут\n\nГод выпуска: {series[2]}\n\nОписание:\n{series[4]}\n\n'
            await bot.send_photo(chat_id=call.message.chat.id, caption=s, photo=series[5])
        await bot.send_message(call.message.chat.id, 'Хотите вернуться в главное меню?', reply_markup=gotohome)



@dp.callback_query_handler(text="back", state="*")
async def back(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    CHANNELS = db.get_chanels()
    if not await check_sub_channel(CHANNELS, call.message.chat.id):
        await bot.send_message(chat_id=call.message.chat.id, text="Вы подписались не на все каналы!",
                               reply_markup=get_chanels())
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= '🏠 Вы вернулись в <b>главное меню</b>.\n\n<a href="https://bot.kinozzz.ru/poster/general.png">🎦</a> Здесь вы можете выбрать <b>раздел</b>, в котором желаете найти или выбрать видеоматериал для просмотра.', reply_markup=inlinekeyboard, inline_message_id=call.inline_message_id)

@dp.message_handler(content_types=['text'])
async def send_all(message):
  await bot.send_message(message.from_user.id, f'❗К сожалению, ваш запрос не распознан!\n\n<a href="https://bot.kinozzz.ru/poster/error.png">🏠</a> <i>Вернитесь в <b>главное меню</b></i>.', reply_markup=exit)



async def on_startup(dp: Dispatcher):
    print('~~~ Bot успешно запущен! ~~~')
    print('~~~ Заходи к нам на форум ~~~')
    print('~~~ url - https://na-sha.ru/ ~~~')
    await bot.send_message(chat_id=admin_id[0], text='🚀 <b>Ваш Bot</b> успешно запущен!\nДля запуска бота введите <b>/start</b>\nПосмотреть статистику <b>/stats</b>\nСделать рассылку <b>/all и Ваш текст</b>')#добавить отправлние всем админам
    # await update_popular_anime()
    # await update_popular_mult()
    # await update_news_films()
    # await update_popular()
    # await update_collections()
    # await update_popular_show()
    '''
    scheduler.add_job(update_news_films, 'cron', hour=11, minute=16)
    scheduler.add_job(update_news_serials, 'cron', hour=12, minute=29)
    scheduler.add_job(update_news_show, 'cron', hour=13, minute=18)
    # scheduler.add_job(update_domain, 'interval', minutes=60)
    scheduler.add_job(update_popular, 'cron', hour=1, minute=10)
    scheduler.add_job(update_popular_mult, 'cron', hour=2, minute=30)
    scheduler.add_job(update_popular_anime, 'cron', hour=3, minute=50)
    scheduler.add_job(update_popular_show, 'cron', hour=5, minute=40)
    scheduler.add_job(update_collections_films, 'cron', hour=7, minute=10)
    scheduler.add_job(update_collections, 'cron', hour=23, minute=40)
    '''
if __name__ == "__main__":
    scheduler = AsyncIOScheduler(timezone="Europe/Minsk")
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)

