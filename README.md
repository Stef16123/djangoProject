# djangoProject

Инструкция по разворачиванию приложения:
-------------------------
* Создайте Postgres базу данных и подключите её в settings.py
* Пример:
``` 
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'test_django',
'USER': 'test_user',
'PASSWORD': '1234',
'HOST': '127.0.0.1',
'PORT': '5432',
}
} 
```
 
установите все библиотеки из файла requirements.
запустите команды:
``` 
python3 manage.py migrate
python3 manage.py runserver
```

Документация:
-------------------------
 
1. Для авторизации используется базовая аутентификация. 
2. Для того что бы ей воспользоваться нужно создать админа (` python3 manage.py createsuperuser `). Затем войдя в в панель администратора можно создать обычного user без статуса admin
3. Для получения опросов, вопросов следует переходить по url ` /api/v1/polls ` или ` /api/v1/questions `
4. Для получения активных опросов следует перейти по url  ` /api/v1/polls/get_active_polls `
5. Для прохождение опроса следует составить post запрос по следующему url ` /api/v1/polls/complete_poll `
* Пример body:
``` {
"answers": [
{
"question": 2,
"text": "yes"
},
{
"question": 1,
"text": "no"
}
],
"poll": 1,
"isAnon": "False"
}
```

7. Для завершения анонимного запроса следует указать в body ` "isAnon": "True" `
8. Для получения пройденных пользователем опросов с детализацией следует перейти по url ` api/v1/completed_polls/get_user_history `

Скриншоты:
-------------------------
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/polls.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/admin.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/complete_poll2.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/get_active_polls.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/get_user_history.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/questions.png)
