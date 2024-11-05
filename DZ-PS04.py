from selenium import webdriver  # Импортируем модуль webdriver из библиотеки Selenium для управления браузером
from selenium.webdriver.common.by import By  # Импортируем класс By для указания методов поиска элементов
from selenium.webdriver.common.keys import Keys  # Импортируем класс Keys для работы с клавишами клавиатуры
import time  # Импортируем модуль time для работы с временными задержками


# Функция для получения и отображения параграфов текущей статьи
def get_article(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")  # Находим все элементы с тегом <p> (параграфы)
    for paragraph in paragraphs:
        print(paragraph.text)  # Выводим текст каждого параграфа
    print("\n--- Конец параграфов ---\n")  # Разделитель для конца параграфов


# Функция для получения и отображения ссылок текущей статьи
def get_links(browser):
    links = browser.find_elements(By.CSS_SELECTOR,
                                  "#bodyContent a")  # Находим все ссылки в основном содержимом страницы
    valid_links = []  # Список для хранения валидных ссылок
    link_texts = []  # Список для хранения текста ссылок

    for link in links:
        href = link.get_attribute("href")  # Получаем URL ссылки
        text = link.text.strip()  # Получаем текст ссылки и убираем лишние пробелы
        # Фильтруем ссылки: исключаем файлы и служебные страницы, оставляя только статьи
        if href and text and href.startswith("https://ru.wikipedia.org/wiki/") and not href.startswith(
                "https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B9%D0%BB:"):
            valid_links.append(href)  # Добавляем валидную ссылку в список
            link_texts.append(text)  # Добавляем текст ссылки в список

    # Выводим текст всех валидных ссылок с порядковыми номерами
    for idx, text in enumerate(link_texts):
        print(f"{idx + 1}: {text}")
    return valid_links  # Возвращаем список валидных ссылок


# Главная функция программы
def main():
    user = input("Введите поисковый запрос: ")  # Запрашиваем у пользователя поисковый запрос
    browser = webdriver.Firefox()  # Запускаем браузер Firefox

    try:
        # Переходим на главную страницу Википедии
        browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
        assert "Википедия" in browser.title  # Проверяем, что заголовок страницы содержит "Википедия"

        search_box = browser.find_element(By.ID, "searchInput")  # Находим поле ввода поиска
        search_box.send_keys(user)  # Вводим запрос в поле поиска
        search_box.send_keys(Keys.ENTER)  # Нажимаем Enter для начала поиска

        # Основной цикл программы
        while True:
            # Предлагаем пользователю варианты действий
            print("\nЧто будем делать дальше?")
            print("1: Просмотреть параграфы текущей статьи")
            print("2: Перейти на одну из связанных страниц")
            print("3: Выйти из программы")

            answer = input("Ваш выбор: ")  # Считываем выбор пользователя

            if answer == "1":
                get_article(browser)  # Вызываем функцию для отображения параграфов
            elif answer == "2":
                valid_links = get_links(browser)  # Получаем список валидных ссылок
                if valid_links:
                    link_choice = int(input("Введите номер ссылки для перехода: ")) - 1  # Пользователь выбирает ссылку
                    if 0 <= link_choice < len(valid_links):
                        browser.get(valid_links[link_choice])  # Переходим по выбранной ссылке
                    else:
                        print("Некорректный выбор.")  # Обрабатываем некорректный ввод
                else:
                    print("Связанных страниц не найдено.")  # Если ссылок нет, выводим сообщение
            elif answer == "3":
                print("Всего доброго!")  # Завершаем работу программы
                break  # Выходим из цикла
            else:
                print("Некорректный ввод, попробуйте снова.")  # Сообщение об ошибке ввода

    finally:
        browser.quit()  # Закрываем браузер после завершения работы программы


# Запуск главной функции, если скрипт исполняется напрямую
if __name__ == "__main__":
    main()
