True и False в переменных


Вчера мы узнали, что логические выражения могут принимать одно из двух значений: True или False.  
Эти значения можно записывать в переменные:

is_cold = True 

Более того, в переменные можно вписывать и сами логические выражения (например, сравнения). 
А Python вычислит и подставит значение True или False в переменную:

temperature = 8
is_cold = temperature < 10  # is_cold будет равно True, т. к. температура меньше 10 

Здесь мы создали переменную is_cold с результатом сравнения temperature < 10. В итоге получается, что is_cold 
равно True, потому что температура меньше 10.


Тип данных bool
Но какой тип данных у переменной is_cold? Давай проверим с помощью команды type().


temperature = 8

is_cold = temperature < 10

print(type(is_cold))

Получилось <class 'bool'>, но что это значит? 
bool  — это специальный тип данных, в котором Python хранит значения логических выражений. Он может принимать только два значения: True или False. 

----------------------------------------------

Операции с типом данных bool
Давай сначала подумаем: а как логические выражения используются в языке?
Например, описание погоды холодно — это логическое выражение, так как оно может быть истиной или ложью. Мы можем сказать: «Если НЕ холодно, то можно сходить погулять». 
Вот так этот код выглядел бы на Python:
  
if not is_cold:
    print("Можно сходить погулять") 

Операция not (НЕ)
Операция not — это логическое отрицание. Она выдаёт True, если выражение неверно (равно False), и наоборот.
Для примера напечатаем результаты такого применения not:

print(True)

# Без неожиданностей, будет напечатано: True

print(not True)

# Будет напечатано: False

print(not False)

# Будет напечатано: True

----------------------------------------------

Вернёмся к нашему примеру с погодой и попробуем скомбинировать несколько условий. Мы определились, что, если на улице не холодно, можно спокойно выбраться на прогулку. 
Но что, если холодно ?

is_cold = True
is_sunny = True

if is_cold and is_sunny:
    print("День чудесный!")

Операция and используется для совмещения двух логических выражений. 
Она выдаcт True, только если оба условия истинны. В остальных случаях она выдаст False.
Попробуй разные комбинации значений переменных is_cold и is_sunny: когда только одна из них True, 
а другая False, или когда обе переменные принимают значение False.  Запусти код с новыми значениями и ответь на вопрос 👇

В каких случаях программа будет печатать «День чудесный!»?


--is_cold = True и is_sunny = True

--is_cold = False и is_sunny = True

--is_cold = True и is_sunny = False

--is_cold = False и is_sunny = False



Делаем вывод:
💡 <условие_1> and <условие_2> принимает значение True, только если оба условия истинны.
  
---------------------------------------------------

Операция or (ИЛИ)
Ну, начнём с того, что обычно выходной — это суббота ИЛИ воскресенье. 
В Python аналог слова ИЛИ — это операция or. 
Вот как может выглядеть программа, которая по названию дня недели определяет, выходной это или будний день.


day_of_week = "Суббота"

if day_of_week == "Суббота" or day_of_week == "Воскресенье":
  print("Сегодня выходной!")

else:
  print("Сегодня будний день!")


Операция or выдаст значение True, если хотя бы одно из условий выполнено. 

-------------------------------------------------------


Задача 1
Попробуй сделать так, чтобы программа приветствовала пользователя в зависимости от времени суток.
Замени многоточия в условиях логическим оператором and или or.


# Впиши, который сейчас час (минуты указывать не нужно)
current_hour = ...

print("На часах " + str(current_hour) + ":00.")

if current_hour >= 6 ... current_hour <= 11:
  print('Доброе утро!')

if current_hour >= 12 ... current_hour <= 17:
  print('Добрый день!')

if current_hour >= 18 ... current_hour <= 22:
  print('Добрый вечер!')

if current_hour <= 5 ... current_hour >= 23:
  print('Доброй ночи!')

..................................................


Теперь напиши программу, которая, исходя из данных, определяет погоду и выводит на экран сообщение Идём гулять, на улице хорошо, если:
не идёт дождь,
а температура воздуха больше 22 градусов.

..выглядеть она должна примерно так...

# Передадим в программу данные
is_raining = False  # Дождя нет
temperature = 16    # Прохладненько

if not is_raining and temperature > 22:
    print('Идём гулять, на улице хорошо')
else:
    print('Сидим дома, читаем Практикум')


--------------------------------------------------------






Язык логики
Когда ты будешь углубляться в программирование или математику, то обнаружишь, что истину (True) часто обозначают как 1, а ложь (False) как 0.
Логические выражения с операциями могут быть очень длинными. Чтобы в них сориентироваться, часто используют таблицы истинности. 
В них перечисляются все возможные комбинации значений логических выражений — например, выражений A и B. А в последнем столбце записывается результат логической операции.
Например, для операции НЕ таблица истинности будет очень простой:
A	not A
1	0
0	1
Для комбинаций с И значений станет уже больше:
A	B	A and B
0	0	0
0	1	0
1	0	0
1	1	1
А такой будет таблица для ИЛИ:
A	B	A or B
0	0	0
0	1	1
1	0	1
1	1	1




















