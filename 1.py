from selenium import webdriver  # Импортируем модуль webdriver из библиотеки Selenium для управления браузером
from selenium.webdriver.common.by import By  # Импортируем класс By для указания методов поиска элементов
from selenium.webdriver import Keys  # Импортируем Keys для использования клавиш клавиатуры
import time  # Импортируем модуль time для работы с временными задержками

# Инициализируем веб-драйвер для Firefox (убедитесь, что у вас установлен geckodriver)
browser = webdriver.Firefox()

# Открываем веб-страницу с указанным URL в браузере
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

# Проверяем, что в заголовке страницы присутствует слово "Википедия"
assert "Википедия" in browser.title

# Задерживаем выполнение программы на 5 секунд, чтобы дать время странице загрузиться
time.sleep(5)

# Находим элемент поля поиска по его ID
search_box = browser.find_element(By.ID, "searchInput")

# Вводим текст "Солнечная система" в поле поиска
search_box.send_keys("Солнечная система")

# Нажимаем клавишу ENTER для выполнения поиска
search_box.send_keys(Keys.ENTER)

# Задерживаем выполнение программы на 5 секунд, чтобы дать время результатам поиска загрузиться
time.sleep(5)

# Находим ссылку с текстом "Солнечная система" и кликаем по ней
a = browser.find_element(By.LINK_TEXT, "Солнечная система")
a.click()

# Задерживаем выполнение программы на 5 секунд, чтобы дать время странице загрузиться
time.sleep(5)

# Закрываем браузер и завершаем сессию веб-драйвера
browser.quit()