import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('subscriptions.db')
cursor = conn.cursor()

# Выполнить запрос для просмотра всех записей в таблице users
cursor.execute('SELECT * FROM users')

# Получаем все строки
users = cursor.fetchall()

# Вывести все записи пользователей
for user in users:
    print(user)

# Закрыть соединение
conn.close()

# # import telebot
# from telebot import types
# import sqlite3
# from datetime import datetime, timedelta
# import threading
# import time

# API_TOKEN = '8163214877:AAFKyMkngxJocJKDN1L7IQm8kZC0eV1Xey0'
# ADMIN_ID = '1321982385'  # Замените на ID администратора
# CHANNEL_ID = '-1002445975865'  # Ссылка на ваш канал
# SUPPORT_LINK = 'https://t.me/tanya_everything_support'  # Правильная ссылка для кнопки

# bot = telebot.TeleBot(API_TOKEN)

# # Подключение к базе данных SQLite
# conn = sqlite3.connect('subscriptions.db', check_same_thread=False)
# cursor = conn.cursor()

# # Создание таблицы для хранения информации о пользователях
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS users (
#     user_id INTEGER PRIMARY KEY,
#     first_name TEXT,
#     last_name TEXT,
#     subscription_type TEXT,
#     subscription_start_date TEXT,
#     subscription_status TEXT
# )
# ''')
# conn.commit()

# # Команда /start - приветственное сообщение с кнопками "Получить доступ", "Личный кабинет", "Служба поддержки"
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = types.InlineKeyboardMarkup()
#     access_button = types.InlineKeyboardButton("🔓 Получить доступ", callback_data="get_access")
#     account_button = types.InlineKeyboardButton("👤 Личный кабинет", callback_data="account")
#     support_button = types.InlineKeyboardButton("🛠 Служба поддержки", url=SUPPORT_LINK)
#     markup.add(access_button)
#     markup.add(account_button)
#     markup.add(support_button)

    

#     if str(message.chat.id) == ADMIN_ID:  # Проверка, что это администратор
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         send_button = types.KeyboardButton("📨 Отправить рассылку")
#         send_unsub_button = types.KeyboardButton("📨 Отправить рассылку отмененным")
#         markup.add(send_button, send_unsub_button)
#         bot.send_message(message.chat.id, "Добро пожаловать, админ! Вы можете отправить рассылку.", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, """
#             🔑 Ключ к счастью 🔑\n\n✨ Что умеет этот бот? ✨\n💼 Официальный бот для оплаты доступа к каналу «Tanya Everything» 🩷\n🔓 Получи доступ к эксклюзивным материалам и открой для себя больше счастья и вдохновения! 🌸💫\n\n🌟 Простота в использовании\n💳 Легко оплатить и получить доступ через несколько кликов!\n📲 Не упусти возможность погрузиться в интересный и полезный контент, который ждет тебя! 💖\n\n🌈 Канал «Tanya Everything» – это твой проводник к самопознанию, счастью и гармонии! ✨
#         """.strip(), reply_markup=markup)


# # Обработка нажатий на кнопки "Получить доступ", "Личный кабинет"
# @bot.callback_query_handler(func=lambda call: call.data == "get_access" or call.data == "account")
# def handle_main_menu(call):
#     if call.data == "get_access":
#         choose_subscription(call)

#     elif call.data == "account":
#         show_account(call.message)

# # Логика "Получить доступ" (из исходного кода)
# def choose_subscription(call):
#     markup = types.InlineKeyboardMarkup()

#     # Кнопки для выбора подписки
#     one_month = types.InlineKeyboardButton("🗓️ 1 месяц", callback_data="1 месяц")
#     six_months = types.InlineKeyboardButton("🗓️ 6 месяцев", callback_data="6 месяцев")
#     twelve_months = types.InlineKeyboardButton("🗓️ 12 месяцев", callback_data="12 месяцев")

#     markup.add(one_month, six_months, twelve_months)
#     bot.send_message(call.message.chat.id, "✨ Выберите тип подписки: ✨\n\n🔹 <b>1 месяц</b> — 1000₽ / 5100ТГ\nИдеально, если вы хотите попробовать контент и оценить его уникальность.\n\n🔹 <b>6 месяцев</b> — 5000₽ / 25500ТГ\nСамый популярный вариант! Долгосрочный доступ для погружения в эксклюзивные материалы.\n\n🔹 <b>12 месяцев</b> — 10000₽ / 51000ТГ\nМаксимальная выгода! Получите доступ на целый год с экономией по сравнению с ежемесячной подпиской.", reply_markup=markup, parse_mode="HTML")

# # Обработка выбора подписки
# @bot.callback_query_handler(func=lambda call: call.data in ["1 месяц", "6 месяцев", "12 месяцев"])
# def handle_subscription_choice(call):
#     user_id = call.message.chat.id
#     chosen_subscription = call.data

#     # Сохраняем тип подписки и дату начала
#     cursor.execute('REPLACE INTO users (user_id, subscription_type, subscription_start_date, subscription_status) VALUES (?, ?, ?, ?)', 
#                    (user_id, chosen_subscription, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'Ожидание оплаты'))
#     conn.commit()

#     # Запрос имени и фамилии для завершения
#     question = bot.send_message(user_id, "😊Пожалуйста, введите ваше имя:")
#     bot.register_next_step_handler(question, lambda message: ask_last_name(message, chosen_subscription, question.message_id))

#     # Удаляем сообщение с запросом выбора подписки
#     bot.delete_message(call.message.chat.id, call.message.message_id)

# def ask_last_name(message, chosen_subscription, prev_message_id):
#     first_name = message.text
#     user_id = message.chat.id
#     question = bot.send_message(user_id, "👤Теперь введите вашу фамилию:")
#     bot.register_next_step_handler(question, lambda msg: save_user_data(msg, first_name, chosen_subscription, question.message_id))

#     # Удаляем предыдущее сообщение (вопрос) и ответ пользователя
#     bot.delete_message(user_id, message.message_id)
#     bot.delete_message(user_id, prev_message_id)

# def save_user_data(message, first_name, subscription_type, prev_message_id):
#     last_name = message.text
#     user_id = message.chat.id

#     # Обновляем запись о пользователе в базе данных
#     cursor.execute('UPDATE users SET first_name = ?, last_name = ? WHERE user_id = ?', 
#                    (first_name, last_name, user_id))
#     conn.commit()

#     # Словарь с ценами для разных типов подписки
#     subscription_prices = {
#         "1 месяц": "1000₽ / 5100ТГ",
#         "6 месяцев": "5000₽ / 25500ТГ",
#         "12 месяцев": "10000₽ / 51000ТГ"
#     }

#     # Получаем цену для выбранной подписки
#     price = subscription_prices.get(subscription_type, "Неизвестно")

#     # Отправляем пользователю информацию для оплаты с указанием цены
#     bot.send_message(user_id, f"""
# 🎉 Вы выбрали подписку на {subscription_type}.

# 💵 Стоимость: {price}

# 💳 Для завершения оплаты переведите указанную сумму на одну из следующих карт:

# 🇷🇺 Сбер (для оплаты в рублях): 5336 6902 2669 7219 (получатель: Татьяна С)
# 🇰🇿 Kaspi (для оплаты в тенге): 4400 4302 9567 5877 (получатель: Татьяна С)

# 📸 После оплаты отправьте чек в этот чат.

# 🕒 Проверка чека займет до 12 часов.
# 🙏 Спасибо за ваш выбор!
# """)

#     # Удаляем предыдущее сообщение (вопрос) и ответ пользователя
#     bot.delete_message(user_id, message.message_id)
#     bot.delete_message(user_id, prev_message_id)

# # Логика личного кабинета
# def show_account(message):
#     user_id = message.chat.id
#     cursor.execute('SELECT subscription_type, subscription_start_date, subscription_status FROM users WHERE user_id = ?', (user_id,))
#     user_info = cursor.fetchone()

#     if user_info:
#         subscription_type, subscription_start_date, subscription_status = user_info
#         if subscription_status == 'Подтверждено':
#             # Подсчет оставшегося времени подписки
#             start_date = datetime.strptime(subscription_start_date, '%Y-%m-%d %H:%M:%S')
#             days_passed = (datetime.now() - start_date).days

#             if "1 месяц" in subscription_type:
#                 total_days = 30
#             elif "6 месяцев" in subscription_type:
#                 total_days = 180
#             elif "12 месяцев" in subscription_type:
#                 total_days = 365
#             else:
#                 total_days = 0

#             end_date = start_date + timedelta(days=total_days)

#             # Подсчитываем количество дней, прошедших с начала подписки
#             days_passed = (datetime.now() - start_date).days

#             # Подсчитываем количество оставшихся дней
#             days_remaining = total_days - days_passed

#             # Форматируем даты для вывода
#             start_date_str = start_date.strftime('%d-%m-%Y')
#             end_date_str = end_date.strftime('%d-%m-%Y')

#             # Формируем сообщение с датой начала, конца подписки и количеством оставшихся дней
#             if days_remaining > 0:
#                 status_message = (f"⏳ У вас осталось {days_remaining} дней по подписке на {subscription_type}.\n"
#                                   f"🔖 Дата начала: {start_date_str}\n"
#                                   f"📆 Дата окончания: {end_date_str}.")
#             else:
#                 status_message = (f"⚠️ Ваша подписка на {subscription_type} истекла.\n"
#                                   f"🔖 Дата начала: {start_date_str}\n"
#                                   f"📆 Дата окончания: {end_date_str}.")

#             # Кнопки "Продлить подписку", "Отменить подписку", "Назад"
#             markup = types.InlineKeyboardMarkup()
#             extend_button = types.InlineKeyboardButton("🔄 Продлить подписку", callback_data="extend_subscription")
#             cancel_button = types.InlineKeyboardButton("❌ Отменить подписку", callback_data="cancel_subscription")
#             back_button = types.InlineKeyboardButton("🔙 Назад", callback_data="back_to_main")
#             markup.add(extend_button, cancel_button)
#             markup.add(back_button)

#             bot.send_message(user_id, status_message, reply_markup=markup)
#         else:
#             markup = types.InlineKeyboardMarkup()
#             back_button = types.InlineKeyboardButton("🔙 Назад", callback_data="back_to_main")
#             access_button = types.InlineKeyboardButton("🔓 Получить доступ", callback_data="get_access")


#             markup.add(back_button, access_button)

#             msg = bot.send_message(user_id, "🚫 У вас нет активной подписки.🔑 Хотите получить доступ?", reply_markup=markup)
#     else:
#         # Если нет подписки
#         markup = types.InlineKeyboardMarkup()
#         access_button = types.InlineKeyboardButton("Получить доступ", callback_data="get_access")
#         markup.add(access_button)
#         bot.send_message(user_id, "🚫 У вас нет активной подписки.🔑 Хотите получить доступ?", reply_markup=markup)

# # Обработка "Продлить подписку", "Отменить подписку", "Назад"
# @bot.callback_query_handler(func=lambda call: call.data == "extend_subscription" or call.data == "cancel_subscription" or call.data == "back_to_main")
# def handle_account_actions(call):
#     if call.data == "extend_subscription":
#         bot.delete_message(call.message.chat.id, call.message.message_id)
#         extend_subscription(call)
#     elif call.data == "cancel_subscription":
#         cancel_subscription(call)
#     elif call.data == "back_to_main":
#         # Удаляем сообщение личного кабинета и возвращаем к приветственному
#         bot.delete_message(call.message.chat.id, call.message.message_id)
#         # send_welcome(call.message)

# # Логика продления подписки
# def extend_subscription(call):
#     user_id = call.message.chat.id
#     cursor.execute('SELECT subscription_type, subscription_start_date FROM users WHERE user_id = ?', (user_id,))
#     user_info = cursor.fetchone()

#     if user_info:
#         current_subscription_type, subscription_start_date = user_info
#         start_date = datetime.strptime(subscription_start_date, '%Y-%m-%d %H:%M:%S')

#         # Вычисляем оставшееся количество дней по текущей подписке
#         days_passed = (datetime.now() - start_date).days
#         if "1 месяц" in current_subscription_type:
#             total_days = 30
#         elif "6 месяцев" in current_subscription_type:
#             total_days = 180
#         elif "12 месяцев" in current_subscription_type:
#             total_days = 365
#         else:
#             total_days = 0
        
#         # Вычисляем количество оставшихся дней
#         days_remaining = total_days - days_passed

#         # Логика продления аналогична покупке новой подписки
#         markup = types.InlineKeyboardMarkup()

#         # Кнопки для выбора подписки
#         one_month = types.InlineKeyboardButton("🗓️ 1 месяц", callback_data="1 месяц")
#         six_months = types.InlineKeyboardButton("🗓️ 6 месяцев", callback_data="6 месяцев")
#         twelve_months = types.InlineKeyboardButton("🗓️ 12 месяцев", callback_data="12 месяцев")

#         markup.add(one_month, six_months, twelve_months)
#         bot.send_message(call.message.chat.id, f"⏳ У вас осталось {days_remaining} дней по текущей подписке.\n📅 Выберите тип продления:", reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: call.data in ["1 месяц", "6 месяцев", "12 месяцев"])
# def handle_extension_choice(call):
#     user_id = call.message.chat.id
#     chosen_subscription = call.data

#     # Получаем информацию о текущей подписке
#     cursor.execute('SELECT subscription_type, subscription_start_date FROM users WHERE user_id = ?', (user_id,))
#     user_info = cursor.fetchone()

#     if user_info:
#         current_subscription_type, subscription_start_date = user_info
#         start_date = datetime.strptime(subscription_start_date, '%Y-%m-%d %H:%M:%S')

#         # Вычисляем оставшиеся дни текущей подписки
#         days_passed = (datetime.now() - start_date).days
#         if "1 месяц" in current_subscription_type:
#             total_days = 30
#         elif "6 месяцев" in current_subscription_type:
#             total_days = 180
#         elif "12 месяцев" in current_subscription_type:
#             total_days = 365

#         days_remaining = total_days - days_passed

#         # Добавляем новые дни в зависимости от выбранного продления
#         if chosen_subscription == "1 месяц":
#             extra_days = 30
#         elif chosen_subscription == "6 месяцев":
#             extra_days = 180
#         elif chosen_subscription == "12 месяцев":
#             extra_days = 365
#         else:
#             extra_days = 0

#         # Обновляем дату окончания подписки, добавляя дополнительные дни
#         new_end_date = datetime.now() + timedelta(days=days_remaining + extra_days)
#         new_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         # Обновляем запись в базе данных
#         cursor.execute('UPDATE users SET subscription_start_date = ?, subscription_type = ? WHERE user_id = ?', 
#                        (new_start_date, chosen_subscription, user_id))
#         conn.commit()

#         bot.send_message(user_id, f"✅ Продление подписки успешно! 🎉\n 📅 Ваша подписка продлена на {extra_days} дней.")


# # Логика отмены подписки
# # Логика отмены подписки
# def cancel_subscription(call):
#     user_id = call.message.chat.id
#     cursor.execute('SELECT subscription_start_date FROM users WHERE user_id = ?', (user_id,))
#     subscription_start_date = cursor.fetchone()[0]
    
#     today = datetime.now()
#     start_date = datetime.strptime(subscription_start_date, '%Y-%m-%d %H:%M:%S')
#     days_passed = (today - start_date).days

#     if days_passed > 14:
#         # Отказ в возврате
#         bot.send_message(user_id, "❌ Отказ в возврате средств, так как прошло более 2 недель с начала подписки.")
#     else:
#         # Запрос данных для возврата
#         question = bot.send_message(user_id, "❓ Пожалуйста, укажите причину отмены подписки.")
#         bot.register_next_step_handler(question, process_refund_reason, question.message_id)

# # Запрос причины отмены подписки
# def process_refund_reason(message, question_message_id):
#     user_id = message.chat.id
#     reason = message.text

#     # Удаляем сообщение пользователя и запрос причины
#     bot.delete_message(user_id, message.message_id)
#     bot.delete_message(user_id, question_message_id)

#     question = bot.send_message(user_id, "💳 Теперь введите номер карты для возврата.")
#     bot.register_next_step_handler(question, lambda msg: process_refund_details(msg, reason, question.message_id))

# # Обработка данных для возврата
# def process_refund_details(message, reason, question_message_id):
#     user_id = message.chat.id
#     card_details = message.text

#     # Удаляем сообщение пользователя и запрос номера карты
#     bot.delete_message(user_id, message.message_id)
#     bot.delete_message(user_id, question_message_id)

#     # Пересылаем данные админу для подтверждения возврата
#     markup = types.InlineKeyboardMarkup()
#     confirm_button = types.InlineKeyboardButton("Подтвердить отмену", callback_data=f"confirm_cancel_{user_id}")
#     markup.add(confirm_button)

#     username = message.from_user.username if message.from_user.username else f"{message.from_user.first_name} {message.from_user.last_name}"


#     bot.send_message(
#         ADMIN_ID,
#         f"Пользователь @{username} запросил отмену подписки.\nПричина: {reason}\nНомер карты: {card_details}",
#         reply_markup=markup
#     )

#     bot.send_message(user_id, "📨 Ваш запрос на возврат средств отправлен админу. ⏳ Ожидайте подтверждения.")

# # Обработка подтверждения отмены подписки админом
# @bot.callback_query_handler(func=lambda call: call.data.startswith('confirm_cancel_'))
# def handle_cancel_confirmation(call):
#     user_id = call.data.split('_')[-1]

#     # Обнуление подписки пользователя
#     cursor.execute('UPDATE users SET subscription_status = ?, subscription_start_date = ? WHERE user_id = ?',
#                    ('Отменена', None, user_id))
#     conn.commit()

#     # Уведомление пользователя об успешной отмене
#     bot.send_message(user_id, "Ваша подписка успешно отменена и обнулена.")
#     bot.send_message(ADMIN_ID, f"✅ Подписка пользователя {user_id} успешно отменена.")

#     # Сообщение администратору остается, удаление не происходит.

# # Обработка отправки фото чека
# @bot.message_handler(content_types=['photo'])
# def handle_receipt(message):
#     user_id = message.chat.id
    
#     # Получаем информацию о пользователе
#     cursor.execute('SELECT first_name, last_name, subscription_type FROM users WHERE user_id = ?', (user_id,))
#     user_info = cursor.fetchone()

#     if user_info:
#         first_name, last_name, subscription_type = user_info
#     else:
#         first_name, last_name, subscription_type = "Неизвестно", "Неизвестно", "Не указано"
    
#     # Пересылаем чек админу с информацией о пользователе
#     bot.send_message(user_id, "📩 Чек отправлен админу для подтверждения.")
#     bot.forward_message(ADMIN_ID, user_id, message.message_id)
    
#     # Отправляем админу кнопку для подтверждения или отклонения оплаты
#     markup = types.InlineKeyboardMarkup()
#     confirm_button = types.InlineKeyboardButton("Подтвердить оплату", callback_data=f"confirm_{user_id}")
#     decline_button = types.InlineKeyboardButton("Отклонить оплату", callback_data=f"decline_{user_id}")
#     markup.add(confirm_button, decline_button)
    
#     bot.send_message(ADMIN_ID, f"Пользователь {first_name} {last_name} ({user_id}) отправил чек на подписку: {subscription_type}. Подтвердите оплату или отклоните.", reply_markup=markup)

#     # Удаляем сообщение с чеком после обработки
#     bot.delete_message(user_id, message.message_id)

#     # Проверяем, если есть сообщение, на которое идет ответ, и оно не пустое
#     if message.reply_to_message is not None:
#         bot.delete_message(user_id, message.reply_to_message.message_id)


# # Обработка подтверждения или отклонения оплаты админом
# @bot.callback_query_handler(func=lambda call: call.data.startswith('confirm_') or call.data.startswith('decline_'))
# def handle_admin_action(call):
#     user_id = call.data.split('_')[-1]

#     invite_link = create_one_time_invite_link()

#     if call.data.startswith('confirm_'):
#         # Подтверждение оплаты
#         cursor.execute('UPDATE users SET subscription_status = ? WHERE user_id = ?', ('Подтверждено', user_id))
#         conn.commit()
        
#         # Отправка ссылки на канал пользователю
#         bot.send_message(user_id, f"✅ Оплата подтверждена! 🎉\n\n🔗 Вот ссылка на канал: {invite_link}\n\nДобро пожаловать и приятного просмотра! 💫")
#         bot.send_message(ADMIN_ID, f"Оплата пользователя {user_id} подтверждена.")
    
#     elif call.data.startswith('decline_'):
#         # Запрос причины отказа
#         bot.send_message(call.message.chat.id, "Пожалуйста, укажите причину отклонения.")
#         bot.register_next_step_handler(call.message, lambda msg: handle_decline_reason(msg, user_id))

# def handle_decline_reason(message, user_id):
#     reason = message.text
#     bot.send_message(user_id, f"Ваша оплата была отклонена по следующей причине: {reason}.")
#     bot.send_message(ADMIN_ID, f"Оплата пользователя {user_id} отклонена по причине: {reason}.")

# db_path = "C:\\Users\\anm24\\Desktop\\test\\subscriptions.db"    

# def get_subscribed_users(db_path):
#     """Функция для получения всех пользователей с активной подпиской"""
#     connection = sqlite3.connect(db_path)
#     cursor = connection.cursor()
    
#     # Предполагаем, что в таблице users есть поле subscription_status (1 - подписан, 0 - нет)
#     cursor.execute("SELECT user_id FROM users WHERE subscription_status = 'Подтверждено'")
#     users = cursor.fetchall()
    
#     connection.close()
    
#     # Возвращаем список user_id
#     return [user[0] for user in users]

# def send_message_to_all_subscribers(message, db_path):
#     """Функция для рассылки сообщения всем подписанным пользователям"""
#     users = get_subscribed_users(db_path)
    
#     for user_id in users:
#         try:
#             bot.send_message(user_id, message)
#         except Exception as e:
#             print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")

# # Команда для рассылки сообщений администратором
# @bot.message_handler(func=lambda message: message.text == "📨 Отправить рассылку")
# def handle_send_to_all(message):
#     if str(message.chat.id) == ADMIN_ID:  # Проверка, что это администратор
#         # Создаем клавиатуру с кнопками выбора типа рассылки
#         markup = types.InlineKeyboardMarkup()
#         button1 = types.InlineKeyboardButton("Прямой эфир", callback_data="live")
#         button2 = types.InlineKeyboardButton("Важная инфа", callback_data="important")
#         button3 = types.InlineKeyboardButton("Новое предложение", callback_data="offer")
#         markup.add(button1, button2, button3)
        
#         bot.send_message(message.chat.id, "Выберите тип рассылки:", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Эта команда доступна только администратору.")

# # Обработка нажатия кнопок
# @bot.callback_query_handler(func=lambda call: call.data in ["live", "important", "offer"])
# def handle_broadcast_type(call):
#     broadcast_type = call.data  # Получаем выбранный тип рассылки

#     if broadcast_type == "live":
#         bot.send_message(call.message.chat.id, "Введите тему прямого эфира:")
#         bot.register_next_step_handler(call.message, lambda msg: ask_for_live_date(msg))

#     elif broadcast_type == "important":
#         bot.send_message(call.message.chat.id, "Вы выбрали Важную информацию. Введите текст сообщения для рассылки:")
#         bot.register_next_step_handler(call.message, lambda msg: process_admin_message(msg, "important"))

#     elif broadcast_type == "offer":
#         bot.send_message(call.message.chat.id, "Вы выбрали Новое предложение. Введите текст предложения:")
#         bot.register_next_step_handler(call.message, lambda msg: process_admin_message(msg, "offer"))

# def ask_for_live_date(message):
#     live_theme = message.text
#     bot.send_message(message.chat.id, "Введите дату прямого эфира:")
#     bot.register_next_step_handler(message, lambda msg: ask_for_live_time(msg, live_theme))

# def ask_for_live_time(message, live_theme):
#     live_date = message.text
#     bot.send_message(message.chat.id, "Введите время прямого эфира:")
#     bot.register_next_step_handler(message, lambda msg: process_live_broadcast(msg, live_theme, live_date))

# def process_live_broadcast(message, live_theme, live_date):
#     live_time = message.text
#     db_path = "C:\\Users\\anm24\\Desktop\\test\\subscriptions.db"  # Путь к базе данных

#     # Шаблон для прямого эфира
#     live_broadcast_message = f"""
# 📢 Прямой эфир! 

# 🎙 **Тема**: {live_theme}
# 📅 **Дата**: {live_date}
# 🕒 **Время**: {live_time}

# Подключайтесь к эфиру и задавайте вопросы!
#     """

#     send_message_to_all_subscribers(live_broadcast_message, db_path)
#     bot.send_message(message.chat.id, "Сообщение о прямом эфире отправлено всем подписанным пользователям.")

# def process_admin_message(message, broadcast_type):
#     admin_message = message.text
#     db_path = "C:\\Users\\anm24\\Desktop\\test\\subscriptions.db"  # Путь к базе данных

#     # В зависимости от типа рассылки, формируем сообщение
#     if broadcast_type == "important":
#         message_to_send = f"🔔 **Важная информация**: {admin_message}"
#     elif broadcast_type == "offer":
#         message_to_send = f"💡 **Новое предложение**: {admin_message}"

#     send_message_to_all_subscribers(message_to_send, db_path)
#     bot.send_message(message.chat.id, f"Сообщение отправлено всем подписанным пользователям (Тип: {broadcast_type}).")

# def send_message_to_all_subscribers(message, db_path):
#     """Функция для рассылки сообщения всем подписанным пользователям"""
#     users = get_subscribed_users(db_path)
    
#     for user_id in users:
#         try:
#             bot.send_message(user_id, message, parse_mode='Markdown')
#         except Exception as e:
#             print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")





# db_path = "C:\\Users\\anm24\\Desktop\\test\\subscriptions.db"    

# def get_unsubscribed_users(db_path):
#     """Функция для получения всех пользователей с отмененной подпиской"""
#     connection = sqlite3.connect(db_path)
#     cursor = connection.cursor()
    
#     # Предполагаем, что в таблице users есть поле subscription_status ('Подтверждено' или 'Отменена')
#     cursor.execute("SELECT user_id FROM users WHERE subscription_status = 'Отменена'")
#     users = cursor.fetchall()
    
#     connection.close()
    
#     # Возвращаем список user_id
#     return [user[0] for user in users]

# def send_message_to_unsubscribed_users(message, db_path):
#     """Функция для рассылки сообщения всем пользователям с отмененной подпиской"""
#     users = get_unsubscribed_users(db_path)
    
#     for user_id in users:
#         try:
#             bot.send_message(user_id, message)
#         except Exception as e:
#             print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")

# # Команда для рассылки сообщений пользователям с отмененной подпиской администратором
# @bot.message_handler(func=lambda message: message.text == "📨 Отправить рассылку отмененным")
# def handle_send_to_unsubscribed(message):
#     if str(message.chat.id) == ADMIN_ID:  # Проверка, что это администратор
#         # Создаем клавиатуру с кнопками выбора типа рассылки для отмененных подписок
#         markup = types.InlineKeyboardMarkup()
#         button1 = types.InlineKeyboardButton("Прямой эфир", callback_data="live_unsub")
#         button2 = types.InlineKeyboardButton("Важная инфа", callback_data="important_unsub")
#         button3 = types.InlineKeyboardButton("Новое предложение", callback_data="offer_unsub")
#         markup.add(button1, button2, button3)
        
#         bot.send_message(message.chat.id, "Выберите тип рассылки для пользователей с отмененной подпиской:", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, "Эта команда доступна только администратору.")

# # Обработка нажатия кнопок для отмененных подписок
# @bot.callback_query_handler(func=lambda call: call.data in ["live_unsub", "important_unsub", "offer_unsub"])
# def handle_unsub_broadcast_type(call):
#     broadcast_type = call.data  # Получаем выбранный тип рассылки

#     if broadcast_type == "live_unsub":
#         bot.send_message(call.message.chat.id, "Введите тему прямого эфира для пользователей с отмененной подпиской:")
#         bot.register_next_step_handler(call.message, lambda msg: ask_for_live_date_unsub(msg))

#     elif broadcast_type == "important_unsub":
#         bot.send_message(call.message.chat.id, "Введите текст важной информации для пользователей с отмененной подпиской:")
#         bot.register_next_step_handler(call.message, lambda msg: process_unsub_message(msg, "important_unsub"))

#     elif broadcast_type == "offer_unsub":
#         bot.send_message(call.message.chat.id, "Введите текст предложения для пользователей с отмененной подпиской:")
#         bot.register_next_step_handler(call.message, lambda msg: process_unsub_message(msg, "offer_unsub"))

# # Обработка прямого эфира для отмененных подписок
# def ask_for_live_date_unsub(message):
#     live_theme = message.text
#     bot.send_message(message.chat.id, "Введите дату прямого эфира:")
#     bot.register_next_step_handler(message, lambda msg: ask_for_live_time_unsub(msg, live_theme))

# def ask_for_live_time_unsub(message, live_theme):
#     live_date = message.text
#     bot.send_message(message.chat.id, "Введите время прямого эфира:")
#     bot.register_next_step_handler(message, lambda msg: process_live_broadcast_unsub(msg, live_theme, live_date))

# def process_live_broadcast_unsub(message, live_theme, live_date):
#     live_time = message.text
#     db_path = "C:\\Users\\anm24\\Desktop\\test\\subscriptions.db"  # Путь к базе данных

#     # Шаблон для прямого эфира
#     live_broadcast_message = f"""
# 📢 Прямой эфир! 

# 🎙 **Тема**: {live_theme}
# 📅 **Дата**: {live_date}
# 🕒 **Время**: {live_time}

# Подключайтесь к эфиру и задавайте вопросы!
#     """

#     send_message_to_unsubscribed_users(live_broadcast_message, db_path)
#     bot.send_message(message.chat.id, "Сообщение о прямом эфире отправлено всем пользователям с отмененной подпиской.")

# def process_unsub_message(message, broadcast_type):
#     admin_message = message.text
#     db_path = "C:\\Users\\anm24\\Desktop\\test\\subscriptions.db"  # Путь к базе данных

#     # В зависимости от типа рассылки, формируем сообщение
#     if broadcast_type == "important_unsub":
#         message_to_send = f"🔔 **Важная информация** (Отменена подписка): {admin_message}"
#     elif broadcast_type == "offer_unsub":
#         message_to_send = f"💡 **Новое предложение** (Отменена подписка): {admin_message}"

#     send_message_to_unsubscribed_users(message_to_send, db_path)
#     bot.send_message(message.chat.id, f"Сообщение отправлено всем пользователям с отмененной подпиской (Тип: {broadcast_type}).")

# def send_message_to_unsubscribed_users(message, db_path):
#     """Функция для рассылки сообщения всем пользователям с отмененной подпиской"""
#     users = get_unsubscribed_users(db_path)
    
#     for user_id in users:
#         try:
#             bot.send_message(user_id, message, parse_mode='Markdown')
#         except Exception as e:
#             print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")










# def check_subscription_expiry():
#     while True:
#         # Извлекаем пользователей с активной подпиской
#         cursor.execute('SELECT user_id, subscription_type, subscription_start_date FROM users WHERE subscription_status = "Подтверждено"')
#         users = cursor.fetchall()

#         if users:
#             for user in users:
#                 user_id, subscription_type, subscription_start_date = user
#                 start_date = datetime.strptime(subscription_start_date, '%Y-%m-%d %H:%M:%S')

#                 # Рассчитываем сколько прошло времени с начала подписки
#                 days_passed = (datetime.now() - start_date).days
#                 hours_passed = (datetime.now() - start_date).seconds // 3600

#                 if "1 месяц" in subscription_type:
#                     total_days = 30
#                 elif "6 месяцев" in subscription_type:
#                     total_days = 180
#                 elif "12 месяцев" in subscription_type:
#                     total_days = 365
#                 else:
#                     total_days = 0

#                 days_remaining = total_days - days_passed
#                 hours_remaining = (24 - hours_passed) if days_remaining == 0 else None

#                 # Отправляем уведомления за 3 дня, 1 день и за 1 час до конца подписки
#                 if days_remaining == 3:
#                     send_expiry_warning(user_id, days_remaining)
#                 elif days_remaining == 1:
#                     send_expiry_warning(user_id, days_remaining)
#                 elif days_remaining == 0 and hours_remaining == 1:
#                     send_expiry_warning(user_id, hours_remaining, time_type="hour")

#         # Проверка раз в час
#         time.sleep(3600)

# # Функция для отправки уведомлений
# def send_expiry_warning(user_id, time_remaining, time_type="days"):
#     if time_type == "days":
#         bot.send_message(user_id, f"Ваша подписка истекает через {time_remaining} дней! Не забудьте продлить подписку.", reply_markup=create_extend_button())
#     elif time_type == "hour":
#         bot.send_message(user_id, f"Ваша подписка истекает через {time_remaining} час! Не забудьте продлить подписку.", reply_markup=create_extend_button())

# # Функция для создания кнопки "Продлить подписку"
# def create_extend_button():
#     markup = types.InlineKeyboardMarkup()
#     extend_button = types.InlineKeyboardButton("Продлить подписку", callback_data="extend_subscription")
#     markup.add(extend_button)
#     return markup

# # Запуск потока для проверки подписок
# def start_subscription_checker():
#     checker_thread = threading.Thread(target=check_subscription_expiry)
#     checker_thread.daemon = True
#     checker_thread.start()

# def create_one_time_invite_link():
#     try:
#         # Используем метод createChatInviteLink для создания одноразовой ссылки
#         invite_link = bot.create_chat_invite_link(
#             chat_id=CHANNEL_ID,
#             expire_date=None,         # Ссылка не будет иметь временных ограничений
#             member_limit=1            # Одноразовая ссылка (разрешено только 1 использование)
#         )
#         return invite_link.invite_link
#     except Exception as e:
#         bot.send_message(ADMIN_ID, f"Ошибка при создании ссылки для канала: {e}")
#         return None

# @bot.message_handler(commands=['get_channel_id'])
# def get_channel_id(message):
#     if str(message.chat.id) == ADMIN_ID:
#         # Укажите приглашение на канал вместо username
#         invite_link = 'https://t.me/+3mVzZ157h49kY2Zi'  # ваша ссылка приглашения
#         try:
#             chat_info = bot.get_chat(invite_link)
#             bot.send_message(message.chat.id, f"ID вашего канала: {chat_info.id}")
#         except Exception as e:
#             bot.send_message(message.chat.id, f"Произошла ошибка: {e}")
#     else:
#         bot.send_message(message.chat.id, "Эта команда доступна только администратору.")

# # Запуск бота
# if __name__ == "__main__":
#     start_subscription_checker()  # Запуск проверки подписок
#     bot.polling()