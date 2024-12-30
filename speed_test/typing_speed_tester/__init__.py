# Этот файл делает директорию полноценным пакетом Python.
# Здесь можно инициализировать глобальные переменные или импортировать модули для удобства использования.

from .tester import TypingTester
from .text_provider import TextProvider
from .exceptions import InvalidInputError, InsufficientDataError
from .decorators import time_execution
from .gui import TypingTestApp  # Импортируем интерфейс (класс приложения)

# Если нужно, можно инициализировать экземпляры классов или другие компоненты:
typing_tester = TypingTester()  # Инициализируем тестер для использования в пакете
text_provider = TextProvider()  # Инициализируем провайдер текста, если требуется

# Добавление классов и функций в __all__ для удобства импорта
__all__ = [
    "TypingTester",
    "TextProvider",
    "InvalidInputError",
    "InsufficientDataError",
    "time_execution",
    "TypingTestApp",  # Теперь интерфейс доступен через этот импорт
    "typing_tester",  # Экземпляр TypingTester
    "text_provider"   # Экземпляр TextProvider
]
