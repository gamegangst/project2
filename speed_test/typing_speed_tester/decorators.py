import time
import logging
from functools import wraps


# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_execution_time(func):
    """Декоратор для измерения времени выполнения функции."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        logging.info(f"Функция {func.__name__} выполнена за {execution_time:.2f} сек.")
        return result
    return wrapper


def validate_input(func):
    """Декоратор для проверки корректности входных данных."""
    def wrapper(text, *args, **kwargs):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Входной текст должен быть непустой строкой.")
        return func(text, *args, **kwargs)
    return wrapper


def log_user_action(func):
    """Декоратор для логирования действий пользователя."""
    def wrapper(*args, **kwargs):
        user_action = func.__name__.replace("_", " ").capitalize()
        logging.info(f"Действие пользователя: {user_action}")
        return func(*args, **kwargs)
    return wrapper


def time_execution(func):
    """
    Декоратор для замера времени выполнения функции.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция '{func.__name__}' выполнялась {execution_time:.4f} секунд.")
        return result
    return wrapper
