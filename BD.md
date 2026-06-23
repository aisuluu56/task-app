Подключение pgAdmin к PostgreSQL
pgAdmin обычно устанавливается автоматически вместе с PostgreSQL. Вот пошаговая инструкция.
Шаг 1. Запустить pgAdmin
Вариант A: Через меню «Пуск»:
Пуск → PostgreSQL 17 (или другая версия) → pgAdmin 4
Вариант B: Через поиск Windows:
Нажмите Win → введите pgAdmin → запустите pgAdmin 4
При первом запуске pgAdmin попросит задать мастер-пароль для самого pgAdmin (это не пароль от PostgreSQL). Придумайте любой и запомните его.
После запуска в браузере откроется интерфейс pgAdmin по адресу http://127.0.0.1:XXXX.
Шаг 2. Создать подключение к серверу
В левом дереве объектов:
Раскройте узел Servers
Если сервер уже есть (обычно PostgreSQL 17) — переходите к Шагу 3
Если сервера нет, нажмите правой кнопкой на Servers → Register → Server…
Шаг 3. Настроить параметры подключения
Откроется окно Register - Server. Заполните вкладки:
Вкладка General
Name: PostgreSQL 17 (любое понятное имя)
Вкладка Connection
Поле
Значение
Host name/address
localhost
Port
5432
Maintenance database
postgres
Username
postgres
Password
тот пароль, который вы задали при установке PostgreSQL
Поставьте галочку Save password, чтобы не вводить пароль каждый раз.
Нажмите Save.
Шаг 4. Проверить подключение
Если всё сделано правильно, в левом дереве появится узел сервера с зелёным значком 🔌. Раскройте его:
Databases → postgres
Должны быть видны схемы, таблицы и т.д.
Шаг 5. Создать базу данных task_app
В дереве щёлкните правой кнопкой на Databases
Create → Database…
В поле Database введите: task_app
Owner оставьте postgres
Нажмите Save
База task_app появится в списке.
Шаг 6. Выполнить schema.sql
В дереве щёлкните правой кнопкой на базе task_app
Выберите Query Tool (или Query Tool в верхней панели)
Откроется редактор SQL-запросов
Откройте файл schema.sql:
File → Open File… → выберите ваш schema.sql
Или просто скопируйте содержимое:
sql
12345
Нажмите кнопку Execute/Run (▶️) или клавишу F5
В нижней панели появится сообщение:
12
Шаг 7. Проверить, что таблица создана
В дереве раскройте: task_app → Schemas → public → Tables
Должна появиться таблица tasks
Раскройте её — увидите колонки: id, title, status
Чтобы посмотреть данные, щёлкните правой кнопкой на tasks → View/Edit Data → All Rows

py -m pytest test_service.py -v
py main.py