from datetime import date

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from AIP_English import *
from Key_English import API_TOKEN
from AIP_Ukraine import *

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class Questions(StatesGroup):
    # АНГЛ БОТ
    q1 = State()
    q2 = State()
    q3 = State()
    # ВТРАТИ БОТ
    q4 = State()
    q5 = State()

kbd_UAEND = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ввести нову дату/Typed a new date', callback_data='NoUA')],
    [InlineKeyboardButton(text='Повернутися в головне меню/Back to the main menu', callback_data='Backemainror')]
])

kbd_UAEND2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отримати дані за другий день війни "2022-02-25"/Get data for the second day of the war "2022-02-25"', callback_data='Get_Sek_data')],
    [InlineKeyboardButton(text='Ввести нову дату/Typed a new date', callback_data='NoUA')],
    [InlineKeyboardButton(text='Повернутися в головне меню/Back to the main menu', callback_data='Backemainror')]
])

kbd_UA11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text= 'Шукати дані/Search for data', callback_data='SerchUA')],
    [InlineKeyboardButton(text='Ввести нову дату/Typed a new date', callback_data='NoUA')]
])

kbd_ENGEROR = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ввести нове слово/Typed a new word', callback_data='Noeror')],
    [InlineKeyboardButton(text = 'Повернутися в головне меню/Back to the main menu', callback_data='Backemainror')]
])

kbd_ENG1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Так, шукати/Yes, search', callback_data='Yeseror')],
    [InlineKeyboardButton(text='Ні, введіть нове слово/No, typed a new word', callback_data='Noeror')]
])
kbd_ENG123 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Повернутися в головне меню/Back to the main menu', callback_data='Backemainror')]
])

kbd_ENG2 = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(text='Сайт з синонімами/антонімами', url="https://api-ninjas.com/api/thesaurus"),
    InlineKeyboardButton(text='Сайт з втратами росіян', url="https://russianwarship.rip/")
    ],
    [InlineKeyboardButton(text = 'Повернутися в головне меню/Back to the main menu', callback_data='Backemainror')]
])

kbd_ENG222 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Антоніми/Antonyms', callback_data='Antonymseror')],
    [InlineKeyboardButton(text = 'Введіть нове слово/Typed a new word', callback_data='Noeror')],
    [InlineKeyboardButton(text = 'Повернутися в головне меню/Back to the main menu', callback_data='Backemainror')]
])

kbd_ENG223 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Синоніми/Synonyms', callback_data = 'Synonymseror')],
    [InlineKeyboardButton(text = 'Введіть нове слово/Typed a new word', callback_data='Noeror')],
    [InlineKeyboardButton(text = 'Повернутися в головне меню/Back to the main menu', callback_data='Backemainror')]
])

kbd_ENG3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Синоніми/Synonyms', callback_data = 'Synonymseror')],
    [InlineKeyboardButton(text='Антоніми/Antonyms', callback_data='Antonymseror')]
])

kbd_UA1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Отримати дані за сьогодні/Get data for today', callback_data='GetDataNow')],
    [InlineKeyboardButton(text = 'Повернутися в головне меню/Back to the main menu', callback_data='Backemainror')]
])


kbd_reply = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True, keyboard=[
    [KeyboardButton(text="Start/Restart"),], [KeyboardButton(text="Help"),]
])

kbd_message = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пошук синонимів та антонімів/Search for synonyms and antonyms', callback_data='English')],
    [InlineKeyboardButton(text='Пошук втрат росіян/Search for Russian losses', callback_data='Ukraine')],
    [InlineKeyboardButton(text="Зупинити бота/Stop bot", callback_data='erorstop')]
])

async def set_all_default_commands(bot: Bot):
    await set_all_default_comand(bot)

@dp.callback_query_handler(Text(startswith="Backemainror"), state="*")
@dp.message_handler(Command(['start', 'restart']), state="*")
@dp.message_handler(Text("Start/Restart"), state="*")
async def start_restart(obj: types.Message | types.CallbackQuery, state: FSMContext):
    await set_all_default_comand(bot)
    await state.finish()
    if isinstance(obj, types.Message):
        message = obj
    else:
        await obj.answer()
        message = obj.message
    await message.answer(text='''
    (мова: 🇺🇦)
    Бот запущено/перезапущено. Цей бот має два режими. 
    Перший - це пошук синонимів та антонимів для англійских слів. 
    Другий - це пошук статисти втрат росіян по даті типу "2023-05-02"
    Більше інформації /help.
    Слава Україні! Героям слава!
    \n(language: 🇬🇧)
    The bot is running/restarted. This bot has two modes. 
    The first is to search for synonyms and antonyms for English words. 
    The second is to search for statistics on Russian casualties by date such as "2023-03-02".
    More information /help.
    Glory to Ukraine! Glory to the heroes!
    ''', reply_markup=kbd_message)

@dp.callback_query_handler(Text(startswith="English"), state="*")
@dp.callback_query_handler(Text(startswith="Noeror"), state="*")
async def process_button(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.finish()
    await callback.message.answer(text='Введіть слово.\nПриклад: \"car\" (мова: 🇬🇧)\n'
                                       'Enter a word.\nExample: \"car\" (language: 🇬🇧)', reply_markup=kbd_ENG123)
    await Questions.q1.set()

@dp.callback_query_handler(Text(startswith="NoUA"), state="*")
@dp.callback_query_handler(Text(startswith="Ukraine"), state="*")
async def process_button(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(text='(мова: 🇺🇦)\nВведіть число за яке ви хочете отримати дані.\nПриклад: \"РІК-МІСЯЦЬ-ДЕНЬ\"=>\"2023-05-02\"\n'
                                       '(language: 🇬🇧)\nEnter the date for which you want to get the data.\nExample: \"Year-Month-Day\" => \"2023-05-02\"', reply_markup=kbd_UA1)
    await Questions.q4.set()

@dp.message_handler(state=Questions.q1)
async def Engl_API(message: types.Message, state: FSMContext):
    await message.answer(text = f"Ви ввели слово \"{message.text}\", шукати? (мова: 🇬🇧)\n"
                                f"Did you type in the word \"{message.text}\", search? (language: 🇬🇧)", reply_markup = kbd_ENG1)
    await state.update_data({'search':message.text})
    await Questions.q2.set()

@dp.message_handler(state=Questions.q2)
@dp.callback_query_handler(Text(startswith="Yeseror"), state="*")
async def Search(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    wg = data.get('search')
    syn = get_sin(wg)
    ant = get_ant(wg)
    if syn == [] and ant == []:
        await callback.message.answer(f"Ви вибрали кнопку:\"Так, шукати/Yes, search\", результат:\nПОМИЛКА! Бот не знайшов слів як синонімів/антонімів до слова \'{wg}\' (мова: 🇬🇧)\n"
                                      f"You have selected the \"Так, шукати/Yes, search\" button, the result:\nERROR! Bot did not get any words as synonyms/antonyms for the word \'{wg}\' (language: 🇬🇧)", reply_markup=kbd_ENGEROR)
    else:
        await callback.message.answer("Ви вибрали кнопку:\"Так, шукати/Yes, search\", результат:\nБот отримав дані! (мова: 🇬🇧)\n"
                                      "You have selected the \"Так, шукати/Yes, search\" button, the result: The bot has received the data! (language: 🇬🇧)")
        await callback.message.answer("Що будемо виводити? (мова: 🇬🇧)\n"
                                      "What are we going to withdraw? (language: 🇬🇧)", reply_markup=kbd_ENG3)
    await Questions.q3.set()

@dp.message_handler(state=Questions.q3)
@dp.callback_query_handler(Text(startswith="Synonymseror"), state="*")
async def syn_g(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    wg = data.get('search')
    syn = get_sin(wg)
    me = "Синоніми|Synonyms: "
    if syn == []:
        me += "---"
    else:
        me += ", ".join(syn) + "."
    await callback.message.answer(me, reply_markup=kbd_ENG222)

@dp.message_handler(state=Questions.q3)
@dp.callback_query_handler(Text(startswith="Antonymseror"), state="*")
async def ant_g(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    data = await state.get_data()
    wg = data.get('search')
    ant = get_ant(wg)
    me = "Антоніми|Antonyms: "
    if ant == []:
        me += "---"
    else:
        me += ", ".join(ant) + "."
    await callback.message.answer(me, reply_markup=kbd_ENG223)

@dp.message_handler(Command(['help']), state="*")
@dp.message_handler(Text("Help"), state="*")
async def help(message: types.Message):
    await message.answer(text = '(мова: 🇺🇦)\nВи вибрали кнопку \"Help або /help\"\nЩо б запустити бота введіть /start або /restart\nЗа для того аби подивится мої подяки введи /board або /gratitude_board\nБот створений як фінальний проект до першого блоку навчаняя в GoIteens.\nВласник бота: Моргун Михайло\n'
                                '\n(language: 🇬🇧)\nYou have selected the \"Help or /help\" button\nTo start the bot, enter /start or /restart\nTo see my gratitude, enter /board or /gratitude_board\nThe bot was created as a final project for the first block of training in GoIteens: Mikhail Morgun', reply_markup=kbd_ENG2)

@dp.message_handler(Command(['board', 'gratitude_board']), state="*")
@dp.message_handler(Text('gratitude_board'), state="*")
async def gratitude_board(message: types.Message):
    await message.answer(text = '(мова: 🇺🇦)\nВи написали \"gratitude_board або /board\"\nЯ дякую своєму вчителям\nз Tech Skills Михайлові Денисову та\nз Soft Skills Валдаєвій Анні,\nменеджеру нашої групи Поліні Білоус\nТа всім одноклассникам:\nОлександру Димовy,\nМаксимy Хомінy,\nОлександру Навроцкому,\nДарию Соколову,\nМаркy Вую,\nІллі Грабазію,\nЕвгенію Демченко,\nОлександрy Кривешко та Владимиру Ніколаєву\nІ всім моїм родичам\nДякую! :)'
                                '\n---\n(language: 🇬🇧)\nYou wrote "gratitude_board or /board\"\nI am grateful to my teachers\nfrom Tech Skills Mykhailo Denysov\nand from Soft Skills Anna Valdaieva,\nour group manager Polina Bilous,\nand all my classmates:\nOleksandr Dymov,\nMaksym Khomin,\nOleksandr Navrotskyi,\nDarii Sokolov,\nMark Vuy,\nIlya Grabazii,\nEvgenii Demchenko,\nOleksandra Kryveshko and Volodymyr Nikolaiev\nAnd to all my relatives\nThank you! :)', reply_markup = kbd_ENG123)


@dp.message_handler(state=Questions.q4)
async def vidpovid(message: types.Message, state: FSMContext):
    await message.answer(text = f'(мова: 🇺🇦)\nВи ввели дату \"{message.text}\", шукати дані про цей день?\n'
                                f'(language: 🇬🇧)\nDid you enter the date \"{message.text}\", do you want to search for data about this day?', reply_markup = kbd_UA11)
    await state.update_data({'search': message.text})
    await Questions.q5.set()

@dp.message_handler(state=Questions.q5)
@dp.callback_query_handler(Text(startswith="SerchUA"), state="*")
async def poshuk(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer_sticker(sticker="CAACAgIAAxkBAAEI1eZkUisf7-DyN1I8kzCugk10vASexwACExgAAoLaKEnuYxoB8MfEBC8E")

    data = await state.get_data()
    wg = data.get('search')
    await callback.message.answer(text = f"(мова: 🇺🇦)\nВи ввели дату \"{wg}\"\n"
                                         f"(language: 🇬🇧)\nYou entered the date \"{wg}\"\n")
    if verify_date(wg) == True:
            await callback.message.answer(text=f"(мова: 🇺🇦)\nБот отримав дані. Пошук здійснено за числом \"{wg}\"\n" 
                                               f"(language: 🇬🇧)The bot has received the data. The search was performed by the number \"{wg}\"")
            if wg == "2022-02-24":
                await callback.message.answer(
                    text="(мова: 🇺🇦)\nВибачте, але перший день війни \"2022-02-24\", на жаль, не документувався 😢. Спробуйте іншу дату. Дата \"2022-02-24\" є у базі."
                         "\n(language: 🇬🇧)\nSorry, but unfortunately the first day of the war \"2022-02-24\" was not documented 😢. Try another date. The date \"2022-02-24\" is in the database.\n",
                    reply_markup=kbd_ENG123)
                await state.finish()
            else:
                date_from_message = get_stats(wg)
                await callback.message.answer(date_from_message,reply_markup = kbd_UAEND)
    elif verify_date(wg) == False:
        await callback.message.answer(text = f'(мова: 🇺🇦)\nПомилка! Такої дати: \"{wg}\" не існує у базі. Спробуйте ще раз і напишіть по образцу: \"РІК-МІСЯЦЬ-ДЕНЬ\"=>\"2023-05-02\"\nІ майте на увазі що дати в базі з початку повномаштабного вторгння "2022-02-24" до сьогоденяя поки Україна не переможе 💛💙\n'
                                             f'(language: 🇬🇧)\nError. The date: \"{wg}\" does not exist in the database. Try again and write it like this: \"YEAR-MONTH-DAY\"=>\"2023-05-02\"\nBut keep in mind that the dates in the database are from the beginning of the full-scale invasion "2022-02-24" to the present day until Ukraine wins 💛💙', reply_markup= kbd_UAEND)
        await state.finish()

@dp.callback_query_handler(Text(startswith="GetDataNow"), state="*")
async def get_now_date(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer_sticker(sticker="CAACAgIAAxkBAAEI1eZkUisf7-DyN1I8kzCugk10vASexwACExgAAoLaKEnuYxoB8MfEBC8E")
    wg = date.today()
    date_from_message = get_stats(wg)
    await callback.message.answer(text=f"(мова: 🇺🇦)\nБот отримав дані. Пошук здійснено за числом \"{wg}\" - сьогодні.\n"
                                       f"(language: 🇬🇧)The bot has received the data. The search was performed by the number \"{wg}\" - today.")
    await callback.message.answer(date_from_message, reply_markup=kbd_UAEND)
    await state.finish()

@dp.callback_query_handler(Text(startswith="Get_Sek_data"), state="*")
async def get_sec_date(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer_sticker(sticker="CAACAgIAAxkBAAEI1eZkUisf7-DyN1I8kzCugk10vASexwACExgAAoLaKEnuYxoB8MfEBC8E")
    wg = "2022-02-25"
    date_from_message = get_stats(wg)
    await callback.message.answer(text=f"(мова: 🇺🇦)\nБот отримав дані. Пошук здійснено за числом \"{wg}\" - сьогодні.\n"
                                       f"(language: 🇬🇧)The bot has received the data. The search was performed by the number \"{wg}\" - today.")
    await callback.message.answer(date_from_message, reply_markup=kbd_UAEND)
    await state.finish()

@dp.callback_query_handler(Text(startswith="erorstop"), state="*")
async def stop_key(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='''
    (мова: 🇺🇦)
    Бот зупинено. Для запуску бота нажміть /start. Цей бот має два режими. 
    Перший - це пошук синонимів та антонимів для англійских слів. 
    Другий - це пошук статисти втрат росіян по даті типу "2023-05-02"
    Більше інформації /help.
    Слава Україні! Героям слава!
    \n(language: 🇬🇧)
    The bot is stopped. To start the bot, press /start. This bot has two modes. 
    The first is to search for synonyms and antonyms for English words. 
    The second is to search for statistics on Russian casualties by date such as "2023-03-02".
    More information /help.
    Glory to Ukraine! Glory to the heroes!
    ''')

@dp.message_handler()
async def eho(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)