from selenium import webdriver  # Импортируем модуль webdriver из библиотеки Selenium для управления браузером
from selenium.webdriver.common.by import By  # Импортируем класс By для указания методов поиска элементов
from selenium.webdriver import Keys  # Импортируем Keys для использования клавиш клавиатуры
import time  # Импортируем модуль time для работы с временными задержками

user = input("Введите поисковый запрос: ")
browser = webdriver.Firefox()

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

assert "Википедия" in browser.title

search_box = browser.find_element(By.ID, "searchInput")

search_box.send_keys(user)
search_box.send_keys(Keys.ENTER)

print("Что будем делать дальше?")
print("Нажмите 1, если хотите просмотреть параграфы")
print("Нажмите 2, если хотите перейти на одну из связанных страниц")
print("Нажмите 3, если хотите выйти")


answer = int(input("Ваш выбор: "))

if answer == 1:
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)

if answer == 2:
    links = browser.find_elements(By.TAG_NAME, "a")
    for link in links:
        print(link.get_attribute("href"))

if answer == 3:
    print("Всего доброго!")
    browser.quit()

#browser.quit()

