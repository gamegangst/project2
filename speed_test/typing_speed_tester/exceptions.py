class TypingTestError(Exception):
    """Базовый класс для всех пользовательских исключений в проекте."""
    pass


class InvalidInputError(TypingTestError):
    """Ошибка ввода: текст должен быть непустой строкой."""
    def __init__(self, message="Входной текст должен быть непустой строкой."):
        super().__init__(message)


class TimeLimitExceededError(TypingTestError):
    """Ошибка, если пользователь превысил ограничение по времени."""
    def __init__(self, time_limit, message=None):
        if message is None:
            message = f"Превышено ограничение по времени: {time_limit} секунд."
        super().__init__(message)
        self.time_limit = time_limit


class TestNotStartedError(TypingTestError):
    """Ошибка, если пользователь пытается завершить тест, не начав его."""
    def __init__(self, message="Тест не был начат. Пожалуйста, начните тест перед завершением."):
        super().__init__(message)


class InsufficientDataError(TypingTestError):
    """Ошибка, если данных недостаточно для анализа."""
    def __init__(self, message="Недостаточно данных для выполнения анализа."):
        super().__init__(message)


class APIError(TypingTestError):
    """Ошибка взаимодействия с внешним API."""
    def __init__(self, message="Ошибка при обращении к внешнему API. Проверьте подключение к сети."):
        super().__init__(message)
