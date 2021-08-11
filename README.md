# djangoProject

Установка:
-------------------------
* Установить СУБД Postgres 
* Внести в конфигурационный файл данные о СУБД (адрес хоста, порт и т.д.)
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
* Установить необходимые библиотеки, перечисленные в файле requirements.
* запустите команды:
``` 
python3 manage.py migrate
python3 manage.py runserver
```
* Добавить пользователя с ролевой моделью алминистратор (python3 manage.py createsuperuser). Добавление пользователя с ролевой моделью пользователь осуществляется через систему администрирования.

Описание:
-------------------------
 
1. Процесс аутентификации реализован через Basic Authentication. 
2. Для получения опросов, вопросов следует переходить по url ` /api/v1/polls ` или ` /api/v1/questions `
3. Для получения активных опросов следует перейти по url  ` /api/v1/polls/get_active_polls `
4. Для прохождение опроса следует составить post запрос по следующему url ` /api/v1/polls/complete_poll `
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

5. Для завершения анонимного запроса следует указать в body ` "isAnon": "True" `
6. Для получения пройденных пользователем опросов с детализацией следует перейти по url ` api/v1/completed_polls/get_user_history `

Скриншоты:
-------------------------
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/polls.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/admin.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/complete_poll2.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/get_active_polls.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/get_user_history.png)
![Image alt](https://github.com/Stef16123/DjangoProject/raw/master/questions.png)
