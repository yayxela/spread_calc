# spread_calc

- [Текст условия](/market-maker.md)

## Для чего
Считает spread для всех менеджеров за отрезок времени.
Данные в базу загружены, виртуальное окружение настроено

## Как запустить
## Через venv
```
> .\venv\Scripts\activate
```

## Самому
```
> pip install requirements.txt
```

## Что делает
### Инициировать базу 
```
> init_database.py
```
### Загрузить тестовые данные
```
> init_test.py
```

### Добавить пользователей
```
> add_clients.py <name>
```
1. name - имя пользователя

### Добавить запись
```
> add_order.py <name> <side> <price> <size>
```
1. name - имя пользователя
2. side - BUY|SELL
3. price - цена
4. size - количество 

## Async
Запускает подсчет spread асинхронно
```
> main_async.py
```

## Multithreading
Запускает подсчет spread в нескольких потоках
```
> main_multithreading.py
```

## Время выполнения 
4 часа 10 минут
