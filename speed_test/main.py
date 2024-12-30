'''import sys
from typing_speed_tester import TypingTester


def main():
    """
    Главная функция для запуска теста скорости и точности набора текста.
    """
    tester = TypingTester()

    try:
        results = tester.start_test()
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()'''

from typing_speed_tester import TypingTestApp  # Импортируем наш интерфейс

if __name__ == "__main__":
    app = TypingTestApp()
    app.mainloop()


