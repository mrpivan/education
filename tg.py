Как и у других веб-сервисов, у Telegram есть свой API, который используют все Telegram-приложения: мобильные, компьютерные и даже браузерные. 
Когда ты отправляешь сообщение, приложение Telegram на твоём устройстве обращается к API телеграма. На специальный адрес приходит текст сообщения и дополнительная информация. 
Сервер Telegram принимает сообщение, сохраняет его в файл c историей беседы и ещё одним запросом отправляет это сообщение на телефон собеседника.
Получается, что это веб-сервис со своим API, с помощью которого можно посылать и принимать сообщения, изменять информацию об аккаунте (аватарку, описание и прочее) и даже создавать новые аккаунты. 
Всё это можно делать через код, что позволяет создавать программы, которые самостоятельно общаются с людьми. Это и есть боты. Давай поговорим про них подробнее.

Аккаунты телеграм-ботов
Боты в Telegram — это специальный тип аккаунтов, которые могут, как и люди, отсылать сообщения пользователям, иметь аватарку и описание. 
Чтобы пользователи отличали чат-ботов от аккаунтов людей, для бот-аккаунтов установлены ограничения. 
Вот некоторые из них:

Имя бота должно оканчиваться на bot или Bot, например @bot или @MisterRobot.
  
У ботов нет статуса последнего посещения, вместо него выводится надпись «бот».

Бот не может «постучаться» к другому пользователю и первым начать диалог: он должен скромно сидеть и ждать, пока кто-нибудь обратит на него внимание и напишет первым.
Для управления ботами в Telegram есть даже отдельный Bot API. Документация по Bot API опубликована здесь. 
Как мы уже говорили, программа, управляющая ботом, взаимодействует с Bot API через HTTP-запросы. 
Их можно отправлять как с помощью Python-библиотеки requests, так и посредством специальных библиотек-обёрток.
Но прежде чем управлять ботом, нужно его создать. Как и человеку, сначала боту нужно зарегистрироваться в приложении. 

Создаём аккаунт Telegram-бота
В Telegram есть специальный бот для регистрации новых ботов — @BotFather. Его имя не случайно нарушает правила наименования ботов: его создали разработчики 
Telegram, а у них есть возможность обойти установленные правила. Особенно если нужно создать прародителя ботов!
Открой приложение Telegram и найди бота @BotFather: в окно поиска над списком контактов нужно ввести его имя. 
Обрати внимание на иконку возле имени бота: белая галочка на голубом фоне. Эту иконку устанавливают администраторы 
Telegram, она означает, что бот настоящий, а не просто носит похожее имя (в системе может существовать несколько ботов с одинаковыми названиями). 

Регистрируем бота

Начни диалог с ботом @BotFather, нажав кнопку Start («Запустить»). 
Затем отправь команду /newbot и укажи параметры нового бота:
имя (на любом языке), под которым твой бот будет отображаться в списке контактов;
техническое имя бота, по которому его можно будет найти в Telegram. 
Имя должно оканчиваться на слово bot в любом регистре, например Kittybot, kitty_bot или даже your_login_assistant_bot. Имена ботов должны быть уникальны.
Супер! Аккаунт для твоего бота создан. @BotFather поздравит тебя и отправит в чат токен для работы с Bot API. 

  Токен выглядит примерно так: 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11.

Да, это тот самый токен, который нужен, чтобы сервер мог опознать тебя при обращении по API — без него управлять ботом не выйдет. 

Токен нужен, чтобы управлять ботом мог только ты. Это своего рода пароль, который знает только создатель бота и по которому Telegram поймёт, имеешь ли ты право управлять ботом или нет.
По твоему запросу @BotFather может отозвать токен (отправь ему команду /revoke) и сгенерировать новый.
В любой непонятной ситуации выполняй команду /help, и @BotFather покажет, на что он способен 😉.
  
Настройка аккаунта бота

Настроить аккаунт бота можно через @BotFather. 

Отправь команду /mybots. В ответ ты получишь список ботов, которыми ты уже управляешь (возможно, в этом списке пока есть лишь один). 
Укажи бота, которого хочешь отредактировать, и нажми кнопку Edit Bot. 
Ты можешь изменить:

Имя бота (Edit Name)
Описание (Edit Description) — текст, который пользователи увидят в самом начале диалога с ботом под заголовком «Что может делать этот бот?»
Общую информацию (Edit About) — текст, который будет виден в профиле бота
Картинку-аватар (Edit Botpic)
Команды (Edit Commands) — подсказки для ввода команд

Не пожалей времени и заполни все поля — тогда пользователям будет приятнее и проще работать с ботом. 
Дальше ты можешь указать свои контакты в описании, и не забудь про аватар: с ним бота будет проще отличить от других чатов в списке.




БОТ попугай

В этом уроке ты узнаешь, как научить бота отвечать на команды и обрабатывать сообщения пользователей.
Добавляем реакцию
Самое простое, что мы можем сделать, — это научить бота отвечать на сообщения, какими бы они ни были, каждый раз, когда они приходят. 
Давай заглянем в документацию библиотеки telebot. В разделе «Быстрый старт» собраны подходящие примеры для решения этой задачи. 

Мы можем скопировать код одного из них и запустить на своём компьютере:

import telebot

token='наш токен'
bot=telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def repeat_message(message): # Функция для обработки сообщений
      bot.send_message(message.chat.id, message.text) # Отправка ответа

bot.polling() 


Рассмотрим этот код построчно. 

Сначала мы импортируем библиотеку telebot.

В следующей паре строк указываем токен, без которого бот не сможет работать в телеграме. 
  
Потом идёт какая-то странная запись, начинающаяся с символа @, — к ней мы вернёмся позже.

После мы видим функцию repeat_message(), которая определяет, что именно должен сделать бот, когда получит сообщение. 
  
Она принимает параметр message, который содержит информацию о полученном сообщении: идентификатор чата, имя отправителя, сам текст и многое другое. 
Эта функция выполняет всего одно действие — посылает пользователю ответное сообщение с помощью команды bot.send_message().

В её параметрах должны быть указаны идентификатор чата и текст ответа. В этом примере бот отправляет пользователю текст из его же сообщения, то есть просто повторяет за ним.
Команда bot.polling() нужна для запуска бота. После неё он будет готов принимать входящие сообщения и отвечать на них. 
С кодом, кажется, всё понятно. Теперь можно вернуться к непонятной строке: @bot.message_handler(content_types=['text']). 

Здесь используется особый вид функции, который может влиять на работу других функций, — декоратор. Он может, например, сделать так, чтобы функция вызывалась лишь при выполнении определённого условия. 
Имя декоратора всегда начинается с символа @ и записывается перед объявлением функции:

@decorator(parameters) 
def function():
    # Тело функции 
  
В скобках ему можно передать нужные параметры — точно так же, как для любых других функций.
  
В нашем примере декоратор называется message_handler. Именно он отслеживает входящие сообщения и делает так, чтобы в ответ вызывалась функция repeat_message().

@bot.message_handler(content_types=['text'])
def repeat_message(message): # Функция для обработки сообщений
      bot.send_message(message.chat.id, message.text) # Отправка ответа 
  
Как видишь, декоратор имеет параметр content_types, которому передаётся значение ['text']. Чуть позже мы рассмотрим параметры message_handler подробнее, а пока время размяться!




Учим бота различать запросы

Чтобы наш бот был интерактивным и интересным, он должен обрабатывать входящие сообщения по-разному. 

Например, отвечать приветствием на команду /start и выводить справку о себе в ответ на команду /help.

Проще говоря, на разные сообщения должны вызываться разные функции. И, конечно же, библиотека telebot даёт нам это провернуть. 
Вернёмся к нашему примеру:
@bot.message_handler(content_types=['text'])
def repeat_message(message):
    bot.send_message(message.chat.id, message.text) 
Подсказкой служит название параметра декоратора — content_types. Оно переводится как «тип содержимого». Этот параметр помогает различать сообщения по типу — будь то текст, картинка, аудиозапись или что-то ещё. 

Запись content_types=['text'] означает, что функция repeat_message() будет вызвана, только если придёт текстовое сообщение.


Параметры message_handler позволяют проанализировать содержимое сообщения и вызвать функцию для обработки только в том случае, если оно удовлетворяет заданному условию. 
Описание всех возможных параметров есть в документации библиотеки. Если мы перейдём на главную страницу, то увидим огромное оглавление с перечислением всех функций, доступных в библиотеке. 
Но, чтобы быстро найти информацию о message_handler, лучше воспользоваться поиском по странице. Для этого нажми одновременно клавиши Ctrl и F, а затем введи в появившемся окошке то, что мы хотим отыскать. 
Автоматический поиск укажет на нужный пункт в оглавлении, а там уже и подробное описание message_handler с примерами того, как эту функцию использовать.

  


Рассмотрим несколько её основных параметров более подробно.
  
content_types — фильтрует сообщения по типу содержимого. Принимает список с допустимыми форматами, среди которых могут быть text, photo, audio и другие.
  
# Пример: обработка только текстовых и голосовых сообщений
@bot.message_handler(content_types=['text', 'audio'])
def handle_text_audio(message):
    pass # это ключевое слово можно использовать, чтобы Python не ругался на пустую функцию 


commands — различает команды, записанные через /.

  
# Пример: обработка только команд '/start' и '/help'
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass 


func — позволяет указать функцию с нашим собственным фильтром, которая в зависимости от сообщения должна возвращать True или False.

  
# Функция для фильтрации сообщений: возвращает True, если длина сообщения меньше 100
def check_message_len(message):
    return len(message.text) <= 100
        
# Пример: обработка сообщений по длине с нашей собственной функцией
# Будут обработаны только короткие сообщения

@bot.message_handler(func=check_message_len)
def handle_text_doc(message):
    pass 








Как-то так. А теперь давай проверим, всё ли понятно.
Представь, что мы написали функцию, которая должна вызываться только в тех случаях, когда боту приходит либо текст, либо фотография. 
Выбери декоратор, с помощью которого это можно сделать.


@bot.message_handler(content_types=['text', 'photo']) 


@bot.message_handler(content_types=['text'])
@bot.message_handler(content_types=['photo']) 


@bot.message_handler(commands=['text', 'photo']) 



@bot.message_handler(func=filter_text_photo) 






++-+






Назови пароль!

Наверное, ты уже понял, насколько крут декоратор message_handler. 

С ним можно очень точно настраивать общение бота и пользователя, учитывая не только тип сообщения, но и его содержание.
Давай рассмотрим ещё один пример.

Представь, что мы сделали бота только для себя и запрещаем переписываться ему с кем-то ещё 🤐. 
Для этого надо научить его кодовой фразе — паролю, который должен быть в сообщении, чтобы бот на него ответил. Для примера возьмём пароль «хомяк».
Полный код бота приведён ниже.
  
import telebot

token='наш токен'
bot=telebot.TeleBot(token)

def filter_password(message):
    password = "хомяк"
    return password in message.text

@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
    bot.send_message(message.chat.id, "Привет!")

bot.polling() 


В этом примере телеграм-бот имеет полный доступ к сообщению пользователя, так что он может отвечать по-разному в зависимости от содержания сообщения.
Внимательно посмотри на код из примера и соотнеси каждый кусочек с тем, что он делает.





Подведём итоги
Теперь наш бот умеет не только присылать сообщения, но и ориентироваться в сообщениях пользователей! Уже сейчас ты можешь научить его делать крутые штуки — реагировать на команды, 
отвечать на вопросы и поддерживать беседу. 
Ещё теперь ты умеешь работать с декораторами и настраивать действия бота в зависимости от получаемых сообщений. 
А в следующих уроках наш бот научится работать с кнопками и станет ещё более продвинутым!


  



Техническое задание

Цель:

Разработать чат-бота в формате визитки для предоставления информации о выдуманном или реальном персонаже и для взаимодействия с пользователями.
Описание проекта:

Бот-визитка — это программа, способная предоставлять информацию о персонаже. 
Бот должен уметь общаться с пользователями, отвечать на запросы и предоставлять информацию (имя, возраст, хобби и т. д.).
Основные функции бота:

Стартовая команда (/start):

Приветственное сообщение и краткое описание бота
Предложение ознакомиться с доступными командами (/help)

Команда помощи (/help):

Справочная информация о доступных командах и их функциональности
Пояснения по использованию бота
Личная информация:

Бот должен предоставлять ключевую информацию о персонаже: имя, возраст, хобби, интересы и другие важные аспекты. 
Если бот — твоя собственная визитка, то добавь возможность прочитать про твои проекты, а если это игровой персонаж — про его навыки и т. п.

Другие функции бота:

Помимо команд, бот должен отвечать на сообщения пользователя
По желанию может быть реализована отправка фотографий или других медиафайлов по запросу пользователя*
  
Стиль общения:
  
Бот должен взаимодействовать с пользователями вежливо и дружелюбно
Обработка ошибок:
  
Код работает без ошибок.
  
Требования к интерфейсу:
  
Интерфейс бота должен быть интуитивно понятным и удобным
Пользователи должны легко находить интересующую их информацию
  
Ожидаемый результат:
  
Работающий бот-визитка





  Шаг 1: Анализ ТЗ
Первая строчка плана гласит:

📜 1. Проанализировать ТЗ, определить критерии успеха проекта

Определились с минимальным набором функций, который должен быть у твоего бота:
Есть команда /start
Есть команда /help
Есть возможность посмотреть информацию про персонажа
С этого и начнём!

💡 Дополнительные возможности можно будет добавить, когда основная часть будет готова и сработает безошибочно.
  
Шаг 2: Существующие решения



 2. Найти существующие решения и похожие проекты



Шаг 3: Необходимые инструменты

📜 3. Определить инструменты, необходимые для работы

Инструменты в этом случае — всё, что может понадобиться: язык, на котором будешь писать, редактор, в котором будешь работать, библиотеки, к которым предстоит обращаться.
Условимся, что мы пишем код на языке Python в редакторе PyCharm. А для бота будем использовать библиотеку telebot (pyTelegramBotAPI).

Шаг 4: Подзадачи
📜 4. Разбить задачи на подзадачи и составить план их решения

Наша задача — написать работающего бота с визиткой. 
Казалось бы, что тут можно разбить? Сейчас разберёмся.
Понимание структуры проекта
Представь, что тебе захочется сменить персонажа или дополнить информацию о нём. Придётся лезть в код и в куче мест менять параметры. 
Значит, твой код должен быть хорошо структурирован и удобочитаем, иначе в нём будет сложно разобраться спустя время и при необходимости доработать.


Когда мы решили, что за что отвечает и каким будет наполнение, 
можно представить сложность каждой части и сколько она займёт времени. 

Вот как может выглядеть начало плана по написанию ботовой части:

Создать новый токен в BotFather

Установить telebot

Из бота-попугая взять каркас бота, подставить туда новый токен

Запустить и проверить

Изменить команду /start под бота-визитку

Запустить и проверить

Изменить команду /help под бота-визитку

Запустить и проверить

Создать новую функцию /about

Запустить и проверить

И так далее. Надеемся, логика понятна. После описания плана действий можно приступать к разработке!
💡 Предварительное понимание структуры проекта — очень важный шаг в разработке.
Да, сейчас наш проект состоит из двух частей и можно запомнить, какая за что отвечает. 
Но в будущем число блоков будет расти, все они начнут взаимодействовать между собой, и удержать в голове, какая часть за что отвечает 
и как части друг с другом связаны, будет уже непросто.



import telebot



 
info = """Гендальф Серый\n
 
Возраст: около 2019 лет\n
 
Хобби: Изучение магии, сражения с темными силами, путешествия\n
 
Интересы: Забота о Средиземье, защита свободы народов
 
Чтобы получить его фотографию отправьте "/phgen"
 
"""
 

 
TOKEN = '6754826188:AAEid2Mzmx0uTSpTbRvkFlLn4ozYj54OVJw'
 
bot = telebot.TeleBot(TOKEN)
 

 
@bot.message_handler(commands=['start'])
 
def start_message(message):
 
    bot.send_message(message.chat.id, 'Привет! Я бот. Чем могу помочь?')
 

 
# Обработчик команды /help
 
@bot.message_handler(commands=['help'])
 
def help_message(message):
 
    text = '''Доступные комамнды
 
    /start - начать общение с ботом\n
 
    /help - получить помощь\n
 
    /info - получить информацию о Гендальфе Сером'''
 
    bot.send_message(message.chat.id, text)
 

 
# Обработчик команды /info
 
@bot.message_handler(commands=['info'])
 
def info_message(message):
 
    bot.send_message(message.chat.id, info)
 

 
# Обработчик текстовых сообщений
 
@bot.message_handler(func=lambda message: True)
 
def handle_text_messages(message):
 
    bot.send_message(message.chat.id, "Спасибо за сообщение!")
 

 
# Обработчик отправки фотографий
 
@bot.message_handler(content_types=['photo'])
 
def handle_photo(message):
    bot.send_message(message.chat.id, 'Красивая фотография!')
 

 
@bot.message_handler(commands=['phgen'])    
 
def send_character_photo(message):
  character_photo_path = "ggendalf.PNG"
  files = {'phgen': open(character_photo_path, 'rb')}
 
  bot.send_photo(message.chat.id, files['phgen'])
 

 

 

 
# Обработчик отправки медиафайлов
 
@bot.message_handler(content_types=['document', 'audio', 'voice', 'video'])
 
def handle_media(message):
 
    bot.send_message(message.chat.id, 'Спасибо за медиафайл!')
 
    
 

 
# Запускаем бота
 bot.polling()









Это теоретический урок. В нём ты узнаешь, как хранить данные о пользователе в программе. 


Хранение данных пользователя
Давай для примера рассмотрим простого бота, который спрашивает возраст и рекомендует компьютерную игру по команде /game. Попробуй запустить этот код у себя:



import telebot

# Создаём бота
API_TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Изначально возраст неизвестен, обозначим это как -1
age = -1

# Начало работы, спрашиваем возраст
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я умею рекомендовать игры.")
    bot.send_message(message.chat.id, "Пожалуйста, скажи, сколько тебе лет?")

# Если возраст уже указан, рекомендуем игру
@bot.message_handler(commands=['game'])
def game(message):
    # age == -1 значит, что возраст не указан
    if age == -1:
        bot.send_message(message.chat.id, "Пожалуйста, пришли сначала свой возраст.")
    elif age < 13:
        bot.send_message(message.chat.id, "Minecraft")
    elif 13 <= age < 18:
        bot.send_message(message.chat.id, "Baba Is You")
    else:
        bot.send_message(message.chat.id, "The Stanley Parable")

# Запоминаем присланный возраст
@bot.message_handler()
def save_age(message):
    # Проверяем, что возраст - число
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пожалуйста, пришли свой возраст цифрами.")
    else:
        # Запоминаем присланный возраст в глобальную переменную `age`, объявленную в начале программы
        global age
        age = int(message.text)
        user_data[name] = age
        bot.send_message(message.chat.id, "Отлично, я запомнил! Теперь можешь использовать команду /game")

# Запускаем бота
bot.polling() 


Самое интересное здесь происходит в функции save_age. 
Она срабатывает на все текстовые сообщения, кроме команд /start и /game, и проверяет, состоит ли сообщение из цифр. 
Затем функция записывает число из сообщения в переменную age. Это и есть память бота, в которой хранится информация о пользователе. 
Кстати, заметил_а в коде команду global age перед тем как записать возраст в age? Всё просто: она сообщает Python, ч
то мы хотим изменить уже существующую глобальную переменную age, а не создавать новую переменную внутри функции save_age.
Увы, всё не так просто. Представь, что твоим ботом пользуется сразу несколько человек. Можешь даже попросить кого-нибудь из друзей опробовать твоего бота и посмотреть, 
что получится.
Оказывается, переменная age — общая для всех пользователей. 
Возраст каждого нового пользователя будет записан в неё, тем самым меняя ответы бота для всех предыдущих пользователей. 



Используем словари для хранения данных
Чтобы решить эту проблему, можно использовать вместо переменной словарь:

# Создаем пустой словарь для хранения данных о пользователе
user_data = {} 

Теперь каждый раз, когда новый пользователь пишет свой возраст, можно добавлять в словарь пару (имя пользователя, возраст):

age = int(message.text) ----> age = int(message.text)
                              user_data[name] = age


Но что, если имена двух пользователей совпадут? Тогда возраст одного заменится возрастом другого, а значит, мы снова столкнёмся с той же проблемой 🤨.
  
Разработчики Telegram задумались об этом заранее, поэтому, кроме имени, у каждого пользователя есть специальный номер — user_id. 

Его ещё называют уникальным идентификатором: он привязан к конкретному юзеру и не может встретиться у кого-то ещё. 
Так что в боте лучше сохранять пары (user_id, возраст):


user_data[user_id] = age  


В процессе работы бота этот словарь будет выглядеть как-то так:

user_data = {
    123456789: 25,
    987654321: 12
} 
👉🏼 Получить user_id из сообщения пользователя в коде можно так: message.from_user.id



------------------------------


# Начало работы, спрашиваем возраст
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я умею рекомендовать игры.")
    bot.send_message(message.chat.id, "Пожалуйста, скажи, сколько тебе лет?")

# Если возраст уже указан, рекомендуем игру
@bot.message_handler(commands=['game'])
def game(message):
    # Получаем `user_id` пользователя
    user_id = message.from_user.id

        # Проверяем, что user_id пользователя есть в словаре
    # Если нет -- просим прислать свой возраст
    if user_id not in user_data:
        bot.send_message(message.chat.id, "Пожалуйста, пришли сначала свой возраст.")
    elif user_data[user_id] < 13:
        bot.send_message(message.chat.id, "Minecraft")
    elif 13 <= user_data[user_id] < 18:
        bot.send_message(message.chat.id, "Baba Is You")
    else:
        bot.send_message(message.chat.id, "The Stanley Parable")

# Запоминаем присланный возраст
@bot.message_handler()
def save_age(message):
    # Проверяем, что возраст - число
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пожалуйста, пришли свой возраст цифрами.")
    else:
        # Получаем `user_id` пользователя
        user_id = message.from_user.id

        # Запоминаем присланный возраст в локальную переменную `age`
        age = int(message.text)
        # Сохраняем возраст пользователя в словарь по `user_id`
        user_data[user_id] = age
        bot.send_message(message.chat.id, "Отлично, я запомнил! Теперь можешь использовать команду /game")

# Запускаем бота
bot.polling() 

-----------------------------------



Возникает вопрос: а почему здесь нет global user_data? Отвечаем: дело в том, что в этом коде мы не создаём новую переменную, 
а записываем значение в уже существующий словарь user_data. У Python не остаётся выбора, кроме как найти существующую переменную user_data и использовать её.
Если бы мы вместо записи по ключу просто пересоздавали словарь так: user_data = {user_id: int(message.text)}, 
то команда global user_data снова понадобилась бы.



Давай посмотрим, насколько ты хорошо понял_а проблему, с которой мы столкнулись, и её решение. Выбери все верные утверждения:


1/
Телеграм-боты могут хранить информацию только об одном пользователе-



2/
Когда мы записываем информацию о людях в одну переменную, возникает проблема: если приходит новый человек, его информация заменяет информацию о том, кто был раньше+



3/
Когда мы используем словари для хранения информации о пользователях, она хранится отдельно на каждого и не перезаписывается другими пользователями+


4/
Словари слишком сложны для хранения информации о пользователях, поэтому стоит хранить информацию в переменных-






-++-




Словари с набором значений

Иногда задачи требуют хранения большого количества данных. Это может быть возраст, имя или, например, количество использований бота. 
Тут тоже помогут словари, только вместо одного значения, как в прошлом примере, нужно сохранить набор значений. 
Для этого также удобно использовать словарь — можно дать явное название каждому из значений, чтобы не запутаться, например, age и name:

user_data = {
    123456789: {"age": 25, "name": "Анфиса"},
    987654321: {"age": 30, "name": "Кирилл"}
} 

Теперь по каждому пользователю есть не только одно значение, но целый словарь с данными. 
Так можно собрать сколько угодно информации о пользователе, просто добавляя её в словарик.
Вот как можно это реализовать:

Создаём для каждого нового пользователя пустой словарь после команды /start:

 if user_id not in user_data:
         user_data[user_id] = {}
  
Записываем в этот словарь возраст, указанный пользователем:

 user_data[user_id]['age'] = age
  
При желании добавляем другую инфу. Например, имя:

 user_data[user_id]['name'] = message.from_user.first_name


-----------------------------


import telebot

# Создаём бота
API_TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

# Изначально пользователей нет, пустой словарь
user_data = {}

# Начало работы, спрашиваем возраст
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я умею рекомендовать игры.")
    bot.send_message(message.chat.id, "Пожалуйста, скажи, сколько тебе лет?")

# Если возраст уже указан, рекомендуем игру
@bot.message_handler(commands=['game'])
def game(message):
    # Получаем `user_id` пользователя
    user_id = message.from_user.id

    # Проверяем, что user_id пользователя есть в словаре
    # Если нет -- просим прислать свой возраст
    if user_id not in user_data:
        bot.send_message(message.chat.id, "Пожалуйста, пришли сначала свой возраст.")
    elif user_data[user_id] < 13:
        bot.send_message(message.chat.id, "Minecraft")
    elif 13 <= user_data[user_id] < 18:
        bot.send_message(message.chat.id, "Baba Is You")
    else:
        bot.send_message(message.chat.id, "The Stanley Parable")

# Запоминаем присланный возраст
@bot.message_handler()
def save_age(message):
    # Проверяем, что возраст - число
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пожалуйста, пришли свой возраст цифрами.")
    else:
        # Получаем `user_id` пользователя
        user_id = message.from_user.id

        # Запоминаем присланный возраст в локальную переменную `age`
        age = int(message.text)
        # Сохраняем возраст пользователя в словарь по `user_id`
        user_data[user_id]['age'] = age
        # Сохраняем имя пользователя в словарь по `user_id`
        user_data[user_id]['name'] = message.from_user.first_name

        bot.send_message(message.chat.id, "Отлично, я запомнил! Теперь можешь использовать команду /game")

# Запускаем бота
bot.polling()
  
-------------------------------------


Подведём итоги
Использовать словари в телеграм-ботах очень удобно, особенно для хранения и обработки данных о пользователях. 
Словари позволяют разделить информацию о каждом пользователе. В результате ботом могут пользоваться сразу много людей, не нарушая его работу.
На следующих этапах разработки бота мы сможем расширить такой подход. 
Например, добавим новые ключи и значения для имени пользователя, предпочтений и других данных.
