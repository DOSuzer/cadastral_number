# cadastral_number
## Описание
Сервис принимает запрос с указанием кадастрового номера, широты и долготы, эмулирует отправку запроса на внешний сервер, который может обрабатывать запрос до 60 секунд. Затем отдает результат запроса.

Проект эмуляции внешнего сервера [cadastral_endpoint](https://github.com/DOSuzer/cadastral_endpoint).

Адрес сервера 127.0.0.1:8000/

## Запуск проекта
1. Клонировать репозиторий:
   ```
   git clone git@github.com:DOSuzer/cadastral_number.git
   ```
2. Перейти в папку с docker-compose.yml:
   ```
   cd cadastral_number/cadastral_proccess
   ```
   
3. Запустить сборку:
   ```
   docker-compose up
   ```


## В проекте доступны следующие эндпойнты:
+ /query/
  * POST запрос - запрос данных по кадастровому номеру;
    ```
    {
    "cadastral_number":"11:22:123456:155",
    "longitude":"55",
    "latitude":"54"
    }
    ```
    Ответ:
    ```
    {
    "status": "Запрос отправлен.",
    "record_id": 10,
    "task_id": "490c8abb-fc62-4d2d-84ab-0756e6485121"
    }
    ```
+ /result/
  * GET запрос - получение результатов запроса
    ```
    {
    "record_id": 10,
    "task_id": "490c8abb-fc62-4d2d-84ab-0756e6485121"
    }
    ```
    Ответ:
    ```
    {
    "status": "SUCCESS",
    "result": true
    }
    ```
+ /history/
  * GET запрос - получение истории запросов
    
    Ответ:
    ```
    {
    "count": 10,
    "next": "http://127.0.0.1:8000/history/?page=2",
    "previous": null,
    "results": [
        {
            "id": 10,
            "cadastral_number": "11:22:123456:155",
            "longitude": "55.000000",
            "latitude": "54.000000",
            "result": true,
            "date": "15-09-2023 12:30:13"
        },
        {
            "id": 9,
            "cadastral_number": "11:22:123456:155",
            "longitude": "55.000000",
            "latitude": "54.000000",
            "result": null,
            "date": "15-09-2023 12:29:47"
        },
        {
            "id": 8,
            "cadastral_number": "11:22:123456:155",
            "longitude": "54.000000",
            "latitude": "54.000000",
            "result": false,
            "date": "15-09-2023 12:18:38"
        },
        {
            "id": 7,
            "cadastral_number": "11:22:123456:155",
            "longitude": "54.000000",
            "latitude": "54.000000",
            "result": true,
            "date": "15-09-2023 12:18:37"
        },
        {
            "id": 6,
            "cadastral_number": "11:22:123456:155",
            "longitude": "54.000000",
            "latitude": "54.000000",
            "result": true,
            "date": "15-09-2023 12:18:36"
        }
    ]
    }
    ```

+ /history/?filter=11:22:123456:155
  * GET запрос - получение истории запросов

    Ответ:
    ```
    {
    "count": 7,
    "next": "http://127.0.0.1:8000/history/?filter=11%3A22%3A123456%3A155&page=2",
    "previous": null,
    "results": [
        {
            "id": 10,
            "cadastral_number": "11:22:123456:155",
            "longitude": "55.000000",
            "latitude": "54.000000",
            "result": true,
            "date": "15-09-2023 12:30:13"
        },
        {
            "id": 9,
            "cadastral_number": "11:22:123456:155",
            "longitude": "55.000000",
            "latitude": "54.000000",
            "result": null,
            "date": "15-09-2023 12:29:47"
        },
        {
            "id": 8,
            "cadastral_number": "11:22:123456:155",
            "longitude": "54.000000",
            "latitude": "54.000000",
            "result": false,
            "date": "15-09-2023 12:18:38"
        },
        {
            "id": 7,
            "cadastral_number": "11:22:123456:155",
            "longitude": "54.000000",
            "latitude": "54.000000",
            "result": true,
            "date": "15-09-2023 12:18:37"
        },
        {
            "id": 6,
            "cadastral_number": "11:22:123456:155",
            "longitude": "54.000000",
            "latitude": "54.000000",
            "result": true,
            "date": "15-09-2023 12:18:36"
        }
    ]
    }
    ```
    
+ /ping/
  * GET запрос - получение статуса сервера

    Ответ:
    ```
    {
    "status": "Сервер работает",
    "database": "sqlite"
    }
    ```
