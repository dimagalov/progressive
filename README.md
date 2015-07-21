# progressive
Web service for smart news aggregation


Библиотеки:

pip install vk_api sqlalchemy



Запуск:

rm vk.db ; python3 database/create_db.py && python3 web.py & python3 main.py &



main.py складывает в БД новые посты
web.py запускает веб сервер
