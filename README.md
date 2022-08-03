# Проект YaCut
Проект для создания короткого (до 16 символов) уникального идентификатора
для длинной ссылки. Позволяет автоматическую генерацию сокращения, если
идентификатор не задан пользователем.

## Требования
`Python 3.9` `Flask 2.0`

## Установка и запуск
Клонировать репозиторий и перейти в него в командной строке:

```commandline
git clone 
```

```commandline
cd yacut
```

Cоздать и активировать виртуальное окружение:

```commandline
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```commandline
    source venv/bin/activate
    ```

* Если у вас windows

    ```commandline
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```commandline
python3 -m pip install --upgrade pip
```

```commandline
pip install -r requirements.txt
```

Запуск проекта:
```commandline
flask run
```

## Лицензия
GNU GPLv3

## Автор
Алексей Швалев