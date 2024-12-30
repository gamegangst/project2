import tkinter as tk
import time
from typing import Dict
from .text_provider import TextProvider
from .exceptions import InvalidInputError

class TypingTestApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Typing Speed Tester")
        self.geometry("1400x800")

        self.text_provider = TextProvider()
        self.test_text = self.text_provider.get_random_text()

        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self, text="Введите текст ниже как можно быстрее и точнее:", wraplength=550)
        self.instruction_label.pack(pady=10)

        self.text_display = tk.Label(self, text=self.test_text, font=("Helvetica", 14), wraplength=550)
        self.text_display.pack(pady=20)

        self.user_input_label = tk.Label(self, text="Ваш ввод:")
        self.user_input_label.pack()

        self.user_input = tk.Entry(self, width=50)
        self.user_input.pack(pady=10)

        self.start_button = tk.Button(self, text="Начать тест", command=self.start_test)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self, text="Остановить тест", command=self.stop_test, state="disabled")
        self.stop_button.pack(pady=10)

        self.results_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.results_label.pack(pady=10)

    def start_test(self):
        self.start_time = time.time()
        self.start_button.config(state="disabled")  # Отключаем кнопку старта
        self.stop_button.config(state="normal")  # Включаем кнопку остановки

        self.user_input.delete(0, tk.END)  # Очищаем поле ввода

        self.after(100, self.check_input)

    def check_input(self):
        """
        Проверяет, ввел ли пользователь весь текст и завершился ли тест.
        """
        user_input = self.user_input.get()

        if user_input == self.test_text:
            self.end_test()
        else:
            self.after(100, self.check_input)

    def stop_test(self):
        """
        Останавливает тест по запросу пользователя.
        """
        self.end_test(stop=True)

    def end_test(self, stop=False):
        """
        Завершает тест и выводит результаты.
        """
        end_time = time.time()
        duration = end_time - self.start_time

        # Если тест был остановлен вручную, то показываем результат с учетом времени до остановки
        if stop:
            duration = time.time() - self.start_time

        accuracy = self.calculate_accuracy(self.test_text, self.user_input.get())
        speed = self.calculate_speed(self.user_input.get(), duration)

        results = {
            "time_taken": duration,
            "accuracy": accuracy,
            "speed": speed,
        }

        self.display_results(results)

        # Включаем кнопки снова
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def calculate_accuracy(self, original: str, user_input: str) -> float:
        original_words = original.split()
        input_words = user_input.split()

        matches = sum(1 for o, i in zip(original_words, input_words) if o == i)
        accuracy = (matches / len(original_words)) * 100 if original_words else 0

        return round(accuracy, 2)

    def calculate_speed(self, user_input: str, duration: float) -> float:
        if duration <= 0:
            raise InvalidInputError("Время ввода должно быть больше 0.")

        char_count = len(user_input)
        speed = (char_count / duration) * 60  # СИМ
        return round(speed, 2)

    def display_results(self, results: Dict[str, float]):
        result_text = (
            f"Время: {results['time_taken']:.2f} сек\n"
            f"Точность: {results['accuracy']}%\n"
            f"Скорость: {results['speed']} символов в минуту"
        )

        self.results_label.config(text=result_text)
