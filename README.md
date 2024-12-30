# Speed Tester

## Авторы проекта
ФИО: Мазурик Павел Петрович // Ответственный за основную логику проекта
ISU: 472193

ФИО: Никифоров Дмитрий Алексеевич // Ответственный за графический интерфейс
ISU: 466882

## Описание проекта
Speed Tester — это инструмент для анализа скорости и точности набора текста. Он позволяет:
- Узнать скорость набора текста (в символах / секунду).
- Узнать, с какой точностью набирается текст (в процнтах).

## Установка и настройка
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование
Запустите основной файл проекта:
```bash
python main.py
```

### Пример сценария работы
1. При запуске программы отобразится главное меню.
2. Нажмите кнопку "Начать".
3. Начните вводить текст.
4. Остановите ввод в любой момент.


## Зависимости
- Python 3.10+
- lorem


## Структура проекта
```
├── typing_speed_tester/
│   ├── __init__.py <- служит для того, чтобы каталог typing_speed_tester стал пакетом Python
│   ├── analyzer.py <- может включать функции для вычисления скорости набора текста, точности и других метрик
│   ├── decorators.py <- декораторы, которые могут быть использованы для улучшения функциональности других модулей
│   ├── exceptions.py <- позволяет централизованно управлять ошибками и улучшить обработку исключений
│   ├── gui.py <- графический интерфейс
│   ├── tester.py <- логика самого тестирования
│   └── test_provider.py <- модуль для генерации тестовых данных
├── main.py <- запускает приложение
├── requirements.txt <- указаны все зависимости проекта
├── README.md <- файл с документацией
```

## Участие ChatGPT 4.0
В процессе разработки ChatGPT 4o помогал в:
- Оформлении кода в соответствии с PEP 8.
- Дебаггинге кода.
- Написании комментариев и док-строк.