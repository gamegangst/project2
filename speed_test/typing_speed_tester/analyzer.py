from decorators import log_execution_time, validate_input
from exceptions import InvalidInputError, InsufficientDataError


@log_execution_time
@validate_input
def calculate_speed(text: str, time_taken: float) -> float:
    """
    Рассчитывает скорость набора текста в словах в минуту (WPM).

    :param text: Текст, набранный пользователем.
    :param time_taken: Время (в секундах), затраченное на набор текста.
    :return: Скорость набора текста в словах в минуту (WPM).
    """
    if time_taken <= 0:
        raise ValueError("Время должно быть больше 0.")

    words = len(text.split())
    if words == 0:
        raise InsufficientDataError("Текст слишком короткий для расчета скорости.")

    words_per_minute = words / time_taken * 60
    return round(words_per_minute, 2)


@log_execution_time
@validate_input
def calculate_accuracy(user_input: str, reference_text: str) -> float:
    """
    Рассчитывает точность набора текста в процентах.

    :param user_input: Текст, набранный пользователем.
    :param reference_text: Эталонный текст, с которым сравнивается ввод пользователя.
    :return: Точность набора текста в процентах.
    """
    if not isinstance(reference_text, str) or not reference_text.strip():
        raise InvalidInputError("Эталонный текст должен быть непустой строкой.")

    reference_words = reference_text.split()
    user_words = user_input.split()

    total_words = max(len(reference_words), len(user_words))
    if total_words == 0:
        raise InsufficientDataError("Недостаточно слов для расчета точности.")

    correct_words = sum(1 for u, r in zip(user_words, reference_words) if u == r)
    accuracy = correct_words / total_words * 100
    return round(accuracy, 2)

