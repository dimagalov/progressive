# progressive
Web service for smart news aggregation

Библиотеки: pip install vk_api sqlalchemy

Запуск: rm vk.db ; database/create_db.py && nohup web.py & nohup main.py &

main.py складывает в БД новые посты
web.py запускает веб-сервер
