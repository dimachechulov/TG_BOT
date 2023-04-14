from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import config
from main import db
inlinekeyboard = InlineKeyboardMarkup()
inlinekeyboard.add(InlineKeyboardButton(text="🔍 Поиск по коду", callback_data="poisk"))
inlinekeyboard.add(InlineKeyboardButton(text="Рандомный фильм/сериал", callback_data="random"))
inlinekeyboard.add(InlineKeyboardButton(text="💬 Контакты", callback_data="contacts"))

news_menu_kb = InlineKeyboardMarkup()
news_menu_kb.add(InlineKeyboardButton(text="Фильмы", callback_data="news_films"), InlineKeyboardButton(text="Сериалы", callback_data="news_serials"))
news_menu_kb.add(InlineKeyboardButton(text="ТВ-шоу", callback_data="news_show"))
news_menu_kb.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

popular_menu_kb = InlineKeyboardMarkup()
popular_menu_kb.add(InlineKeyboardButton(text="Фильмы", callback_data="popular_films"), InlineKeyboardButton(text="Сериалы", callback_data="popular_series"))
popular_menu_kb.add(InlineKeyboardButton(text="Мультфильмы", callback_data="popular_cartoon"), InlineKeyboardButton(text="Мультсериалы", callback_data="popular_cartoon_serials"))
popular_menu_kb.add(InlineKeyboardButton(text="Аниме-фильмы", callback_data="popular_anime"), InlineKeyboardButton(text="Аниме-сериалы", callback_data="popular_anime_serials"))
popular_menu_kb.add(InlineKeyboardButton(text="ТВ-шоу", callback_data="popular_show"))
popular_menu_kb.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

inlinekeyboard2 = InlineKeyboardMarkup()
inlinekeyboard2.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard3 = InlineKeyboardMarkup()
inlinekeyboard3.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard4 = InlineKeyboardMarkup()
inlinekeyboard4.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard5 = InlineKeyboardMarkup()
inlinekeyboard5.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard6 = InlineKeyboardMarkup()
inlinekeyboard6.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard7 = InlineKeyboardMarkup()
inlinekeyboard7.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

inlinekeyboard8 = InlineKeyboardMarkup()
inlinekeyboard8.add(InlineKeyboardButton(text="◀️ Категории", callback_data="categories"),
InlineKeyboardButton(text="🏠 Меню", callback_data="back"))

exit = InlineKeyboardMarkup()
exit.add(InlineKeyboardButton(text="🏠 Главное меню", callback_data="back"))

gotohome = InlineKeyboardMarkup()
gotohome.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

category = InlineKeyboardMarkup()
category.add(InlineKeyboardButton(text="Фильмы", callback_data="films"),
InlineKeyboardButton(text="Сериалы", callback_data="serials"))
category.add(InlineKeyboardButton(text="Аниме-фильмы", callback_data="anime_films"),
InlineKeyboardButton(text="Аниме-сериалы", callback_data="anime_serials"))
category.add(InlineKeyboardButton(text="Мультфильмы", callback_data="cartoon"),
InlineKeyboardButton(text="Мультсериалы", callback_data="cartoon_serials"))
category.add(InlineKeyboardButton(text="ТВ-Шоу", callback_data="tv"))
category.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

contacts = InlineKeyboardMarkup()
contacts.add(InlineKeyboardButton(text="✈️ Наш форум", url="https://na-sha.ru/"),
InlineKeyboardButton(text="📝 Наш группа", url="https://t.me/nasharu1"))
contacts.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

about = InlineKeyboardMarkup()
# about.add(InlineKeyboardButton(text="🖊️ Вопросы / Ответы", callback_data="faq"))
about.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))


Admin = InlineKeyboardMarkup(
inline_keyboard = [

    [
        InlineKeyboardButton(text="Добавление\n фильма", callback_data="add_film"),
        InlineKeyboardButton(text="Добавление сериала", callback_data="add_series"),
    ],
    [

        InlineKeyboardButton(text="Добавление админа", callback_data="add_admin"),
        InlineKeyboardButton(text="Добавление канала", callback_data="add_chanel"),
    ],
    [ InlineKeyboardButton(text="Просмотр имеющиеся фильмов", callback_data="get_film"),
      InlineKeyboardButton(text="Просмотр имеющиеся сериалов", callback_data="get_series"),

      ],
    [
      InlineKeyboardButton(text="Просмотр имеющиеся админов", callback_data="get_admin"),
      InlineKeyboardButton(text="Просмотр имеющиеся каналов", callback_data="get_chanel"),
    ],
      [InlineKeyboardButton(text="Удаление фильма", callback_data="del_film"),
       InlineKeyboardButton(text="Удаление сериала", callback_data="del_series"),

],
    [
        InlineKeyboardButton(text="Удаление админа", callback_data="del_admin"),
        InlineKeyboardButton(text="Удаление канала", callback_data="del_chanel"),
    ],

      [InlineKeyboardButton(text="◀️ Назад", callback_data="back"),]

]
)

AdminError = InlineKeyboardMarkup()
AdminError.add(InlineKeyboardButton(text="🏠 Меню", callback_data="back"))
film_back = InlineKeyboardMarkup()
film_back.add(InlineKeyboardButton(text="Повторить попытку", callback_data="add_film"))
series_back = InlineKeyboardMarkup()
series_back.add(InlineKeyboardButton(text="Повторить попытку", callback_data="add_series"))
chanel_back = InlineKeyboardMarkup()
chanel_back.add(InlineKeyboardButton(text="Повторить попытку", callback_data="add_chanel"))
chanel_back1 = InlineKeyboardMarkup()
chanel_back1.add(InlineKeyboardButton(text="Повторить попытку", callback_data="del_chanel"))
film_back1 = InlineKeyboardMarkup()
film_back1.add(InlineKeyboardButton(text="Повторить попытку", callback_data="del_film"))
series_back1 = InlineKeyboardMarkup()
series_back1.add(InlineKeyboardButton(text="Повторить попытку", callback_data="del_series"))
admin_back1 = InlineKeyboardMarkup()
admin_back1.add(InlineKeyboardButton(text="Повторить попытку", callback_data="del_admin"))
Admin_back = InlineKeyboardMarkup()
Admin_back.add(InlineKeyboardButton(text="Повторить попытку", callback_data="add_admin"))
Admin_back1 = InlineKeyboardMarkup()
Admin_back1.add(InlineKeyboardButton(text="Отмена", callback_data="back"))


search_back = InlineKeyboardMarkup()
search_back.add(InlineKeyboardButton(text="◀️ Назад", callback_data="poisk"))
search = InlineKeyboardMarkup()
search.add(InlineKeyboardButton(text="Поиск сериала", callback_data="search_series"))
search.add(InlineKeyboardButton(text="Поиск фильма", callback_data="search_films"))
search.add(InlineKeyboardButton(text="◀️ Назад", callback_data="back"))

go_poisk = InlineKeyboardMarkup()
# about.add(InlineKeyboardButton(text="🖊️ Вопросы / Ответы", callback_data="faq"))
go_poisk.add(InlineKeyboardButton(text="◀️ Назад", callback_data="poisk"))


def get_chanels():
    checkSubMenu = InlineKeyboardMarkup(row_width=1)
    CHANELS = db.get_chanels()
    for chanel in CHANELS:
        btn = InlineKeyboardButton(text=chanel[0], url=chanel[2])
        checkSubMenu.insert(btn)
    btn = InlineKeyboardButton(text="Я подписался!",callback_data="subchanneldone")
    checkSubMenu.insert(btn)
    return checkSubMenu


