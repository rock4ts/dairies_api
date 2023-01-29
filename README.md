# DAIRIES-API
DAIRIES-API - это програмный интерфейс проекта социальной сети Dairies.  
API предоставляет пользователям доступ к работе с записями (постами) личных дневников, включая создание, чтение и редактирование.  
API также позволяет оставлять комментарии к постам, подписываться на любимых авторов и просматривать информацию о существующих сообществах.
<br></br>

## Установка
Для запуска проекта в командной строке:  

Клонируйте репозиторий:
```bash
git clone https://github.com/rock4ts/dairies_project_api
```
Перейдите в папку проекта:
```bash
cd dairies_project_api
```
Создайте и активируйте виртуальное окружение:
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
Выполните миграции:
```python
python3 manage.py migrate
```
Запустите проект:
```python
python3 manage.py runserver
```
<br></br>

## Особенности проекта
В основе проекта лежат модели Post, Comment, Follow и Group.  

Зарегистрированные пользователи могут просматривать / добавлять, полностью или частично изменять или удалять информацию об объектах вышеуказанных моделей.  

Для анонимных пользователей доступна лишь функция чтения.  

Ответ на запрос о получении информации о подписках (объектах модели Follow) ограничен информацией о собственных подписках авторизованного пользователя и недоступен для анонимных пользователей.  

API также не предусматривает возможность добавления или изменения информации о группах (объектах модели Group).

<br></br>
## Регистрации и аутентификация пользователя:  

В данном проекте использована система аутентификации по JWT-токену. Для работы с пользователями и JWT в файл зависимостей _requirements.txt_ были добавлены библиотеки djangorestframework-simplejwt и djoser.  

Чтобы зарегистрировать нового пользователя отправьте http запрос методом 'POST' по нижеуказанному адресу, в теле запроса в формате JSON укажите параметры "username" и "password":  

```
Адрес для регистрации пользователя:

'адрес_сервера_django/api/v1/users/'
```
```
Пример тела POST-запроса для регистрации пользователя:

{
    "username": "rock4ts",
    "password": "r4ndompa$$w0rd"
}
```

Зарегистрированного пользователя необходимо аутентифицировать. Для этого понадобиться JWT-токен.  
Токен можно получить, отправив POST-запрос с параметрами и значениями, использованными при регистрации:

```
Адрес для получения JWT-токена:

'адрес_сервера_django/api/v1/jwt/create/'
```
```
Пример тела POST-запроса для получения JWT-токена:

{
    "username": "rock4ts",
    "password": "r4ndompa$$w0rd"
}
```

При успешном выполнении запроса API вернёт токен в поле access, а данные из поля refresh пригодятся для обновления токена.

```
Пример ответа с JWT-токеном:

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzY2Njg3NCwianRpIjoiNWE0ZjIwMGQxN2RmNDBhMGJkY2JmN2YyYTRjYTE0MTQiLCJ1c2VyX2lkIjoxfQ.SzIFfzaC1wxIuwrH1kE-91Uu0b0yWqrW7Pg38ixxx",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzOTI2MDc0LCJqdGkiOiJmMTU3MzAxMGZhNjk0ZmNiOTI1ZTA0NmI3ZGNlNjA4OCIsInVzZXJfaWQiOjF9.IjyppcUSfKzBWlivZo0DZPlZ7JAkpkOMVeBMQPxHxxx"
}
```

Этот токен также надо будет передавать в заголовке каждого запроса, в поле Authorization.  
Перед самим токеном должно стоять ключевое слово Bearer и пробел.  
<br></br>
**Примечание**:
В [документации](https://djoser.readthedocs.io/en/latest/getting_started.html#available-endpoints) djoser содержиться список доступных эндпоинтов для расширенной работы с пользователями.

<br></br>
## Примеры запросов:
* Запрос на добавления поста:  

```
Адрес POST-запроса:

'адрес_сервера_django/api/v1/posts/'
```

```
Тело запроса:

{
    "text": "test text",
    "group": 1,
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3/OAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANCSURBVEiJtZZPbBtFFMZ/M7ubXdtdb1xSFyeilBapySVU8h8OoFaooFSqiihIVIpQBKci6KEg9Q6H9kovIHoCIVQJJCKE1ENFjnAgcaSGC6rEnxBwA04Tx43t2FnvDAfjkNibxgHxnWb2e/u992bee7tCa00YFsffekFY+nUzFtjW0LrvjRXrCDIAaPLlW0nHL0SsZtVoaF98mLrx3pdhOqLtYPHChahZcYYO7KvPFxvRl5XPp1sN3adWiD1ZAqD6XYK1b/dvE5IWryTt2udLFedwc1+9kLp+vbbpoDh+6TklxBeAi9TL0taeWpdmZzQDry0AcO+jQ12RyohqqoYoo8RDwJrU+qXkjWtfi8Xxt58BdQuwQs9qC/afLwCw8tnQbqYAPsgxE1S6F3EAIXux2oQFKm0ihMsOF71dHYx+f3NND68ghCu1YIoePPQN1pGRABkJ6Bus96CutRZMydTl+TvuiRW1m3n0eDl0vRPcEysqdXn+jsQPsrHMquGeXEaY4Yk4wxWcY5V/9scqOMOVUFthatyTy8QyqwZ+kDURKoMWxNKr2EeqVKcTNOajqKoBgOE28U4tdQl5p5bwCw7BWquaZSzAPlwjlithJtp3pTImSqQRrb2Z8PHGigD4RZuNX6JYj6wj7O4TFLbCO/Mn/m8R+h6rYSUb3ekokRY6f/YukArN979jcW+V/S8g0eT/N3VN3kTqWbQ428m9/8k0P/1aIhF36PccEl6EhOcAUCrXKZXXWS3XKd2vc/TRBG9O5ELC17MmWubD2nKhUKZa26Ba2+D3P+4/MNCFwg59oWVeYhkzgN/JDR8deKBoD7Y+ljEjGZ0sosXVTvbc6RHirr2reNy1OXd6pJsQ+gqjk8VWFYmHrwBzW/n+uMPFiRwHB2I7ih8ciHFxIkd/3Omk5tCDV1t+2nNu5sxxpDFNx+huNhVT3/zMDz8usXC3ddaHBj1GHj/As08fwTS7Kt1HBTmyN29vdwAw+/wbwLVOJ3uAD1wi/dUH7Qei66PfyuRj4Ik9is+hglfbkbfR3cnZm7chlUWLdwmprtCohX4HUtlOcQjLYCu+fzGJH2QRKvP3UNz8bWk1qMxjGTOMThZ3kvgLI5AzFfo379UAAAAASUVORK5CYII="
}
```

```
Пример ответа:

{
    "id": 14,
    "text": "test text",
    "author": "rock4ts",
    "image": "http://127.0.0.1:8000/media/posts/temp.png",
    "group": 1,
    "pub_date": "2022-09-07T08:47:11.084589Z"
} 
```
<br></br>

* Запрос на получение списка комментариев к посту с id == 14:  
```
Адрес GET-запроса:

 'адрес_сервера_django/api/v1/posts/14/comments/'
```

```
Пример ответа:

[
    {
        "id": 1,
        "author": "k4t",
        "post": 14,
        "text": "k4t comment text",
        "created": "2022-09-07T08:47:11.084589Z"
    },
    {
        "id": 2,
        "author": "rock4ts",
        "post": 14,
        "text": "rock4ts comment text",
        "created": "2022-09-07T08:47:11.084589Z"
    }
]
```
<br></br>

* Запрос подписки пользователя "rock4ts" на автора с ником "k4t" :

```
Адрес POST-запроса:

 'адрес_сервера_django/api/v1/follow/'
```
```
Тело запроса:

{
    "following": "k4t"
} 
```

```
Пример ответа:

{
    "id": 1,
    "user": "rock4ts",
    "following": "k4t"
}
```
<br></br>
**Примечание**: перейдя в браузере по адресу 'адрес_сервера_django/redoc', вы можете ознакомиться с полным перечнем возможных запросов и ответов API.

<br></br>
## Технологии:
 Проект создан с использованием _Python 3.7_ и _Django 2.2_

<br></br>
## Автор:
Артём Сухов, студент Яндекс.Практикум, курс Python-разработчик+