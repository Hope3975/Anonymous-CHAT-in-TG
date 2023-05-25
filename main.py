from aiogram import executor 
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.markdown import hbold
from collections import defaultdict
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.callback_data import CallbackData


import random
import string
import json
import os
import re
import logging


from aiogram.types import KeyboardButton
from tok import API_TOKEN, ALLOWED_USER_ID # Импорт ТОкена
from db import * # Импорт всех функций из db.py
# create_db() # вызов создания db если его нет


def save_message_to_json(nickname, message): # Приколы для деда
    file_name = "messages.json"
    
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append({"nickname": nickname, "message": message})

    with open(file_name, "w") as file:
        json.dump(data, file)


storage = MemoryStorage()
bot = Bot(token=API_TOKEN) # Активация бота
dp = Dispatcher(bot, storage = storage) # Хуня для того чтобы получать текст от пользователя
dp.middleware.setup(LoggingMiddleware())

logging.basicConfig(level=logging.INFO)

# Функция создания рандомного ник
def generate_random_nick(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


import random

vowels = ['Kobayashi', 'Yamamoto', 'Takahashi', 'Watanabe', 'Nakamura', 'Mori', 'Yoshida', 'Inoue', 'Yamada', 'Sasaki', 'Nakajima', 'Kato', 'Okada', 'Ishii', 'Fujita', 'Ito', 'Hayashi', 'Sakai', 'Ono', 'Omura', 'Matsuda', 'Miyazaki', 'Nishimura', 'Fukuda', 'Takeuchi', 'Ueda', 'Nagai', 'Ogawa', 'Hara', 'Kojima', 'Nakano', 'Uchida', 'Nakayama', 'Kaneko', 'Tamura', 'Takada', 'Hoshino', 'Imai', 'Kubota', 'Okamoto', 'Sugiyama', 'Yokoyama', 'Arai', 'Taniguchi', 'Kondo', 'Saito', 'Kawaguchi', 'Nakagawa', 'Ishikawa', 'Fujimoto', 'Hashimoto', 'Maeda', 'Matsui', 'Shimizu', 'Miyamoto', 'Miyashita', 'Sugawara', 'Ando', 'Sato', 'Murata', 'Mizuno', 'Kawai', 'Yamashita', 'Noguchi', 'Matsuo', 'Ozawa', 'Kikuchi', 'Oshima', 'Kawasaki', 'Yamaguchi', 'Hirano', 'Fujii', 'Ishida', 'Endo', 'Ogata', 'Kumagai', 'Aoki', 'Hasegawa', 'Sakamoto', 'Eguchi', 'Kodama', 'Morioka', 'Takizawa', 'Sugimoto', 'Yasuda', 'Takahara', 'Goto', 'Shibata', 'Tsuda', 'Takeda', 'Kimura', 'Tsuchiya', 'Yamagishi', 'Izumi', 'Kawano', 'Otsuka', 'Takano', 'Oyama', 'Yamazaki', 'Wada', 'Noda', 'Sakata', 'Sakurai', 'Suzuki', 'Yoshikawa', 'Inoue', 'Tsukamoto', 'Muto', 'Nishida', 'Mochizuki', 'Kawabata', 'Yokota', 'Asano', 'Igarashi', 'Koga', 'Fukushima', 'Higuchi', 'Maruyama', 'Iida', 'Kawakami', 'Nishiyama', 'Kobayashi', 'Kasai', 'Kawamura', 'Terada', 'Niwa', 'Kanai', 'Yoshimura', 'Furukawa', 'Takagi', 'Hori', 'Inaba', 'Kawashima', 'Kameda', 'Ishikawa', 'Hino', 'Shimada', 'Yagi', 'Nakata', 'Sakaguchi', 'Sone', 'Matsunaga', 'Kawamoto', 'Kinoshita', 'Nakazawa', 'Ota', 'Ueno', 'Shirai', 'Sekiguchi', 'Ishihara', 'Kasahara', 'Kurihara', 'Toyoda', 'Kobayashi', 'Nakano', 'Anzai', 'Nagashima', 'Kikuchi', 'Tsuchida', 'Shimoda', 'Yokouchi', 'Yamane', 'Minami', 'Nomura', 'Kawada', 'Shimazaki', 'Nakasone', 'Abe', 'Kusano', 'Kosugi', 'Kanazawa', 'Horiuchi', 'Tanabe', 'Sugihara', 'Taguchi', 'Amano', 'Kajiwara', 'Kawagoe', 'Takei', 'Miyake', 'Ohashi', 'Kudo', 'Tomita', 'Tanimoto', 'Kawase', 'Takaya', 'Oka', 'Asai', 'Kashiwagi', 'Takahata', 'Nakai', 'Terao', 'Kaneko', 'Shoji', 'Takimoto', 'Ouchi', 'Matsubara', 'Hasegawa', 'Shindo', 'Yamabe', 'Hamada', 'Kumamoto', 'Iwata', 'Koyama', 'Oishi', 'Kurita', 'Yamagata', 'Sakuma', 'Sugita', 'Uchiyama', 'Kitagawa', 'Miyazawa', 'Yamamoto', 'Matsuyama', 'Furuta', 'Sekine', 'Tsutsui', 'Sakoda', 'Kataoka', 'Sakurada', 'Ishiguro', 'Nishikawa', 'Ozaki', 'Sato', 'Matsushita', 'Yamada', 'Kanada', 'Ishimoto', 'Kojima', 'Takeuchi', 'Nishimura', 'Muraoka', 'Inagaki', 'Saito', 'Sakai', 'Suzuki', 'Kawano', 'Ogino', 'Mizutani', 'Kamikawa', 'Mizoguchi', 'Kondo', 'Tsukada', 'Takemoto', 'Takayama', 'Akita', 'Nakagawa', 'Nakamura', 'Okazaki', 'Yoshida', 'Tachibana', 'Kanai', 'Miyoshi', 'Ishikura', 'Okada', 'Yamazaki', 'Araki', 'Shibuya', 'Shimomura', 'Nakano', 'Kikuchi', 'Yoshino', 'Hayakawa', 'Wakabayashi', 'Takeuchi', 'Sakamoto', 'Ogawa', 'Ishii', 'Nakata', 'Shimizu', 'Yoshida', 'Aoyama', 'Nakayama', 'Kojima', 'Fukuda', 'Takahashi', 'Inoue', 'Yamaguchi', 'Matsuda', 'Miyazaki', 'Nishimura', 'Nakamura', 'Yoshida', 'Mori', 'Ishikawa', 'Kato', 'Yamada', 'Sasaki', 'Nakajima', 'Saito', 'Sakai', 'Suzuki', 'Kawano', 'Ogino', 'Mizutani', 'Kamikawa']
adjectives = ['Akira', 'Akihiro', 'Daichi', 'Daisuke', 'Eiji', 'Fumio', 'Goro', 'Haruki', 'Hiroshi', 'Hiroto', 'Hisao', 'Hitoshi', 'Ichiro', 'Isamu', 'Jun', 'Junichi', 'Jiro', 'Kaito', 'Kazuki', 'Kazuo', 'Kazuya', 'Kei', 'Keiji', 'Keisuke', 'Ken', 'Kenichi', 'Kenta', 'Kiyoshi', 'Koichi', 'Koji', 'Kosuke', 'Makoto', 'Manabu', 'Masahiro', 'Masaki', 'Masao', 'Masaru', 'Masashi', 'Masato', 'Masayuki', 'Mitsuru', 'Miyuki', 'Nao', 'Naoki', 'Naoto', 'Noboru', 'Nobuhiro', 'Nobuo', 'Nobuyuki', 'Norio', 'Osamu', 'Rei', 'Riku', 'Ryo', 'Ryota', 'Ryu', 'Ryosuke', 'Satoshi', 'Seiji', 'Shin', 'Shinichi', 'Shinji', 'Shintaro', 'Shinya', 'Shiro', 'Shota', 'Shuichi', 'Shun', 'Shunsuke', 'Susumu', 'Tadashi', 'Takahiro', 'Takao', 'Takashi', 'Takayuki', 'Takeo', 'Takeshi', 'Tatsuya', 'Tetsuya', 'Tooru', 'Toshiaki', 'Toshio', 'Tsutomu', 'Yasushi', 'Yasutaka', 'Yoichi', 'Yoji', 'Yoshiaki', 'Yoshio', 'Yoshito', 'Yosuke', 'Yuichi', 'Yuki', 'Yukio', 'Yusuke', 'Yutaka', 'Ai', 'Aiko', 'Airi', 'Akane', 'Akemi', 'Aki', 'Akiko', 'Asuka', 'Ayaka', 'Ayame', 'Aya', 'Ayumi', 'Azumi', 'Chie', 'Chieko', 'Chiharu', 'Chihiro', 'Chika', 'Chinatsu', 'Eiko', 'Emi', 'Emiko', 'Eri', 'Erika', 'Erina', 'Fumiko', 'Hana', 'Haru', 'Haruka', 'Harumi', 'Hatsue', 'Hikari', 'Hikaru', 'Hina', 'Hiroko', 'Hiromi', 'Hisako', 'Hitomi', 'Honoka', 'Izumi', 'Junko', 'Kana', 'Kanako', 'Kaori', 'Kasumi', 'Kazuko', 'Kazumi', 'Keiko', 'Kiko', 'Kiyoko', 'Kumiko', 'Kyouko', 'Mai', 'Makiko', 'Mami', 'Manami', 'Mari', 'Mariko', 'Masako', 'Maya', 'Mayu', 'Mayumi', 'Megumi', 'Michiko', 'Mieko', 'Miho', 'Mika', 'Miki', 'Mikiko', 'Minako', 'Mio', 'Nana', 'Nanami', 'Nao', 'Naoko', 'Natsuki', 'Natsumi', 'Nobuko', 'Noriko', 'Nozomi', 'Rei', 'Reiko', 'Rena', 'Rie', 'Rika', 'Riko', 'Rina', 'Risa', 'Rumi', 'Ryoko', 'Saeko', 'Saki', 'Sakura', 'Sana', 'Sanae', 'Satomi', 'Sayaka', 'Sayuri', 'Seiko', 'Shiho', 'Shiori', 'Shizuka', 'Shizuko', 'Sora', 'Sumiko', 'Takako', 'Tamiko', 'Tomiko', 'Tomoko', 'Tomomi', 'Tsubasa', 'Tsukiko', 'Umeko', 'Yayoi', 'Yoko', 'Yoshiko', 'Yui', 'Yuina', 'Yuka', 'Yuki', 'Yukiko', 'Yuko', 'Yumi', 'Yumiko', 'Yuriko', 'Yuuka', 'Yuuki', 'Yuzuki', 'Issey', 'Itsuki', 'Izumi', 'Jin', 'Junya', 'Kaede', 'Kai', 'Kaito', 'Kanata', 'Kazuhiko', 'Kazuma', 'Keigo', 'Keita', 'Kenji', 'Kenshin', 'Kenta', 'Kiyohiko', 'Kohei', 'Kohaku', 'Kotaro', 'Kou', 'Kunio', 'Kyohei', 'Kyosuke', 'Mamoru', 'Manato', 'Masaaki', 'Masanori', 'Masayoshi', 'Michihiro', 'Minori', 'Mitsuhiro', 'Mizuki', 'Natsuo', 'Nobuhiko', 'Norihito', 'Raito', 'Riku', 'Rin', 'Ryoichi', 'Ryota', 'Ryugo', 'Ryuuji', 'Seiichi', 'Seiya', 'Shigeki', 'Shinjiro', 'Sho', 'Shohei', 'Shota', 'Shunichi', 'Shunji', 'Taiga', 'Taiki', 'Taisei', 'Takuma', 'Tatsuki', 'Tetsuji', 'Tomoaki', 'Tomohiro', 'Toshinori', 'Tsuyoshi', 'Yasuhiro', 'Yasunori', 'Yoshinori', 'Yosuke', 'Yuji', 'Yukihiro', 'Yusaku', 'Yuto', 'Yuya', 'Zen']
emojis = ["😀", "😁", "😂", "😃", "😄", "😅", "😆", "😇", "😉", "😊", "😋", "😌", "😍", "😎", "😏", "😐", "😑", "😒", "😓", "😔", "😕", "😖", "😗", "😘", "😙", "😚", "😛", "😜", "😝", "😞", "😟", "😠", "😡", "😢", "😣", "😤", "😥", "😦", "😧", "😨", "😩", "😪", "😫", "😬", "😭", "😮", "😯", "😰", "😱", "😲", "😳", "😴", "😵", "😶", "😷", "😸", "😹", "😺", "😻", "😼", "😽", "😾", "😿", "🙀", "🙁", "🙂", "🙃", "🙄", "🙅", "🙆", "🙇", "🙈", "🙉", "🙊", "🙋", "🙌", "🙍", "🙎", "🙏"]

def generate_word():
    first_name = random.choice(vowels)
    last_name = random.choice(adjectives)
    emoji = random.choice(emojis)
    return f"[{emoji}] {first_name} {last_name}"

# def check_permissions_and_add_subscription(user_id: int):
#     with sqlite3.connect("users.db") as db:
#         cursor = db.cursor()
        
#         # Проверка подписки
#         cursor.execute("SELECT subscription FROM users WHERE id = ?", (user_id,))
#         user_data = cursor.fetchone()
#         if not user_data or user_data[0] == 0:
#             cursor.execute("UPDATE users SET subscription=1 WHERE id=?", (user_id,))

#         # Проверка админки
#         cursor.execute("SELECT is_admin FROM users WHERE id = ?", (user_id,))
#         user_data = cursor.fetchone()
#         if not user_data or user_data[0] == 0:
#             cursor.execute("UPDATE users SET is_admin = 1 WHERE id = ?", (user_id,))
        
#         db.commit()


@dp.message_handler(commands=['start']) # Обработчик сообщений
async def cmd_start(message: types.Message):
    user_id = message.from_user.id  # Получение id
    # check_permissions_and_add_subscription(user_id)
    ban_status = get_ban_status(user_id)
    print(f">>>>>>>>>>BAN>>>>>>: {ban_status}")
    if ban_status == 1:
        await message.reply("Ваш аккаунт заблокирован.")
        return
    name = generate_word() # Генерация имени
    user_id = message.from_user.id # Получение id
    user_first_name = message.from_user.first_name # Получение имени человека котоырй написал
    print (f"Commands >> /start\nID >> {get_id(user_id)}\nNAME >> {get_nick(user_id)}\nSUB_STATUS >> {get_subscription(user_id)}\n\n") # Логирование
    add_user_to_db(user_id, user_first_name, name) # вызов функции и передаче ей id и имя
    subscription_status = get_subscription(user_id)
    subscription_type = "Бесплатный" if subscription_status == 0 else "Платный"
    welcome_text = f"<b>🤚Привет, {user_first_name}!\n\n👤Твой ник в анонимном чате: \n    [{get_nickName(user_id)}]\n\nСтутусПодписки: \n    🤩 {subscription_type}\n\n👽Этот бот позволит тебе анонимно общаться с людьми.\n ❓Есть вопросы? Жми /help</b>" # текст сообщения на вывод
    sticker_id = "CAACAgIAAxkBAAICumQ8O1zpaRc7q9G5_xY9OWnmEzSlAAJJAgACVp29CiqXDJ0IUyEOLwQ"  # Идентификатор стикера (file_id)
    await bot.send_sticker(chat_id=message.chat.id, sticker=sticker_id)  # Отправка стикера
    markup = create_keyboard(user_id)
    await message.reply(welcome_text, parse_mode=ParseMode.HTML, reply_markup=markup) # вывод сообщения

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class ReportState(StatesGroup):
    user_nick = State()
    report_reason = State()

# Обработчик команды /report
@dp.message_handler(Command("report"), state=None)
async def report_command(message: types.Message):
    await message.reply("Введите ник пользователя, на которого хотите пожаловаться:")

    # Устанавливаем состояние
    await ReportState.user_nick.set()

@dp.message_handler(state=ReportState.user_nick)
async def process_user_nick(message: types.Message, state: FSMContext):
    # Получаем данные состояния
    user_nick = message.text

    # Сохраняем данные состояния
    await state.update_data(user_nick=user_nick)

    # Следующее состояние
    await ReportState.next()
    await message.reply("Введите причину жалобы:")

@dp.message_handler(state=ReportState.report_reason)
async def process_report_reason(message: types.Message, state: FSMContext):
    # Получаем данные состояния
    state_data = await state.get_data()
    user_nick = state_data["user_nick"]
    report_reason = message.text

    # Формируем текст сообщения
    report_text = f"Жалоба на пользователя:\n {user_nick}\nПричина: {report_reason}"

    # Отправляем сообщение администраторам
    admins_data = get_admins()
    for admin_id, username, nick in admins_data:
        try:
            await bot.send_message(chat_id=admin_id, text=report_text)
        except Exception as e:
            logging.error(f"Failed to send report to admin {admin_id}: {e}")

    # Отправляем пользователю сообщение об успешной отправке жалобы
    await message.reply("Жалоба успешно отправлена администраторам!")

    # Сбрасываем состояние
    await state.finish()

class UserState(StatesGroup):
    admin_nick = State()
    message_text = State()
    reply_to_user = State()

class AdminState(StatesGroup):
    ban = State()
    unban = State()

# Define callback data
reply_cb = CallbackData("reply", "user_id")



@dp.message_handler(lambda message: message.text == "📨 Написать админу", state=None)
async def write_to_admin_button(message: types.Message):
    await list_admins_command(message)


admin_id_to_nick_map = {}

# Define new callback data
write_cb = CallbackData("write", "admin_id")

@dp.message_handler(Command("lsadmin"), state=None)
async def list_admins_command(message: types.Message):
    admins_data = get_admins()

    # Создайте клавиатуру с кнопками для каждого админа
    markup = InlineKeyboardMarkup()
    for admin_id, username, nick in admins_data:
        # Save admin_id to admin_nick mapping
        admin_id_to_nick_map[admin_id] = nick

        markup.add(InlineKeyboardButton(f"{nick}", callback_data=write_cb.new(admin_id=admin_id)))

    await message.reply("Для покупки подписки писать: \n𝗕𝘆𝘁𝗲𝗕𝘂𝘀𝘁𝗲𝗿'𝘀 𝐈𝐓 👑OWNER👑\n\nНажмите что бы скопировать.\n\nАдминистраторы:\n\n", reply_markup=markup)

    # Установите состояние
    await UserState.admin_nick.set()

# New callback query handler
@dp.callback_query_handler(write_cb.filter(), state=UserState.admin_nick)
async def process_write_button(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    admin_id = int(callback_data["admin_id"])
    admin_nick = admin_id_to_nick_map.get(admin_id)

    # Save state data
    await state.update_data(admin_id=admin_id, admin_nick=admin_nick)

    # Next state
    await UserState.next()
    await call.answer()
    await call.message.reply("Введите текст сообщения для админа:")

@dp.message_handler(state=UserState.message_text)
async def process_message_text(message: types.Message, state: FSMContext):
    # Get state data
    data = await state.get_data()
    admin_nick = data.get("admin_nick")
    message_text = message.text

    if admin_id := get_admin_id_by_nick(admin_nick):
        sender_name = message.from_user.first_name
        sender_id = message.from_user.id

        # Отправить сообщение админу
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Ответить", callback_data=reply_cb.new(user_id=sender_id)))
        await bot.send_message(admin_id, f"Сообщение от {sender_name} (ID: {sender_id}):\n\n{message_text}", reply_markup=markup)
        await message.reply("Ваше сообщение отправлено админу.")
    else:
        await message.reply("Админ с таким ником не найден.")

    # Finish state
    await state.finish()

@dp.message_handler(state=UserState.reply_to_user)
async def process_reply_to_user(message: types.Message, state: FSMContext):
    # Get state data
    data = await state.get_data()
    recipient_id = data.get("reply_to_user_id")
    message_text = message.text

    # Отправить ответное сообщение пользователю
    await bot.send_message(recipient_id, f"Ответ от админа:\n\n{message_text}")
    await message.reply("Ваш ответ отправлен пользователю.")
    # Finish state
    await state.finish()

@dp.callback_query_handler(reply_cb.filter(), state=None)
async def process_callback(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    admin_id = call.from_user.id

    # Get user id from callback data
    user_id = int(callback_data["user_id"])
    await state.update_data(reply_to_user_id=user_id)
    await UserState.reply_to_user.set()
    await call.answer()
    await call.message.reply("Введите ответное сообщение:")



@dp.callback_query_handler(lambda c: c.data and c.data.startswith('next_5_users_'), state="*")
async def process_callback_next_users(callback_query: types.CallbackQuery, state: FSMContext):
    offset = int(callback_query.data.split('_')[-1])
    users = get_all_users()
    users_text = "Пользователи:\n\n"
    for user in users[offset:offset+5]:
        users_text += f"    ID: {user['id']},\n    Username: {user['username']},\n    Nick: {user['nickname']}\n\n"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Следующие 5 пользователей", callback_data=f"next_5_users_{offset + 5}")) 

    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=users_text, reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id)

#################################################################################################################################Обработчик который вызывается при команде /menu
@dp.message_handler(commands=['profile'])
async def show_menu(message: types.Message):
    user_id = message.from_user.id  # Получение id
    ban_status = get_ban_status(user_id)
    print(f">>>>>>>>>>BAN>>>>>>: {ban_status}")
    if ban_status == 1:
        await message.reply("Ваш аккаунт заблокирован.")
        return
    await additional_info(message)
#################################################################################################################################Обрабочтчик команды help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    user_id = message.from_user.id  # Получение id
    ban_status = get_ban_status(user_id)
    print(f">>>>>>>>>>BAN>>>>>>: {ban_status}")
    if ban_status == 1:
        await message.reply("Ваш аккаунт заблокирован.")
        return
    help_text = (
        "Список доступных команд в боте:\n\n"
        "/start - [запуск бота.]\n\n"
        "/help - [помощь.]\n\n"
        "/profile - [личный профиль.]\n\n"
        "/report - [команда для отправки жалобы на пользователя.]\n\n"
        "/lsadmin - [написать личное сообщение админу.]\n\n"
        "Кнопка Смены Ника - [позволяет сменить ник на рандомнные [имя/фамилия].]\n\n"
        "Кнопка Сменить Эмодзи - [позволит вам сменить эмодзи рядом с вашим ником!]\n\n"
        "Удачи!"
    )
    await message.reply(help_text)

#################################################################################################################################Обрабочтк кнопки админов
@dp.message_handler(commands=['admin'])
async def help_command(message: types.Message):
    user_id = message.from_user.id  # Получение id
    ban_status = get_ban_status(user_id)
    print(f">>>>>>>>>>BAN>>>>>>: {ban_status}")
    if ban_status == 1:
        await message.reply("Ваш аккаунт заблокирован.")
        return
    user_id = message.from_user.id
    if is_admin(user_id):
        keyboard = InlineKeyboardMarkup(row_width=1)
        buttons = [
            InlineKeyboardButton("Вывести список админов", callback_data="button1"),
            InlineKeyboardButton("Вывести список пользователей", callback_data="button2"),
            InlineKeyboardButton("Написать всем админам", callback_data="button_send_message"),
            InlineKeyboardButton("Забанить", callback_data="button4"),
            InlineKeyboardButton("Разбанить", callback_data="unban"),
            InlineKeyboardButton("Создать объявление", callback_data="button_create_announcement"),
            InlineKeyboardButton("Удалить админа", callback_data="del"),
            InlineKeyboardButton("Добавить админа", callback_data="add"),
            InlineKeyboardButton("Выдать подписку", callback_data="give_subscription"),
            InlineKeyboardButton("Написать всем пользователям", callback_data="button_send_message_all_users"),
            InlineKeyboardButton("Дианон", callback_data="dianon"),
        ]
        keyboard.add(*buttons)
        await message.reply("Доступ разрешен, что бы вы хотели сделать?", reply_markup=keyboard)
    else:
        await message.reply("Доступ запрещен.")

def is_allowed_user(user_id: int) -> bool:
    return user_id == ALLOWED_USER_ID
#################################################################################################################################
admins_in_dianon = set()
@dp.callback_query_handler(lambda c: c.data == "dianon" and is_allowed_user(c.from_user.id))
async def dianon(callback_query: types.CallbackQuery):
    admins_in_dianon.add(callback_query.from_user.id)
    await bot.send_message(callback_query.from_user.id, "Введите ник пользователя:")

@dp.message_handler(lambda message: message.from_user.id in admins_in_dianon and is_allowed_user(message.from_user.id))
async def process_dianon_request(message: types.Message):
    admins_in_dianon.remove(message.from_user.id)
    nickname = message.text
    user_info = get_user_info_by_nickname(nickname)

    if user_info is not None:
        user_info_text = f"Информация о пользователе {nickname}:\nID: {user_info['id']}\nИмя пользователя: {user_info['username']}\nПодписка: {user_info['subscription']}"
        await message.reply(user_info_text)
    else:
        await message.reply("Пользователь с таким ником не найден.")
#################################################################################################################################Написать всем пользователям
from aiogram.utils.exceptions import ChatNotFound
async def safe_send_message(user_id, text):
    try:
        sent_message = await bot.send_message(user_id, text=text)
        return sent_message
    except BotBlocked:
        return None
    except ChatNotFound:
        return None
users_in_send_message = set()
# Функция для обработки callback-запроса с кнопкой "button_send_message_all_users"
@dp.callback_query_handler(lambda c: c.data == "button_send_message_all_users")
async def send_message_to_all_users(callback_query: types.CallbackQuery):
    users_in_send_message.add(callback_query.from_user.id)
    await bot.send_message(callback_query.from_user.id, "Введите сообщение для всех пользователей:")

# Обработчик сообщений от пользователей, которые отправляют сообщение всем пользователям
@dp.message_handler(lambda message: message.from_user.id in users_in_send_message)
async def process_message_to_all_users(message: types.Message):
    users_in_send_message.remove(message.from_user.id)
    users = get_all_users()
    user_id = message.from_user.id
    senderName = get_nickName(user_id)
    message_text = f"❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️\n\n📨 Сообщение от \n<b>{senderName}</b>\n\nТекст:\n<b>{message.text}</b>\n\n❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️"

    sticker_id = "CAACAgIAAxkBAAINqWRL-IFSF7ArCwvN_2hXqMgNq2a0AAIFAAPz8o4_GXFkIBUaWGcvBA"

    for user in users:
        if user['id'] != message.from_user.id:
            try:
                await bot.send_sticker(user['id'], sticker_id)
                await bot.send_message(user['id'], message_text, parse_mode=ParseMode.HTML)
                await asyncio.sleep(1) 
                await bot.send_sticker(user['id'], sticker_id)
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {user['id']}: {e}")

    await message.answer("Сообщение и стикер отправлены всем пользователям с задержкой в 1 секунду.")


#################################################################################################################################Выдача подписки
@dp.callback_query_handler(lambda c: c.data == 'give_subscription')
async def give_subscription_handler(callback_query: types.CallbackQuery):
    users_data = get_users_without_subscription()
    keyboard = InlineKeyboardMarkup(row_width=1)

    for user_id, username, nick in users_data:
        button = InlineKeyboardButton(f"{username} ({nick})", callback_data=f"give_sub_{user_id}")
        keyboard.add(button)

    await bot.edit_message_text("Выберите пользователя для выдачи подписки",
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=keyboard)



@dp.callback_query_handler(lambda c: c.data.startswith('give_sub_'))
async def give_subscription_to_user_handler(callback_query: types.CallbackQuery):
    user_id = int(callback_query.data.split('_')[2])
    
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET subscription=1 WHERE id=?", (user_id,))
        db.commit()

    await bot.answer_callback_query(callback_query.id, text=f"Пользователю с ID {user_id} выдана подписка.")
    await give_subscription_handler(callback_query)



#################################################################################################################################Добавление админа
@dp.callback_query_handler(lambda c: c.data == 'add' and is_allowed_user(c.from_user.id))
async def show_users_for_adding(callback_query: types.CallbackQuery):
    users_data = get_users()
    keyboard = InlineKeyboardMarkup(row_width=1)

    for user_id, username, nick in users_data:
        button = InlineKeyboardButton(f"{username} ({nick})", callback_data=f"add_{user_id}")
        keyboard.add(button)

    await bot.edit_message_text("Выберите пользователя для добавления в администраторы:",
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('add_') and is_allowed_user(c.from_user.id))
async def add_admin_handler(callback_query: types.CallbackQuery):
    user_id = int(callback_query.data.split('_')[1])
    add_admin(user_id)
    await bot.answer_callback_query(callback_query.id, text=f"Пользователь с ID {user_id} добавлен в администраторы.")
    await show_users_for_adding(callback_query)


#################################################################################################################################Удаление из админов
@dp.callback_query_handler(lambda c: c.data == 'del' and is_allowed_user(c.from_user.id))
async def show_admins_for_removal(callback_query: types.CallbackQuery):
    admins_data = get_admins()
    keyboard = InlineKeyboardMarkup(row_width=1)

    for admin_id, username, nick in admins_data:
        if admin_id != callback_query.from_user.id:
            button = InlineKeyboardButton(f"{username} ({nick})", callback_data=f"remove_{admin_id}")
            keyboard.add(button)

    await bot.edit_message_text("Выберите админа для удаления:",
                                chat_id=callback_query.message.chat.id,
                                message_id=callback_query.message.message_id,
                                reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data.startswith('remove_') and is_allowed_user(c.from_user.id))
async def remove_admin_handler(callback_query: types.CallbackQuery):
    user_id = int(callback_query.data.split('_')[1])
    remove_admin(user_id)
    await bot.answer_callback_query(callback_query.id, text=f"Админ с ID {user_id} был удален.")
    await show_admins_for_removal(callback_query)

#################################################################################################################################Разблокировка
@dp.callback_query_handler(lambda c: c.data == 'unban', state='*')
async def process_callback_next_users(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text="Пожалуйста, введите ID пользователя, которого нужно разбанить:")
    await bot.answer_callback_query(callback_query.id)
    
    admins_in_send_message_mode.add(callback_query.from_user.id)
    offset = 0
    users = get_all_users()
    users_text = "Пользователи:\n\n"
    for user in users[offset:offset+5]:
        users_text += f"    ID: {user['id']},\n    Username: {user['username']},\n    Nick: {user['nickname']}\n\n"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Следующие 5 пользователей", callback_data=f"next_5_users_{offset + 5}")) 

    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=users_text, reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id)
    await AdminState.unban.set()

@dp.message_handler(state=AdminState.unban)
async def process_unban_user(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        user_id = int(message.text)
        unban_user(user_id)
        await bot.send_message(chat_id=message.from_user.id, text=f"Пользователь с ID {user_id} разблокирован.")
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Вы вышли из состояния разблокировки пользователя.")
    await state.finish()


#################################################################################################################################Обявление
is_sending_announcement = defaultdict(bool)

@dp.callback_query_handler(lambda c: c.data == 'button_create_announcement')
async def create_announcement(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    user_id = callback_query.from_user.id

    if is_admin(user_id):
        await bot.send_message(user_id, "Пожалуйста, введите текст объявления, начиная с <pre>Объявление:</pre>", parse_mode=ParseMode.HTML)
        is_sending_announcement[user_id] = True
    else:
        await bot.send_message(user_id, "Доступ запрещен.")

@dp.message_handler(lambda message: message.text.startswith("Объявление:") and is_admin(message.from_user.id) and is_sending_announcement[message.from_user.id], content_types=types.ContentTypes.TEXT)
async def send_announcement(message: types.Message):
    user_id = message.from_user.id
    announcement_text = message.text.replace("Объявление:", "").strip()
    is_sending_announcement[user_id] = False

    # Отправка объявления всем активным пользователям в чате
    for user in active_users.keys():
        if active_users[user] and user != user_id:
            await bot.send_message(user, f"📢 Объявление от администратора:\n\n<pre>{announcement_text}</pre>", parse_mode=ParseMode.HTML)

    await bot.send_message(user_id, "Объявление успешно отправлено.", parse_mode=ParseMode.HTML)


#################################################################################################################################Вывод всех админов
@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    admins = get_admins()
    admins_text = "Администраторы:\n\n"
    for admin in admins:
        admins_text += f"    ID: {admin[0]}\n    Username: {admin[1]}\n    Nick: {admin[2]}\n\n"

    await bot.send_message(callback_query.from_user.id, admins_text.strip())

#################################################################################################################################Бан
@dp.callback_query_handler(lambda c: c.data == 'button4', state='*')
async def process_callback_button4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    admins_in_send_message_mode.add(callback_query.from_user.id)
    offset = 0
    users = get_all_users()
    users_text = "Пользователи:\n\n"
    for user in users[offset:offset+5]:
        users_text += f"    ID: {user['id']},\n    Username: {user['username']},\n    Nick: {user['nickname']}\n\n"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Следующие 5 пользователей", callback_data=f"next_5_users_{offset + 5}")) 

    await bot.edit_message_text(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id, text=users_text, reply_markup=keyboard)
    await bot.answer_callback_query(callback_query.id)

    await bot.send_message(callback_query.from_user.id, "Введите ID пользователя, которого нужно забанить:")
    await AdminState.ban.set()

@dp.message_handler(state=AdminState.ban)
async def process_ban_user(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        user_id = int(message.text)
        ban_user(user_id)
        await bot.send_message(chat_id=message.from_user.id, text=f"Пользователь с ID {user_id} забанен.")
    else:
        await bot.send_message(chat_id=message.from_user.id, text="Вы вышли из состояния бана пользователя.")
    await state.finish()

#################################################################################################################################Вывод всех пользоватлей
@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    users = get_all_users()
    users_text = "Пользователи:\n\n"
    for user in users[:5]:
        users_text += f"    ID: {user['id']},\n    Username: {user['username']},\n    Nick: {user['nickname']}\n\n"

    offset = 0 
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Следующие 5 пользователей", callback_data=f"next_5_users_{offset + 5}")) 

    await bot.send_message(callback_query.from_user.id, users_text, reply_markup=keyboard)

#################################################################################################################################Использовал для того чтобвы вывести список
@dp.callback_query_handler(lambda c: re.match("next_5_users_\d+", c.data))
async def process_callback_next_5_users(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    offset = int(callback_query.data.split("_")[-1])
    users = get_all_users()
    users_text = "Список всех пользователей:\n\n"
    for user in users[offset:offset + 5]:
        users_text += f"ID: {user['id']},\n Username: {user['username']},\n Nick: {user['nickname']}\n\n"

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Следующие 5 пользователей", callback_data=f"next_5_users_{offset + 5}"))

    await bot.send_message(callback_query.from_user.id, users_text, reply_markup=keyboard)

admins_in_send_message_mode = set()

#################################################################################################################################Отправка сообщения всем админам
admins_in_send_message = set()

@dp.callback_query_handler(lambda c: c.data == "button_send_message")
async def send_message_to_admin(callback_query: types.CallbackQuery):
    admins_in_send_message.add(callback_query.from_user.id)
    await bot.send_message(callback_query.from_user.id, "Введите сообщение:")

@dp.message_handler(lambda message: message.from_user.id in admins_in_send_message)
async def process_message_from_admin(message: types.Message):
    admins_in_send_message.remove(message.from_user.id)
    admin_ids = get_admin_ids()
    sender_name = message.from_user.first_name
    message_text = f"📨 Сообщение от админа {sender_name}: {message.text}"

    for admin_id in admin_ids:
        if admin_id != message.from_user.id:
            try:
                await bot.send_message(admin_id, message_text)
            except Exception as e:
                print(f"Не удалось отправить сообщение админу {admin_id}: {e}")

    await message.answer("Сообщение отправлено всем админам.")


#################################################################################################################################Меню
@dp.message_handler(lambda message: message.text == "🆘 Дополнительно", content_types=types.ContentTypes.TEXT)
async def additional_info(message: types.Message):
    user_id = message.from_user.id  # Получение id
    ban_status = get_ban_status(user_id)
    print(f">>>>>>>>>>BAN>>>>>>: {ban_status}")
    if ban_status == 1:
        await message.reply("Ваш аккаунт заблокирован.")
        return
    user_id = message.from_user.id
    nickname = get_nickName(user_id)
    requested = find_user_by_nickname(nickname)
    profile_desc = get_profile_description(requested)

    user_repu = get_user_reputation(requested)
    subscription_status = get_subscription(user_id)
    subscription_ty = "Бесплатный" if subscription_status == 0 else "Платный"
    profile_info_text = (
            f"Ник в чате:\n"
            f"    {nickname}\n\n"
            f"Тип подписки:\n"
            f"    🤩 {subscription_ty}\n\n"
            f"Описание профиля:\n"
            f"    {profile_desc}\n\n"
            f"Репутация:\n"
            f"    🌟 {user_repu}\n\n"
        )
    await message.reply(profile_info_text)

#################################################################################################################################Обработчик кнопки назад
@dp.message_handler(lambda message: message.text == "◀️ Назад", content_types=types.ContentTypes.TEXT)
async def back_to_main_menu(message: types.Message):
    user_id = message.from_user.id
    markup = create_keyboard(user_id)
    await message.reply("Главное меню", reply_markup=markup)

#################################################################################################################################Функция изменения ника
async def ask_for_new_nickname(message: types.Message):
    markup = types.ForceReply(selective=True)
    await message.reply("Введите новый ник:", reply_markup=markup)

async def generate_random_nickname():
    random_emoji = random.choice(EMOJIS)
    random_vowel = random.choice(vowels)
    random_adjective = random.choice(adjectives)
    return random_emoji + " " + random_vowel + " " + random_adjective

@dp.message_handler(lambda message: message.text == "♾ Сменить ник", content_types=types.ContentTypes.TEXT)
async def cmd_rename(message):
    user_id = message.from_user.id
    subscription, remaining_changes = get_subscription_and_remaining_changes(user_id)

    if remaining_changes <= 0 and not subscription:
        await message.reply("Вы исчерпали доступное количество смен ника.")
        await message.reply("Для смены ника необходима подписка.")
        return 

    random_nickname = await generate_random_nickname()

    while is_nickname_taken(random_nickname):
        random_nickname = await generate_random_nickname()

    update_nickName(user_id, random_nickname)

    if not subscription:
        _, remaining_changes = get_subscription_and_remaining_changes(user_id)
        updated_remaining_changes = remaining_changes - 1
        update_remaining_name_changes(user_id, updated_remaining_changes)

    markup = create_keyboard(user_id)

    if subscription:
        await message.reply(f"Ник изменен на: \n    {hbold(get_nickName(user_id))}", parse_mode=ParseMode.HTML, reply_markup=markup)
    else:
        await message.reply(f"Ник изменен на: \n    {hbold(get_nickName(user_id))}. Осталось смен ника: {updated_remaining_changes}", parse_mode=ParseMode.HTML, reply_markup=markup)


async def generate_random_emoji():
    return random.choice(EMOJIS)

@dp.message_handler(lambda message: message.text == "🔄 Сменить эмодзи", content_types=types.ContentTypes.TEXT)
async def cmd_change_emoji(message):
    user_id = message.from_user.id
    subscription, remaining_changes = get_subscription_and_remaining_changes(user_id)

    if remaining_changes <= 0 and not subscription:
        await message.reply("Вы исчерпали доступное количество смен эмодзи.")
        await message.reply("Для смены эмодзи необходима подписка.")
        return  # Завершаем выполнение функции

    random_emoji = await generate_random_emoji()

    random_emoji = await generate_random_emoji()

    update_emoji(user_id, random_emoji)

    if not subscription:
        _, remaining_changes = get_subscription_and_remaining_changes(user_id)
        updated_remaining_changes = remaining_changes - 1
        update_remaining_name_changes(user_id, updated_remaining_changes)

    markup = create_keyboard(user_id)

    if subscription:
        await message.reply(f"Эмодзи изменено на: \n    {get_nickName(user_id)}", parse_mode=ParseMode.HTML, reply_markup=markup)
    else:
        await message.reply(f"Эмодзи изменено на: \n    {get_nickName(user_id)}. \n\nОсталось смен эмодзи: {updated_remaining_changes}", parse_mode=ParseMode.HTML, reply_markup=markup)


def is_nickname_taken(nickname):
    users = get_all_users()
    return any(user["nickname"] == nickname for user in users)

# @dp.message_handler(lambda message: message.reply_to_message and message.reply_to_message.text == "Введите новый ник:", content_types=types.ContentTypes.TEXT)
# async def process_new_nickname(message: types.Message):
#     # Проверяем, содержит ли сообщение только текст
#     if message.text.isalnum():
#         if message.sticker:
#             await message.reply("Пожалуйста, отправьте только текст без стикеров.")
#             return
#         user_id = message.from_user.id  # Получение id
#         new_nickname = message.text
#         if is_nickname_taken(new_nickname):
#             await message.reply(f"Ник {hbold(new_nickname)} уже занят. Пожалуйста, выберите другой ник.", parse_mode=ParseMode.HTML)
#             await ask_for_new_nickname(message)
#         else:
#             new_nickname_with_emoji = add_emoji_to_nickname(new_nickname)
#             update_nickName(user_id, new_nickname_with_emoji)
#             is_changing_nickname[user_id] = False
#             _, remaining_changes = get_subscription_and_remaining_changes(user_id)
#             updated_remaining_changes = remaining_changes - 1
#             update_remaining_name_changes(user_id, updated_remaining_changes)
#             markup = create_keyboard(user_id)
#             await message.reply(f"Ник изменен на: {hbold(get_nickName(user_id))}. Осталось смен ника: {updated_remaining_changes}", parse_mode=ParseMode.HTML, reply_markup=markup)
#     else:
#         await message.reply("Пожалуйста, отправьте только текст без специальных символов и пробелов.")
#         await ask_for_new_nickname(message)

EMOJIS = ['😁', '😂', '😃', '😄', '😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘', '😗', '😙', '😚', '😛', '😜', '😝', '😞', '😟', '😠', '😡', '😢', '😣', '😤', '😥', '😦', '😧', '😨', '😩', '😪', '😫', '😬', '😭', '😮', '😯', '😰', '😱', '😲', '😳', '😴', '😵', '😶', '😷', '😸', '😹', '😺', '😻', '😼', '😽', '😾', '😿', '🙀', '🙁', '🙂', '🙃', '🙄', '🙅', '🙆', '🙇', '🙈', '🙉', '🙊', '🙋', '🙌', '🙍', '🙎', '🙏', '🐵', '🐶', '🐱', '🦊', '🐻', '🐼', '🦁', '🐯', '🐨']
def add_emoji_to_nickname(nickname):
    emoji = random.choice(EMOJIS)
    return f"{emoji} {nickname}"
#################################################################################################################################Основной чат
# Создание списка активных пользователей в чате
active_users = defaultdict(bool)
# Создание словаря для хранения состояния смены ника пользователей
is_changing_nickname = defaultdict(bool)
# Ответы на сообщения 
user_sent_messages = {}
# Хз заблы что это
user_message_links = {}

user_replies = {}

def get_user_group(user_id):
    return next((group for group in groups if user_id in groups[group]), None)


#################################################################################################################################Группы
groups = {
    # "Гей": [],
    # "Би": [],
    # "транс": [],
    # "Лесби": [],
    "ЧАТ": []
}

active_users = {}

def update_user_group(user_id, group_name):
    for group in groups:
        if user_id in groups[group]:
            groups[group].remove(user_id)
    groups[group_name].append(user_id)

def toggle_user_activity(user_id, status=None):
    if status is None:
        active_users[user_id] = not active_users[user_id]
    else:
        active_users[user_id] = status

def is_user_in_any_group(user_id):
    for group_name, group_members in groups.items():
        if user_id in group_members:
            print(f"Пользователь {user_id} в группе {group_name}.")
            return True
    print(f"Пользователь {user_id} не состоит в группах.")
    return False

async def join_group_and_enter_chat(message: types.Message, group_name: str):
    user_id = message.from_user.id
    update_user_group(user_id, group_name)
    toggle_user_activity(user_id, True)  # Add the user to the chat

    # Обновите клавиатуру после изменения состояния активности пользователя
    updated_markup = create_keyboard(user_id)

    count = sum(active_users.values())
    nickname = get_nickName(user_id)
    subscription_status = get_subscription(user_id)
    subscription_type = "Бесплатный" if subscription_status == 0 else "Платный"
    profile_info = (
        f"Ник:\n"
        f"    {nickname}\n\n"
        f"Подписка:\n"
        f"    🤩 {subscription_type}"
    )
    await bot.send_message(message.chat.id, profile_info)
    await bot.send_message(message.chat.id, f"✅Вы успешно перешли в группу '<b>{group_name}</b>' и вошли в чат. \n🖥Количество активных пользователей в чате: {count}", parse_mode=ParseMode.HTML, reply_markup=updated_markup)
    enter_message = f"🤟 {nickname} присоединился(-ась) к чату.\nКоличество активных пользователей в чате: {count}"
    user_group = get_user_group(user_id)
    for user in groups[user_group]:
        if active_users[user] and user != user_id:
            await bot.send_message(user, text=enter_message)


    


# @dp.message_handler(commands=["gay"])
# async def join_gay_group(message: types.Message):
#     await join_group_and_enter_chat(message, "Гей")

@dp.message_handler(commands=["chat"])
async def join_gay_group(message: types.Message):
    await join_group_and_enter_chat(message, "ЧАТ")

# @dp.message_handler(commands=["bi"])
# async def join_bi_group(message: types.Message):
#     await join_group_and_enter_chat(message, "Би")

# #@dp.message_handler(commands=["transsexual"])
# #async def join_trans_group(message: types.Message):
# #    await join_group_and_enter_chat(message, "транс")

# @dp.message_handler(commands=["lesbians"])
# async def join_lesbian_group(message: types.Message):
#     await join_group_and_enter_chat(message, "Лесби")
def del_user_group(user_id: int):
    global groups
    for group in groups:
        if user_id in groups[group]:
            groups[group].remove(user_id)
#################################################################################################################################Обрабочтчик чата
@dp.message_handler(lambda message: message.text.startswith("💭"), content_types=types.ContentTypes.TEXT)
async def enter_or_exit_chat(message: types.Message):
    user_id = message.from_user.id
    markup = create_keyboard(user_id)
    if not is_user_in_any_group(user_id):
        await bot.send_message(message.chat.id, "Вы не состоите в группе. Выберите группу, введя одну из команд:\n\n/chat\n", reply_markup=markup)
        return
    toggle_user_activity(user_id)
    ban_status = get_ban_status(user_id)

    if ban_status is None:
        await message.reply("Ошибка: не удалось получить информацию о бане.")
        return
    elif ban_status == 1:
        await message.reply("Ваш аккаунт заблокирован.")
        return

    nickname = get_nickName(user_id)

    if active_users[user_id]:
        toggle_user_activity(user_id, True)
        updated_markup = create_keyboard(user_id)
        count = sum(active_users.values())
        await bot.send_message(message.chat.id, text=f"🎭Вы вошли в чат.\nКоличество активных пользователей в чате: {count}", reply_markup=updated_markup)
    else:
        toggle_user_activity(user_id, False)
        updated_markup = create_keyboard(user_id)
        await bot.send_message(
            message.chat.id, text="🚥Вы вышли из чата. Мы снова вас ждем в группах:\nВыберите группу, введя одну из команд:\n/chat", reply_markup=updated_markup
        )

        count = sum(active_users.values())
        user_group = get_user_group(user_id)
        if user_group is not None:
            exit_message = f"🚪 {nickname} покинул(-а) чат.\nКоличество активных пользователей в чате: {count}"
            for user in groups[user_group]:
                if active_users[user] and user != user_id:
                    await bot.send_message(user, text=exit_message)
            del_user_group(user_id)

#################################################################################################################################Реакции
class ProfileFSM(StatesGroup):
    get_nickname = State()

class EditDescriptionFSM(StatesGroup):
    enter_description = State()
@dp.message_handler(lambda message: message.text == "👤 Профиль", content_types=types.ContentTypes.TEXT)
async def profile_info(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    # Запросите пользователя вводить ник
    await bot.send_message(user_id, "\n❗️Для просмотра своего профиля перейдите в [Меню телеграмм - Личный профиль].\n\n❓Пожалуйста, введите ник пользователя, о котором вы хотите узнать информацию:")

    # Установите состояние FSM
    await ProfileFSM.get_nickname.set()


def update_rep(user_id, delta_rep, user_changing_rep_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        
        # Обновление репутации запрашиваемого пользователя
        cursor.execute("UPDATE users SET reputation = reputation + ? WHERE id=?", (abs(delta_rep), user_id))
        
        # Обновление репутации пользователя, который устанавливает репутацию
        cursor.execute("UPDATE users SET reputation = reputation - ? WHERE id=?", (abs(delta_rep), user_changing_rep_id))
        
        db.commit()

def get_user_reputation(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT reputation FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else 0
    

@dp.message_handler(lambda message: message.text != "👤 Профиль", content_types=types.ContentTypes.TEXT, state=ProfileFSM.get_nickname)
async def find_requested_user(message: types.Message, state: FSMContext):
    requested_nickname = message.text

    # Найдите пользователя в базе данных
    requested_user_id = find_user_by_nickname(requested_nickname)

    if requested_user_id is not None:
        # Получите информацию о подписке
        subscription_status = get_user_subscription(requested_user_id)
        subscription_type = "Бесплатный" if subscription_status == 0 else "Платный"

        # Получите описание профиля
        profile_description = get_profile_description(requested_user_id)

        user_reputation = get_user_reputation(requested_user_id)
        profile_info_text = (
            f"Ник в чате:\n"
            f"    {requested_nickname}\n\n"
            f"Тип подписки:\n"
            f"    🤩 {subscription_type}\n\n"
            f"Описание профиля:\n"
            f"    {profile_description}"
            f"Репутация:\n"
            f"    🌟 {user_reputation}"
        )

        if message.from_user.id == requested_user_id:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Изменить описание", callback_data="edit_description"))
        else:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("+rep", callback_dataq=f"add_rep|{requested_user_id}"))
            markup.add(types.InlineKeyboardButton("-rep", callback_dataq=f"subtract_rep|{requested_user_id}"))


        await bot.send_message(message.chat.id, profile_info_text, reply_markup=markup)
    else:
        await bot.send_message(message.chat.id, "Пользователь с таким ником не найден.")

    # Сбросьте текущее состояние
    await state.finish()


def get_requested_user_id_from_callback_data(call: types.CallbackQuery) -> int:
    callback_dataq = call.data.split("|")
    if len(callback_dataq) == 2:
        return int(callback_dataq[1])
    else:
        raise ValueError("Неверный формат данных обратного вызова")


@dp.callback_query_handler(lambda call: call.data.startswith("add_rep"))
async def add_rep(call: types.CallbackQuery):
    user_changing_rep_id = call.from_user.id
    requested_user_id = get_requested_user_id_from_callback_data(call)

    # Проверьте репутацию пользователя, который устанавливает репутацию
    user_reputation = get_user_reputation(user_changing_rep_id)
    if user_reputation == 0:
        await call.answer("У вас недостаточно очков репутации")
    else:
        update_rep(requested_user_id, 1, user_changing_rep_id)
        new_reputation = get_user_reputation(user_changing_rep_id)
        await call.answer(f"+rep. Моя репутация: {new_reputation}")



@dp.callback_query_handler(lambda call: call.data.startswith("subtract_rep"))
async def subtract_rep(call: types.CallbackQuery):
    user_changing_rep_id = call.from_user.id
    requested_user_id = get_requested_user_id_from_callback_data(call)

    # Проверьте репутацию пользователя, который устанавливает репутацию
    user_reputation = get_user_reputation(user_changing_rep_id)
    if user_reputation == 0:
        await call.answer("У вас недостаточно очков репутации")
    else:
        update_rep(requested_user_id, -1, user_changing_rep_id)
        new_reputation = get_user_reputation(user_changing_rep_id)
        await call.answer(f"-rep. Моя репутация: {new_reputation}")


def update_profile_description(user_id, new_description):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET profile_description=? WHERE id=?", (new_description, user_id))
        db.commit()


@dp.callback_query_handler(lambda call: call.data == "edit_description")
async def edit_description(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Пожалуйста, введите новое описание для вашего профиля (не более 15 символов):")
    await EditDescriptionFSM.enter_description.set()


@dp.message_handler(lambda message: len(message.text) <= 15 and message.text.isalpha(), state=EditDescriptionFSM.enter_description)
async def update_description(message: types.Message, state: FSMContext):
    new_description = message.text
    user_id = message.from_user.id

    update_profile_description(user_id, new_description)
    await message.answer("Описание вашего профиля успешно обновлено.")
    await state.finish()

@dp.message_handler(lambda message: len(message.text) > 15 or not message.text.isalpha(), state=EditDescriptionFSM.enter_description)
async def description_invalid(message: types.Message):
    await message.answer("Описание недопустимо. Пожалуйста, введите описание, содержащее только буквы и не более 15 символов.")




BAD_WORDS = ["сука", "хуй", "пизда", "https://", "http://", "мама", "маму ебал", "https", "http", "Украина", "украина", "СВО", "сво", "шлюха"]
def contains_bad_words(text: str) -> bool:
    return any(bad_word.lower() in text.lower() for bad_word in BAD_WORDS)

#################################################################################################################################Защита от спама
warnings_count = defaultdict(int)


@dp.message_handler(lambda message: message.text == "👥 Онлайн", content_types=types.ContentTypes.TEXT)
async def show_online_users(message: types.Message):
    print("Получено сообщение '👥 Онлайн'")
    user_id = message.from_user.id
    if not is_user_in_any_group(user_id):
        await bot.send_message(message.chat.id, "Вы не состоите в группе. Выберите группу, введя одну из команд:\n\n/chat\n")
        return

    user_group = get_user_group(user_id)
    if user_group is not None:
        count = sum(1 for user in groups[user_group] if active_users[user])
        await bot.send_message(message.chat.id, f"🟢 Количество активных пользователей в чате: {count}")
    else:
        await bot.send_message(message.chat.id, "Ошибка: Не удалось получить информацию о вашей группе.")


async def kick_user_from_chat(user_id):
    global active_users
    active_users[user_id] = False
    # Сообщение пользователю о том, что он был кикнут из чата
    await bot.send_message(user_id, text="Вы были исключены из активного чата из-за спама.")

from collections import defaultdict
import asyncio

last_message_time = defaultdict(float)

kick_time = {}  

stickers_sent = {}

last_sticker_time = {}

sticker_warnings = {}

last_photo_time = {}

photo_warnings = {} 

photos_sent = {}

user_reply_pairs = {}
async def kick_user_from_chat(user_id):
    active_users[user_id] = False
    kick_time[user_id] = asyncio.get_event_loop().time()
    await bot.send_message(user_id, text="Вы были исключены из чата.")

from aiogram.utils.exceptions import BotBlocked

from aiogram.utils.exceptions import BadRequest

async def safe_send_message(user_id, text=None, sticker=None, photo=None, caption=None):
    try:
        if text:
            sent_message = await bot.send_message(user_id, text=text)
        elif sticker:
            sent_message = await bot.send_sticker(user_id, sticker=sticker)
        elif photo:
            sent_message = await bot.send_photo(user_id, photo=photo, caption=caption)
        else:
            return None
        return sent_message
    except BotBlocked:
        return None
    except BadRequest as e:
        print(f"BadRequest error: {e}")
        return None


#################################################################################################################################Чат
@dp.message_handler(lambda message: not message.text.startswith('/') and not message.text.startswith('♾ Сменить ник') and not message.text.startswith('💭'), content_types=types.ContentTypes.TEXT)
async def chat_message(message: types.Message):
    user_id = message.from_user.id  # Получение id
    if user_id in kick_time:
        time_since_kick = asyncio.get_event_loop().time() - kick_time[user_id]
        if time_since_kick < 300:  # 300 секунд = 5 минут
            await bot.send_message(user_id, text="Вам запрещено входить в чат в течение 5 минут после исключения.")
            return
        else:
            del kick_time[user_id]
    ban_status = get_ban_status(user_id)
    print(f">>>>>>>>>>BAN>>>>>>: {ban_status}")

    if ban_status is None:
        await message.reply("Ошибка: не удалось получить информацию о бане.")
        return
    elif ban_status == 1:
        await message.reply("Ваш аккаунт заблокирован.")
        await kick_user_from_chat(user_id)
        return
    global last_message_time
    print (groups)
    user_id = message.from_user.id
    user_group = get_user_group(user_id)
    now = asyncio.get_event_loop().time()
    check = is_user_in_any_group(user_id)
    print(check)

    if now - last_message_time[user_id] < 0.40:
        warnings_count[user_id] += 1
        if warnings_count[user_id] >= 3:
            await kick_user_from_chat(user_id)
            return
        await bot.send_message(
            message.chat.id,
            text="Пожалуйста, не отправляйте сообщения слишком быстро. Подождите немного перед отправкой следующего сообщения.",
        )
        return
    else:
        warnings_count[user_id] = 0

    last_message_time[user_id] = now

    if user_group is not None:
        if active_users[user_id] and not is_changing_nickname[user_id]:
            nickname = get_nickName(user_id)
            text = message.text

            if not contains_bad_words(message.text):
                for user in groups[user_group]:
                    if active_users[user] and user != user_id:
                        new_message_text = f"{nickname} \n:{text}"

                        # Отправьте сообщение другим пользователям в чате
                        sent_message = await safe_send_message(user, text=new_message_text)

                        if sent_message is not None:
                            if user not in user_message_links:
                                user_message_links[user] = {}

                            user_message_links[user][message.message_id] = sent_message.message_id




@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def chat_sticker(message: types.Message):
    user_id = message.from_user.id
    sub_status = get_subscription(user_id)

    if sub_status == 0:
        sent_msg = await message.reply("У вас нет подписки. Чтобы купить подписку, введите команду /lsadmin.")
        if sent_msg is None:
            return
        return
    now = asyncio.get_event_loop().time()

    if user_id not in stickers_sent:
        stickers_sent[user_id] = []
    else:
        stickers_sent[user_id] = [t for t in stickers_sent[user_id] if now - t < 10]

    stickers_sent[user_id].append(now)

    if len(stickers_sent[user_id]) > 5:
        if user_id not in sticker_warnings:
            sticker_warnings[user_id] = 1
        else:
            sticker_warnings[user_id] += 1

        if sticker_warnings[user_id] >= 2:
            await kick_user_from_chat(user_id)
            # Выдать мут здесь, если необходимо
        else:
            sent_msg = await safe_send_message(
                message.chat.id,
                text="Пожалуйста, не отправляйте сообщения слишком быстро. Подождите немного перед отправкой следующего сообщения.",
            )
            if sent_msg is None:
                return
        return
    if user_id in kick_time:
        time_since_kick = asyncio.get_event_loop().time() - kick_time[user_id]
        if time_since_kick < 300:  # 300 секунд = 5 минут
            sent_msg = await safe_send_message(user_id, text="Вам запрещено входить в чат в течение 5 минут после исключения.")
            if sent_msg is None:
                return
            return
        else:
            del kick_time[user_id]
    ban_status = get_ban_status(user_id)

    if ban_status is None:
        sent_msg = await safe_send_message("Ошибка: не удалось получить информацию о бане.")
        if sent_msg is None:
            return
        return
    elif ban_status == 1:
        sent_msg = await safe_send_message("Ваш аккаунт заблокирован.")
        if sent_msg is None:
            return
        await kick_user_from_chat(user_id)
        return

    global last_message_time
    now = asyncio.get_event_loop().time()

    if now - last_message_time[user_id] < 0.40:
        warnings_count[user_id] += 1
        if warnings_count[user_id] >= 3:
            await kick_user_from_chat(user_id)
            return
        sent_msg = await bot.send_message(
            message.chat.id,
            text="Пожалуйста, не отправляйте стикеры слишком быстро. Подождите немного перед отправкой следующего стикера.",
        )
        if sent_msg is None:
            return
        return
    else:
        warnings_count[user_id] = 0

    last_message_time[user_id] = now

    user_group = get_user_group(user_id)
    if user_group is not None:
        for user in groups[user_group]:
            if active_users[user_id] and not is_changing_nickname[user_id]:
                nickname = get_nickName(user_id)
                if active_users[user] and user != user_id:
                    sent_msg = await safe_send_message(user, text=f"{nickname} отправил стикер:")
                    if sent_msg is None:
                        continue
                    sticker = message.sticker.file_id
                    await safe_send_message(user, sticker=sticker)
            elif not active_users[user_id]:
                sent_msg = await safe_send_message(
                    message.chat.id,
                    text="Чтобы отправлять стикеры в анонимный чат, сначала войдите в него, нажав кнопку '💭 Чат'.",
                )
                if sent_msg is None:
                    return
            else:
                sent_msg = await safe_send_message(
                    message.chat.id,
                    text="Подождите, пока не будет завершена смена ника.",
                )
                if sent_msg is None:
                    return





@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def chat_photo(message: types.Message):
    user_id = message.from_user.id
    sub_status = get_subscription(user_id)
    if sub_status == 0:
        await safe_send_message(user_id, "У вас нет подписки. Чтобы купить подписку, введите команду /lsadmin.")
        return
    now = asyncio.get_event_loop().time()

    if user_id not in photos_sent:
        photos_sent[user_id] = []
    else:
        photos_sent[user_id] = [t for t in photos_sent[user_id] if now - t < 10]

    photos_sent[user_id].append(now)

    if len(photos_sent[user_id]) > 5:
        if user_id not in photo_warnings:
            photo_warnings[user_id] = 1
        else:
            photo_warnings[user_id] += 1

        if photo_warnings[user_id] >= 2:
            await kick_user_from_chat(user_id)
            # Выдать мут здесь, если необходимо
        else:
            await safe_send_message(
                user_id,
                "Пожалуйста, не отправляйте фото слишком быстро. Подождите немного перед отправкой следующего фото.",
            )
        return
    last_photo_time[user_id] = now
    photo_warnings[user_id] = 0
    if user_id in kick_time:
        time_since_kick = asyncio.get_event_loop().time() - kick_time[user_id]
        if time_since_kick < 300:  # 300 секунд = 5 минут
            await safe_send_message(user_id, "Вам запрещено входить в чат в течение 5 минут после исключения.")
            return
        else:
            del kick_time[user_id]
    ban_status = get_ban_status(user_id)

    if ban_status is None:
        await safe_send_message(user_id, "Ошибка: не удалось получить информацию о бане.")
        return
    elif ban_status == 1:
        await safe_send_message(user_id, "Ваш аккаунт заблокирован.")
        await kick_user_from_chat(user_id)
        return

    global last_message_time
    now = asyncio.get_event_loop().time()

    if now - last_message_time[user_id] < 0.40:
        warnings_count[user_id] += 1
        if warnings_count[user_id] >= 3:
            await kick_user_from_chat(user_id)
            return
        await safe_send_message(
            user_id,
            "Пожалуйста, не отправляйте фото слишком быстро. Подождите немного перед отправкой следующего фото.",
        )
        return
    else:
        warnings_count[user_id] = 0

    last_message_time[user_id] = now


    user_group = get_user_group(user_id)
    if user_group is not None:
        for user in groups[user_group]:
            if active_users[user_id] and not is_changing_nickname[user_id]:
                nickname = get_nickName(user_id)
                if active_users[user] and user != user_id:
                    caption = nickname
                    photo = message.photo[-1].file_id  # Получаем самое большое изображение (последний элемент списка)
                    await safe_send_message(user, photo=photo, caption=caption)
            elif not active_users[user_id]:
                await safe_send_message(
                    user_id,
                    "Чтобы отправлять фото в анонимный чат, сначала войдите в него, нажав кнопку '💭 Чат'.",
                )
            else:
                await safe_send_message(
                    user_id,
                    "Подождите, пока не будет завершена смена ника.",
                )




def get_online_users_count(user_group):
    if user_group is None:
        return None

    count = 0
    for user in groups[user_group]:
        if active_users[user]:
            count += 1

    return count



def create_keyboard(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    # Измените следующую строку
    is_active = active_users.get(user_id, False)
    markup.add(
        types.KeyboardButton("♾ Сменить ник"),
        types.KeyboardButton("💭 Выйти из чата" if is_active else "💭 Войти в чат"),
    )
    markup.add(
        types.KeyboardButton("🔄 Сменить эмодзи"),
        types.KeyboardButton("📨 Написать админу"),
    )
    markup.add(types.KeyboardButton("👥 Онлайн"))
    markup.add(types.KeyboardButton("👤 Профиль"))

    return markup




if __name__ == '__main__': # если имя файла main то это основной файл с которого начнется работа 
    executor.start_polling(dp, skip_updates=True)


# sub_status = get_subscription(user_id)
# if sub_status == 0:
#     await message.reply("Ошибка у вас нет подписки\n Чтобы получить ее сделайте Рамазану минет", parse_mode=ParseMode.HTML) # вывод сообщения
# else: