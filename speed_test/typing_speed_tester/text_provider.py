import random
from typing import List
from lorem_text import lorem  # Для генерации случайного текста
from .exceptions import APIError, InvalidInputError


class TextProvider:
    """
    Класс для предоставления текстов для тестирования скорости набора текста.
    """

    def __init__(self, predefined_texts: List[str] = None):
        """
        Инициализация текстового провайдера.

        :param predefined_texts: Список предопределённых текстов.
        """
        self.predefined_texts = predefined_texts or [
            "Программирование — это искусство, объединяющее логику и креативность.",
            "Python является одним из самых популярных языков программирования.",
            "Эффективная работа требует концентрации и внимания к деталям.",
            "Космос продолжает вдохновлять учёных и исследователей всего мира.",
            "Современные технологии стремительно изменяют нашу жизнь."
        ]

    def get_random_text(self) -> str:
        """
        Возвращает случайный текст из предопределённых или сгенерированный случайным образом.

        :return: Текст для тестирования.
        """
        if random.choice([True, False]):  # 50% шанс взять предопределённый текст
            return random.choice(self.predefined_texts)
        return self._generate_random_text()

    def _generate_random_text(self, word_count: int = 30) -> str:
        """
        Генерирует случайный текст с указанным количеством слов.

        :param word_count: Количество слов в тексте.
        :return: Случайный текст.
        """
        if word_count <= 0:
            raise InvalidInputError("Количество слов должно быть больше 0.")
        try:
            return lorem.words(word_count)
        except Exception as e:
            raise APIError(f"Ошибка при генерации случайного текста: {e}")

    def get_text_by_length(self, length: int) -> str:
        """
        Возвращает текст заданной длины (количество символов).

        :param length: Желаемая длина текста.
        :return: Текст указанной длины.
        """
        if length <= 0:
            raise InvalidInputError("Длина текста должна быть больше 0.")
        text = self.get_random_text()
        while len(text) < length:
            text += " " + self.get_random_text()
        return text[:length]


