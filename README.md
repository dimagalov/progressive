# progressive
Web service for smart news aggregation


**Библиотеки:**

`pip3 install vk_api sqlalchemy tornado pymysql`

`cd web && npm install`

**База данных:**

`python3 news/database/create_db.py`

**Сборка веб-файлов**

`cd web`
`grunt less autoprefixer` или `grunt watch`

**Запуск:**

`python3 web/main.py & python3 news/main.py &`
