# DAIRIES-API
«Dairies-API» - програмный интерфейс проекта социальной сети Dairies, позволяющий сторонним сервисам взаимодействовать с её приложениями.


## Особенности проекта

Основная функция API - управление ресурсами приложения posts. Данное приложение включает в себя модели Post (публикации), Group (группа/тема публикаций), Comment (комментарии к публикациям) и Follow (подписки на авторов).

Список возможных операций с объектами моделей зависит от уровня доступа пользователя: например, неавторизованные пользователи имеют только право просмотра.

В данном проекте использована система аутентификации по JWT-токену. Обработка всех запросов связанных с пользователями, включая, получение токена, осуществляется библиотекой djoser. Для работы с токенами установлен плагин Simple JWT.


## Основные технологии проекта
* Python 3.7
* Django 2.2.16
* Django REST framework 3.12.4


## Запуск проекта локально

*Для запуска проекта потребуется установленный Python версии 3.7 и выше.*

**Создайте папку с названием проекта и инициализируйте репозиторий:**
```bash
mkdir dairies_api
```
```bash
cd dairies_api
```
```bash
git init
```

**Клонируйте репозиторий:**
```bash
git clone https://github.com/rock4ts/dairies_api
```

**Создайте и активируйте виртуальное окружение:**
```python
python3 -m venv venv
```
```python
source venv/bin/activate
```
```python
python3 -m pip install --upgrade pip
```
Установите записимости из файла requirements.txt:
```python
pip install -r requirements.txt 
```
**Выполните миграции:**
```python
python3 manage.py migrate
```
**Запустите проект:**
```python
python3 manage.py runserver
```


## Начало работы

Для доступа к созданию, редактированию или удалению объектов необходимо создать учётную запись и авторизоваться.

Чтобы зарегистрировать нового пользователя отправьте 'POST' запрос по нижеуказанному адресу, в теле запроса в формате JSON укажите параметры "username" и "password":  

```
http://127.0.0.1:8000/api/v1/users/
```
Пример тела запроса:
```
{
    "username": "rock4ts",
    "password": "r4ndompa$$w0rd"
}
```
Ответ успешной регистрации имеет статус `201 Created`, в теле ответа содержатся данные нового пользователя, например:
```
{
    "email": "",
    "username": "rock4ts",
    "id": 1
}
```

Теперь можно получить токен авторизации JWT, отправьте 'POST' запрос, согласно инструкции.
Адрес для получения JWT-токена:
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
Пример тела запроса:
```
{
    "username": "rock4ts",
    "password": "r4ndompa$$w0rd"
}
```

При выполнении запроса API вернёт токен в поле access, а данные из поля refresh пригодятся для обновления токена.
Пример ответа с JWT-токеном:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzY2Njg3NCwianRpIjoiNWE0ZjIwMGQxN2RmNDBhMGJkY2JmN2YyYTRjYTE0MTQiLCJ1c2VyX2lkIjoxfQ.SzIFfzaC1wxIuwrH1kE-91Uu0b0yWqrW7Pg38i",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzOTI2MDc0LCJqdGkiOiJmMTU3MzAxMGZhNjk0ZmNiOTI1ZTA0NmI3ZGNlNjA4OCIsInVzZXJfaWQiOjF9.IjyppcUSfKzBWlivZo0DZPlZ7JAkpkOMVeBMQPxH"
}
```
<br>
Готово! Передавайте полученный токен в заголовке каждого запроса к API в формате "ключ: токен". Например:
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzOTI2MDc0LCJqdGkiOiJmMTU3MzAxMGZhNjk0ZmNiOTI1ZTA0NmI3ZGNlNjA4OCIsInVzZXJfaWQiOjF9.IjyppcUSfKzBWlivZo0DZPlZ7JAkpkOMVeBMQPxH
```
**Обратите внимание, что перед токеном должно стоять ключевое слово Bearer и пробел.** В противном случае авторизация не пройдёт и API вернёт ошибку доступа.


## Права доступа

Неавторизованные пользователи имеют права наблюдателя, им доступен лишь просмотр групп, публикаций и комментариев.

У авторизованных пользователей добавляются права на создание, изменение и удаление собственных объектов ('POST', 'PUT', 'PATCH' и 'DELETE' запросы). Они могут также выводить список и управлять подписками на других пользователей. Наконец, они имеют доступ к просмотру, редактированию и удалению данных своего аккуанта.


## Документация, запросы, эндпоинты

Документация проекта динамически формируется при помощи плагина drf-yasg. Подробную информацию о доступных эндпоинтах и запросах можно посмотреть, перейдя по одной из указанных ссылок:

```
# документация в формате redoc
http://127.0.0.1:8000/redoc/
```
```
# документация в формате swagger
http://127.0.0.1:8000/redoc/
```

Приятного пользования!
