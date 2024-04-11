import telebot
from telebot import types
import webbrowser

bot = telebot.TeleBot("7040983878:AAFHFmAm8LBL3_rk4e6O3E-XwcyLmLSnt4U")
print('Бот жив!')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🛜 Сайт", callback_data='Saut')
    markup.add(btn1)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}. Чтобы задать вопрос напишите '
                                      f'его или\nвыберете раздел из '
                                      'выпадающего списка ⬇️',
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    text = message.text
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🔙 В главное меню", callback_data='Main')
    markup.add(btn)
    bot.delete_message(message.chat.id, message.id - 1, 0)
    bot.send_message(message.chat.id,
                     "Ответ принят, ожидайте ответа в личные сообщения. Чтобы задать новый вопрос напишите его", reply_markup=markup)
    bot.send_message(5478441619, "Клиент пишет: [{}], ссылка на тг: [{} {}](tg://user?id={})"
                     .format(message.text, message.from_user.first_name,
                             message.from_user.last_name, message.from_user.id), disable_web_page_preview=True,
                     parse_mode="Markdown")

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'Main':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("🛜 Сайт", callback_data='Saut')
        markup.add(btn1)
        bot.delete_message(callback.message.chat.id, callback.message.id, 0)
        bot.send_message(callback.message.chat.id, 'Чтобы задать вопрос напишите '
                                          'его или\nвыберете раздел из '
                                          'выпадающего списка ⬇️',
                         reply_markup=markup)
        return

    elif callback.data == 'Saut':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("🔙 В главное меню", callback_data='Main')
        markup.add(btn)
        bot.delete_message(callback.message.chat.id, callback.message.id, 0)
        bot.send_message(callback.message.chat.id, 'Открываю', reply_markup=markup)
        webbrowser.open('https://sokolovskydental.clients.site')
        return



bot.polling(none_stop=True)