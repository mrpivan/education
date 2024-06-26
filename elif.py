Команда elif

Чтобы понять, зачем нужна новая команда, давай попробуем решить одну задачку. И, кстати, обрати внимание на выделенные слова!
Напиши программу, которая приветствует пользователя в зависимости от возраста.

--------------------------
age = 26
# твой код

--------------------------



Эту задачу можно решить несколькими способами, но самый прямолинейный — переписать условие задачи в виде кода:



age = 26

if age > 25:
    print("Здравствуйте!")
else:
    if age > 5:
        print("Привет!")
    else:
        print("Кукусики!")




------------------------------------------


Здесь всего два условия, но бывают ситуации, когда их намного больше. 
Вот пример кода, который переводит количество баллов за тест в пятибалльную оценку:


# Количество верных вопросов от 0 до 100
score = 43

# Проверяем и выводим буквенную оценку
if score >= 80:
    print("Ваша оценка: 5")
else:
    if score >= 70:
        print("Ваша оценка: 4")
    else: 
        if score >= 55:
            print("Ваша оценка: 3")
        else: 
            if score >= 0:
                print("Ваша оценка: 2")
            else:
                print("Вы ввели неверное количество. Введите число от 0 до 100.")


--------------------------------------


Как видишь, постепенно код съезжает вправо, и приходится делать всё больше отступов. 
Так не пойдёт: если условий слишком много, то код не поместится на экран, что как минимум неудобно.
К счастью, проблему можно решить.

Блок

else:
    if age > 5: 
      
можно заменить на

elif age > 5: 

Тут мы используем elif — сокращение от else if (англ. «иначе если»). Эта команда используется, когда нужно разветвить программу по двум условиям или больше. 
Вот как преобразится код, если использовать в нём else if:


# Количество верных вопросов от 0 до 100
score = 43

# Проверяем и выводим буквенную оценку
if score >= 80:
    print("Ваша оценка: 5")
elif score >= 70:
    print("Ваша оценка: 4")
elif score >= 55:
    print("Ваша оценка: 3")
elif score >= 0:
    print("Ваша оценка: 2")
else:
    print("Вы ввели неверное количество. Введите число от 0 до 100.")


----------------------------------------------------------


Используя elif, перепиши программу, которая приветствует пользователя в зависимости от возраста. 
Напомина. условия: если возраст старше 25, выведи «Здравствуйте!», если возраст старше 5, выведи «Привет!», а в других случаях — «Кукусики!».



age = 26

if age > 25:
  print("Здравствуйте!")
else:
  if age > 5:
    print("Привет!")
    else:
      print("Кукусики!")

​

---------------------------------------------------------






Представь, что ты разрабатываешь игру «Защита королевства — 2». 
Сейчас этап программирования ответов городского привратника. Он встречает всех входящих в город и оценивает их фракцию: 

-если это бандит или орк, то страж прогоняет их прочь;

-если это крестьянин, то страж ворчит, но впускает его;

-если это король, то страж кланяется и тепло приветствует его.

Напиши программу, которая учтёт все эти условия. Используй фразы, которые даны в коде, и переменную fraction, которая принимает одно из значений — орк, бандит, крестьянин или король. 
Для проверки фракции используй if, elif и else.




phrase_bad = "Пошло вон, упырское отродье!"
phrase_neutral = "Проходи, не задерживайся, бродяга."
phrase_king = "Ваше величество! Как мы вам рады! Добро пожаловать!"

fraction = 'орк'

# твой код

















РЕШЕНИЕ 

phrase_bad = "Пошло вон, упырское отродье!"
phrase_neutral = "Проходи, не задерживайся, бродяга."
phrase_king = "Ваше величество! Как мы вам рады! Добро пожаловать!"

fraction = 'орк'

# твой код

if fraction == 'орк' or fraction == 'бандит':
    print(phrase_bad)
elif fraction == "крестьянин":
    print(phrase_neutral)
else:
    print(phrase_king)



----------------------------------------------------------------




В Гномии проходит жёсткий отбор в модельное агентство «Метр страсти», но отбоя от желающих нет. 
Нормативы строгие: рост должен быть выше 90 см, а вес не более или равен 80 кг. При этом гномов и гномих с впечатляющей бородой длиной от 120 см берут сразу в VIP-отдел — такие данные встречаются у единиц.
Чтобы не просматривать все заявки вручную, в агентстве решили написать программу на Python, которая будет принимать решение автоматически. 
По описанию она должна определить, проходит ли существо в модельное агентство и попадает ли в VIP-отдел. На экране должен появиться один из трёх вариантов: «проходит», «VIP» или «не проходит». 
Используй if, elif и else для управления ходом программы.




weight = 60 # вес
height = 50 # рост
beard = 110 # борода

# твой код




















РЕШЕНИЕ:


weight = 60 # вес
height = 50 # рост
beard = 110 # борода

# твой код
if height > 90 and weight <= 80 and beard < 120:
    print("проходит")
elif beard >= 120:
    print("VIP")
else:
    print("не проходит")












"""
ЧТОЖ ТЕПЕРЬ ВЫ УМЕЕТЕ ПРЕКРАСНО ПОЛЬЗОВАТЬСЯ ВЕТВЛЕНИЕМ 


