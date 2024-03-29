# Парсер документации Python и PEP

## Технологии:
 ![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)  ![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python) 
 [requests_cache](https://requests-cache.readthedocs.io/en/stable/),
 [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/),
 [prettytable](https://ptable.readthedocs.io/en/latest/tutorial.html)

## Описание проекта
Парсер предназначен для сбора информации о нововведениях Python и количестве статусов документов PEP.
За процесс парсинга отвечает библиотека [```BeautifulSoup```](https://beautiful-soup-4.readthedocs.io/en/latest/).
 Именно с её помощью происходит выбор нужных данных. Вывод статусбара базируется на библиотеке
 [```tqdm```](https://tqdm.github.io/), а вывод табличных значений в красивом виде происходит за счёт
 [```prettytable```](https://ptable.readthedocs.io/en/latest/tutorial.html).

В целях экономии трафика и для проведения процесса тестирования и отладки было организовано кэширование запросов к
 внешним ресурсам с помощью библиотеки [```requests_cache```](https://requests-cache.readthedocs.io/en/stable/). При
 необходимости кэш можно очистить.
## Как запустить проект

Клонируйте репозиторий, перейдите в папку, создайте виртуальное окружение и активируйте:
```
python3 -m venv env
```
```
. venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
(venv) python3 -m pip install --upgrade pip
```
```
(venv) pip install -r requirements.txt
```
## Режимы работы

### whats-new
Собирает ссылки на статьи о нововведениях.

### latest-versions
Собирает информацию о версиях Python — номер, статус и ссылка на документацию.

### download
Скачивает архив с документацией Python на ваш локальный диск. В директорию ./src/downloads/

### pep
Посчитывает количество PEP в каждом статусе и общее количество PEP; данные о статусе парсятся со страницы каждого PEP

### Дополнительные необязательные аргументы
***-h, --help*** — выводит вспомогательную информацию о работе парсера

***-c, --clear-cache*** — Удаляет кэш пред стартом

***-o {pretty,file}, --output {pretty,file}***  —  Дополнительные способы вывода данных. Параметр pretty выводит данные в терминале в оформленной таблице, параметр file сохраняет данные в csv файл.

◾  Через командную строку в директории src запустите скрипт:

    python main.py MODE -ARGS
Где MODE —   Название режима работы (из 4х доступных), а -ARGS  —  Перечисление необязательных аргументов

## Логирование
В проекте собираются логи с уровня INFO и сохраняются в директорию ./src/logs

### Автор
Selivanov Dmitry
