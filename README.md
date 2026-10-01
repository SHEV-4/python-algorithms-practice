# Python: практика з алгоритмів

Збірка навчальних завдань з Python: робота з датою й текстом, файли, структури даних, замикання і генератори, декоратори та ООП. Завдання згруповано за темами курсу.

## Зміст

| Папка | Завдання | Що робить |
|---|---|---|
| `hw03_dates_and_strings` | `first_task.py` | `get_days_from_today(date)` повертає, скільки днів минуло від дати у форматі `РРРР-ММ-ДД` |
| | `second_task.py` | `get_numbers_ticket(min, max, quantity)` генерує унікальні випадкові числа для лотереї |
| | `third_task.py` | `normalize_phone(phone)` приводить телефон до формату `+380XXXXXXXXX` |
| `hw04_files_and_structures` | `first_task/salary.py` | `total_salary(path)` рахує загальну та середню зарплату з файлу |
| | `second_task/cats_info.py` | `get_cats_info(path)` читає файл із котами й повертає список словників |
| | `third_task/` | візуалізація структури папки в кольорі (`colorama`) |
| | `fourth_task/main.py` | консольний бот-помічник зі словником контактів |
| `hw05_functions_and_logs` | `first_task.py` | `caching_fibonacci()`: числа Фібоначчі з кешуванням (замикання) |
| | `second_task.py` | `generator_numbers` і `sum_profit`: сума чисел у тексті через генератор |
| | `third_task.py` | аналізатор лог-файлів: підрахунок за рівнями та фільтрація |
| | `fourth_task.py` | бот-помічник з декоратором `input_error` |
| | `log.txt` | приклад лог-файлу |
| `hw06_oop_address_book` | `main.py` | адресна книга на класах `Field`, `Name`, `Phone`, `Record`, `AddressBook` |

## Приклади

**Нормалізація телефону:**

```python
from third_task import normalize_phone

normalize_phone("(050)123-45-67")   # '+380501234567'
normalize_phone("380501234567")     # '+380501234567'
```

**Кешування Фібоначчі:**

```python
from first_task import caching_fibonacci

fib = caching_fibonacci()
fib(50)   # 12586269025
```

**Аналізатор логів:**

```bash
python third_task.py log.txt ERROR
```

```text
Рівень логування | Кількість
-----------------|----------
INFO             | 3
DEBUG            | 3
ERROR            | 3
WARNING          | 1
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 11:30:15 ERROR Backup process failed.
```

Другий аргумент (рівень логування) необов'язковий: без нього виводиться лише таблиця підрахунку.

**Структура папки:**

```bash
cd hw04_files_and_structures/third_task
pip install -r requirements.txt
python main.py /шлях/до/папки
```

## Запуск

Потрібен Python 3.12 або новіший (у `third_task` використано f-рядки з вкладеними лапками). Єдина зовнішня залежність це `colorama` для `hw04_files_and_structures/third_task`.

```bash
git clone https://github.com/SHEV-4/python-algorithms-practice.git
cd python-algorithms-practice
```

Файли в кожній папці запускай із цієї папки, наприклад:

```bash
cd hw05_functions_and_logs
python second_task.py
python fourth_task.py
```

## Що використано

Python, стандартна бібліотека (`datetime`, `random`, `re`, `pathlib`, `collections`, `sys`), замикання, генератори, декоратори, ООП, `colorama`.
