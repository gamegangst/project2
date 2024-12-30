import time
from typing import Dict, Tuple
from .text_provider import TextProvider
from .exceptions import InvalidInputError


class TypingTester:
    """
    Класс для тестирования скорости и точности набора текста.
    """

    def __init__(self):
        """
        Инициализация тестера.
        """
        self.text_provider = TextProvider()

    def start_test(self) -> Dict[str, float]:
        """
        Запуск тестирования скорости и точности.

        :return: Результаты тестирования.
        """
        print("Добро пожаловать в тест скорости и точности набора текста!")
        test_text = self.text_provider.get_random_text()
        print("\nВведите текст ниже как можно быстрее и точнее:\n")
        print(f"---\n{test_text}\n---")

        input("Нажмите Enter, когда будете готовы начать...")

        start_time = time.time()  # Засекаем время
        user_input = input("\nНачинайте вводить текст:\n")
        end_time = time.time()  # Засекаем время окончания

        # Рассчитываем результаты
        duration = end_time - start_time
        accuracy = self._calculate_accuracy(test_text, user_input)
        speed = self._calculate_speed(user_input, duration)

        results = {
            "time_taken": duration,
            "accuracy": accuracy,
            "speed": speed,
        }

        self._display_results(results)
        return results

    def _calculate_accuracy(self, original: str, user_input: str) -> float:
        """
        Рассчитывает точность ввода текста.

        :param original: Оригинальный текст.
        :param user_input: Введённый пользователем текст.
        :return: Процент точности.
        """
        original_words = original.split()
        input_words = user_input.split()

        matches = sum(1 for o, i in zip(original_words, input_words) if o == i)
        accuracy = (matches / len(original_words)) * 100 if original_words else 0

        return round(accuracy, 2)

    def _calculate_speed(self, user_input: str, duration: float) -> float:
        """
        Рассчитывает скорость набора текста в символах в минуту (СИМ).

        :param user_input: Введённый пользователем текст.
        :param duration: Время, затраченное на ввод (в секундах).
        :return: Скорость в СИМ.
        """
        if duration <= 0:
            raise InvalidInputError("Время ввода должно быть больше 0.")

        char_count = len(user_input)
        speed = (char_count / duration) * 60  # СИМ
        return round(speed, 2)

    def _display_results(self, results: Dict[str, float]):
        """
        Выводит результаты тестирования пользователю.

        :param results: Результаты тестирования.
        """
        print("\nРезультаты тестирования:")
        print(f"Время: {results['time_taken']:.2f} сек")
        print(f"Точность: {results['accuracy']}%")
        print(f"Скорость: {results['speed']} символов в минуту")
