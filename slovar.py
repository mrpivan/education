Возьмём список контактов бабушки. Для простоты рассмотрим его небольшую часть:

names = ["Маруся", "Олег Вереницын", "Доча"]

logins = ['@marusya_1954', '@el_baton', '+74017017189'] 

В names записаны понятные бабушке имена контактов, а в logins — их соответствующие логины в мессенджере.
  
Допустим, мы хотим определить имя человека с логином @el_baton. Но как нам соединить эти два списка, чтобы связать каждое имя с соответствующим логином?

Например, мы можем перебирать индексы от 0 до 2 и проверять, равен ли логин по текущему индексу и строка @el_baton. Если да, то можем вывести соответствующее имя из списка names по текущему индексу.
Не переживай, если текст выше сложно понять — лучше посмотри, как это выглядит в коде. Иногда код понять легче, чем текст!


names = ["Маруся", "Олег Вереницын", "Доча"]
logins = ['@marusya_1954', '@el_baton', '+74017017189']

search_login = "@el_baton"
for i in [0, 1, 2]: # проходим по индексам списка logins
    if logins[i] == search_login:
        print(names[i])


Если телефонная книга длинная, то можно заменить [0, 1, 2] на range(len(logins))— это простой способ пройтись по всем индексам списка:

names = ["Маруся", "Олег Вереницын", "Доча"]

logins = ['@marusya_1954', '@el_baton', '+74017017189']

search_login = "@el_baton"

for i in range(len(logins)): # проходим по индексам списка logins

    if logins[i] == search_login:

        print(names[i])


Отлично! Задача решена. Но для этого нам пришлось написать непростую программу, и, чтобы найти логин в списке, нужно перебрать его целиком. 
Введение в словари
В Python существует более эффективное решение подобных задач — при помощи словарей. Словарь — это специальная структура данных, которая позволяет связать одни значения (логины) с другими (именами). Вот как это выглядит:

contacts = {
    '@marusya_1954': 'Маруся', 
    '@el_baton': 'Олег Вереницын', 
    '+74017017189': 'Доча'
} 

Теперь мы можем легко найти имя по логину, используя логин в качестве индекса в списке:

contacts = {
    '@marusya_1954': 'Маруся', 
    '@el_baton': 'Олег Вереницын', 
    '+74017017189': 'Доча'
}
search_login = "@el_baton"

print(contacts[search_login])
# или сразу:

print(contacts["@el_baton"])
Синтаксис и термины
Давай посмотрим на словарь ближе. 
Как видишь, мы создали его перечислением через запятую пар "логин": "имя". 
Первый элемент пары (здесь это «логин») называют ключом, а второй (здесь это «имя») — значением. 
После создания словаря мы можем по ключу получать соответствующее ему значение, используя ключ просто как индекс в списке: contacts["@marusya_1954"].  При этом ключ должен быть уникальным: в одном словаре не может быть двух одинаковых ключей.






  Но использовать значение для поиска ключа не получится — программа выдаст ошибку:

contacts = {
    '@marusya_1954': 'Маруся', 
    '@el_baton': 'Олег Вереницын', 
    '+74017017189': 'Доча'
}
print(contacts["Маруся"])


Всё потому, что словарь позволяет получить значение по ключу, но не наоборот.
  
Что же, пора попрактиковаться

У Дяди Толи есть свой магазинчик волшебных предметов. Он захотел перенести его в онлайн, чтобы клиенты могли покупать волшебные предметы, не выходя из дома. 
Для первого шага сделай программу, которая по названию предмета выведет его стоимость. Используй словарь, где ключами будут названия предметов, а значениями — 
их стоимость.

Дядя Толя любезно предоставил таблицу цен:

Название предмета	Стоимость (золотых)

Цветастая кальянка	50

Магический сандалфон	100

Зелье радужной глыбы	200

Волшебный коврик для медитации	75

Создай словарь с ценами предметов shop и выведи стоимость предмета из переменной item.





item = "Волшебный коврик для медитации"

# твой код






















Но использовать значение для поиска ключа не получится — программа выдаст ошибку:

contacts = {
    '@marusya_1954': 'Маруся', 
    '@el_baton': 'Олег Вереницын', 
    '+74017017189': 'Доча'
}
print(contacts["Маруся"])



Всё потому, что словарь позволяет получить значение по ключу, но не наоборот.
  
Что же, пора попрактиковаться!

У Дяди Толи есть свой магазинчик волшебных предметов. Он захотел перенести его в онлайн, чтобы клиенты могли покупать волшебные предметы, не выходя из дома. 

Для первого шага сделай программу, которая по названию предмета выведет его стоимость. 
Используй словарь, где ключами будут названия предметов, а значениями — их стоимость.

Дядя Толя любезно предоставил таблицу цен:

Название предмета	Стоимость (золотых)

Цветастая кальянка	50

Магический сандалфон	100

Зелье радужной глыбы	200

Волшебный коврик для медитации	75

Создай словарь с ценами предметов shop и выведи стоимость предмета из переменной item.




  Подробнее про ключи
Ключами в словарях могут быть не только строки. 
  
Возможно, ты знаешь, что в некоторые школы ученики заходят по специальной карточке-пропуску с номером. 

Соответственно, где-то в этой системе работает программа, которая по номеру пропуска определяет, что это за ребёнок, и проверяет, есть ли он в базе.

  
children = {
    691203: "Ежов Вячеслав Геннадьевич",
    323146: "Клязина Анна Анатольевна",
    892841: "Ким Надежда Константиновна"
    # ... и так далее
} 

В таком случае ключом выступает int. Также ключом может быть float. А вот список ключом быть не может:

d = {
    [0, 1] : "один элемент",
    [6, 4, 3] : "другой элемент"
} 

Программа выдаст ошибку. Дело в том, что в Python ключи словаря могут быть только неизменяемыми.

Вспомни: в уроке про списки, обсуждая отличия между списками и строками, мы говорили, что можно изменить элемент списка, но нельзя изменить элемент строки.

Словарь обращает на это внимание и выдаёт ошибку, если ключ можно изменять.


  Ключами словаря могут быть строки и числа, но не могут быть списки и другие словари.

Теперь давай решим ещё одну задачку для Дяди Толи. Кто ему поможет, если не ты?

Теперь ему нужно сделать автоматический подсчёт стоимости покупок клиента. 
В списке goods указаны товары в корзине покупателя. Твоя программа должна вывести суммарную стоимость всех этих товаров.
Давай подумаем, как это сделать. Представим на минутку, что вместо словаря с ценами у нас обычная таблица, 
записанная, например, в тетради, в которой можно посмотреть цену любого товара. 

Чтобы посчитать стоимость всех покупок, лежащих в чьей-то корзине (в нашем случае - перечисленных в переменной goods), 
мы должны будем найти название каждого товара в таблице, посмотреть, сколько он стоит, и прибавить это число к общей стоимости. 
Несложно, правда? А теперь вместо таблицы можно использовать словарь shop. На самом деле, это даже удобнее - вместо того, 
чтобы искать название и цену товара вручную, мы можем получить её сразу. Например, для волшебного коврика это будет выглядеть так:

shop["Волшебный коврик для медитации"] # Результат - 75 

Вот и всё! Дело за малым: с помощью цикла нужно перебрать все товары из переменной goods, суммируя их стоимость.
  
Важная подсказка: магазинчик начал использовать программу совсем недавно, и ещё не все товары добавлены в словарь. 
Чтобы избежать ошибки, перед обращением к элементу словаря стоит проверить, что он там есть:
"Волшебный коврик для медитации" in shop # Результат - True
"Алмазное солнце" in shop # Результат - False 


shop = {
    "Цветастая кальянка":	50,
    "Магический сандалфон":	100,
    "Зелье радужной глыбы":	200,
    "Волшебный коврик для медитации":	75
}

goods = ["Волшебный коврик для медитации", "Цветастая кальянка", "Цветастая кальянка"]













total_cost = 0
shop = {
    "Цветастая кальянка": 50,
    "Магический сандалфон": 100,
    "Зелье радужной глыбы": 200,
    "Волшебный коврик для медитации": 75
}

goods = ["Волшебный коврик для медитации", "Цветастая кальянка", "Цветастая кальянка"]

for item in goods:
    total_cost += shop[item]

print(total_cost)
