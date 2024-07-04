import telebot
 
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
 
from data_base import load_user_data, save_user_data
 

 

 
token = "6543125611:AAEW1FHNiY04kevt8ZS9B4jumMRewSXp2JU"
 
bot = telebot.TeleBot(token=token)
 

 
questions_list = [
 
    "Тебе нравятся бобры?",
 
    "Тебе нравятся на вкус деревья?",
 
    "Ты бы хотел стать бобром?",
 
    "У тебя были мысли о том, чтобы построить плотину?",
 
    "Ты человек?"
 
]
 

 
answers_list = [
 
    ["Да", "Нет", "Очень"],
 
    ["Когда то пробывал", "Ты дурак?", "Грызу каждый день"],
 
    ["Римская империя?", "Никогда", "Каждый день думаю"],
 
    ["Я не знаю", "Да", "Нет конечно"],
 
    ["Нет", "Естественно", "Я бобер"]
 
]
 

 
score_list = [2, 0, 3]
 

 
user_data = {}
 

 
DATA_PATH = 'users_data.json'
 

 

 
def markup_create(answers):
 
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
 
    for ans in answers:
 
        markup.add(KeyboardButton(ans))
 
    return markup
 

 

 
@bot.message_handler(commands=["start"])
 
def start(message):
 
    user_id = str(message.from_user.id)
 
    user_data[user_id] = {  # инициализируем словарь для нового пользователя, который нажал /start
 
        'index': 0,
 
        'score': 0
 
    }
 
    # сразу после того как изменили словарь user_data - надо сохранять его, чтобы не потерять данные
 
    save_user_data(user_data, DATA_PATH)
 
    bot.send_message(message.chat.id, "Тест на бобровость:\n")
 
    ask_question(message, 0)  # передаем индекс 0, потому что посе команды /start всегда начинаем с первого вопроса
 

 

 
def ask_question(message, idx):
 
    question = questions_list[idx]
 
    answers = answers_list[idx]
 
    msg = f"Вопрос {idx+1} из {len(questions_list)}: {question}\n"
 
    markup = markup_create(answers)
 
    bot.send_message(message.chat.id, msg, reply_markup=markup)
 
    bot.register_next_step_handler(message, processing_user_response, idx)
 

 

 
def processing_user_response(message, idx):
 
    user_id = str(message.from_user.id)
 
    user_data = load_user_data(DATA_PATH)  # загружаем данные пользователей
 
    answer_idx = answers_list[idx].index(message.text)  # получаем индекс ответа, который дал пользоватлеь, в списке ответов (0, 1 или 2)
 
    user_data[user_id]["score"] += score_list[answer_idx]  # записываем балл, соответствующий ответу пользователя в user_data
 
    user_data[user_id]["index"] += 1
 
    save_user_data(user_data, DATA_PATH)
 
    if idx < len(questions_list) - 1:  # если следующий вопрос ещё есть, то задаем его
 
        ask_question(message, idx+1)
 
    else:  # если этот вопрос был последним - выводим результат
 
        show_res(message)
 

 

 
def show_res(message):
 
    user_id = str(message.from_user.id)
 
    user_data = load_user_data(DATA_PATH)
 
    score = user_data[user_id]['score']
 
    percent = round(score / 15, 2) * 100
 
    bot.send_message(message.chat.id, f"Вы бобер на: {percent}%")
 
    bot.send_message(message.chat.id, "Чтобы пройти тест снова - /start")
 

 

 
bot.polling() 
