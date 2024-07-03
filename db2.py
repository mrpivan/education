База данных


Теперь ты разбираешься в JSON-файлах: 

можешь их создавать, редактировать и сохранять в них нужную информацию. 
Лучше всего они подходят для маленьких проектов. 
Но знаешь, что происходит при каждом вызове функции json.dump(user_data, file)?

Данные не просто записываются, а перезаписываются целиком. 

Представь, что в словаре user_data хранятся данные пользователей нашей программы. 
Всякий раз, когда подключается новый пользователь, его данные записываются в словарь user_data,
а для сохранения в файл нужно перезаписать файл целиком! 
Сейчас это не вызывает особых проблем и ты можешь спокойно пользоваться JSON-ом. 
Но что делать разработчикам игры или популярной социальной сети, к которой новые пользователи подключаются каждую секунду? 
В этом обзорном уроке мы расскажем, какие сложности с хранением данных могут возникнуть в огромных проектах и как их решить. 
Ты узнаешь о хранении данных в таблицах, познакомишься с базами данных SQL и NoSQL.


Таблицы

Чтобы не перезаписывать файл целиком при каждом добавлении новых данных, можно хранить их в Excel-таблице. 
Это даст возможность добавлять в таблицу только одну строку, не трогая остальные. Для этого в Python есть специальная библиотека pandas. 
Она идеально подходит для работы с табличными данными.

SQL
  
Большие компании придерживаются той же логики: они делят данные на связанные друг с другом таблички. 


Вот только хранят их не в Excel, а в специальных базах данных. Они позволяют хранить большие объёмы данных, эффективно добавлять и извлекать их. 

Такие базы данных называются реляционными (англ. relation — «связь»). У реляционных баз данных есть несколько основных характеристик:

Данные хранятся в таблицах, связанных между собой по ключу (как в примере с User_ID).

Схема того, как связаны таблицы и какие типы данных есть в каждом столбце каждой таблицы, называется структурой.

Таблицы вместе со схемой их связей хранятся в файле специального формата (они бывают разные, например .sqlite или .myd).

Используется язык запросов для извлечения, изменения, обработки данных. Это позволяет выполнять сложные операции с данными значительно быстрее, чем в Excel.

Есть возможности выдачи ролей для управления доступом, что повышает уровень безопасности.

  
Язык запросазам данныов к таким бх называется SQL (англ. Structured Query Language — «структурированный язык запросов»). 
По сути, это отдельный язык программирования. 
Сейчас мы не будем закапываться в написание запросов, но обязательно вернёмся к ним в будущем. Но вот один из наиболее популярных:

SELECT *
FROM user_info 

Этот запрос позволяет выгружать все данные из таблицы. Результатом станет такая таблица:

User_ID	User_Name	User_Country	Account_type
101	    user123	     USA	        Premium
102	    codingPro	    India	       Regular
103	     dataGeek	    Russia	     Regular


Символ * в запросе показывает, что нужно выгрузить все данные, а user_info — это название таблицы, из которой нужно выгрузить. 

То есть в переводе с SQL-ного на человеческий запрос выглядит как ВЫБРАТЬ всё ИЗ таблицы user_info



Не забывай, что SQL — отдельный язык программирования со своим синтаксисом. На нём можно писать довольно сложные запросы. 
Вот так, например, можно посмотреть имена пользователей и названия видео, у которых было больше 10 комментариев.

SELECT user_info.User_Name, video_info.Video_Title
FROM user_info
JOIN video_info ON user_info.User_ID = video_info.User_ID
WHERE video_info.Comments > 10; 

В результате получится такая табличка:

User_Name	Video_Title
user123	   "Python Classes"
dataGeek	"Machine Learning 101"



SQL и данные с разной структурой

Язык SQL позволяет эффективно манипулировать данными. 
А ещё несомненный плюс баз данных на нём — возможность хранить таблицы на удалённом сервере. 

Это очень удобно при командной работе: все имеют непрерывный доступ к последней версии данных. 
  
Но у SQL есть и свои ограничения: данные имеют жёсткую структуру.
Это значит, что нужно заранее хорошо продумать, какие таблицы понадобятся, 
какие в них будут поля (столбцы) и как эти таблицы будут связаны между собой. 
Любые изменения в структуре потребуют изменения всей схемы данных, что очень затратно по времени. 

Представь, что одна социальная сеть хранит данные о любимых книгах пользователя и изначально имела возможность лишь перечислить их названия:

["Преступление и наказание", "Мастер и Маргарита",
 "Маленькие женщины", "Думай медленно... решай быстро"] 

Но затем сделали апдейт, и их стало можно делить на рубрики. Например, так:

{
    "художественная литература": {
        "классика": ["Мастер и Маргарита",
                    "Преступление и наказание"],
        "современная": ["Маленькие женщины"]
    },
    "образовательная литература": {
        "психология": ["Мышление, быстрое и медленное"]
    }
} 

Часть пользователей воспользовалась этой возможностью, а другая предпочла оставить всё как есть. 
Так как у этих данных нет единой структуры, хранить их в SQL довольно сложно. И тут на помощь приходит…




NoSQL

NoSQL (англ. Not only SQL — «не только SQL») — это базы данных, которые предоставляют более гибкую модель хранения. 
В отличие от SQL-баз, NoSQL могут хранить всё без фиксированной структуры. База данных NoSQL лучше всего подходит для обработки неопределённых, несвязанных или быстро меняющихся данных.
Самый близкий тебе пример формата хранения данных в NoSQL — JSON. Такие базы данных называются документоориентированными.
Они хранят информацию не как строчки в таблицах, а в объектах, похожих на JSON, каждый из которых называется документом:







В NoSQL база данных даёт быстрый доступ к документу, и для изменения одного поля не придётся перезаписывать его целиком. 
Чего нельзя сделать, если сохранить кучу JSON-файлов у себя на компьютере.
У данных из нашего примера, как и в SQL-базах, есть поля и значения, но хранятся они иначе. 
Плюс в том, что в одних документах можно легко добавлять новые поля, не добавляя эти поля в другие. 
Например, мы легко можем добавить возраст в один из доков:







В SQL так сделать не получилось бы: нам бы пришлось добавлять поле age во все строки таблицы. А в некоторых задачах это не очень нужно. 
Особенно когда значение поля известно о небольшой части пользователей.
Другой пример формата хранения данных в NoSQL — графовые базы данных. 
Графы — это такие схемы, в которых каждый объект представлен точкой, а связи между объектами — линиями или стрелками между этими точками:






Точки называют узлами или вершинами, а стрелочки — рёбрами графа.
  
Такие базы данных очень подходят для хранения связей в социальных сетях, где люди могут подписываться и добавлять в друзья. 
Например, с помощью запроса к такой базе можно легко увидеть всех подписчиков конкретного пользователя.
Или в случае с книгами посчитать, сколько читателей у той или иной книги.
Есть ещё другие виды NoSQL баз данных: например, ключ-значение или семейство столбцов. 
У них также есть свой формат хранения данных и своя специфика применения. Можешь почитать про них тут.
Базы NoSQL, несмотря на название, часто позволяют обращаться к ним с помощью SQL запросов — это стандарт в разработке, который удобно использовать. Но они предоставляют и другие способы взаимодействия. Обычно это отдельные библиотеки со своими функциями и классами, с помощью которых можно считывать и изменять данные.
Ух, ну и урок! Если всё кажется сложным, не пугайся. 
Организация и хранение данных — объёмная задача, которой занимается целая команда IT-специалистов: 


архитекторы данных планируют и проектирует базы так, чтобы хранение и доступ к данным были эффективными,

инженеры данных реализуют архитектуру, организуя сбор, обработку и хранение данных,

менеджер качества данных обеспечивает точность и надёжность данных,

дата-сайентисты работают с данными, строят графики и делают анализ, на основе которого компании принимают решения о дальнейшем развитии.

