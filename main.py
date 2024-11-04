from selenium import webdriver  # Импортируем модуль webdriver из библиотеки Selenium для управления браузером
import time  # Импортируем модуль time для работы с временными задержками

# Инициализируем веб-драйвер для Firefox (убедитесь, что у вас установлен geckodriver)
browser = webdriver.Firefox()

# Открываем веб-страницу с указанным URL в браузере
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")

# Задерживаем выполнение программы на 5 секунд, чтобы дать время странице загрузиться
time.sleep(5)

# Закомментированная строка: сохраняет скриншот текущей страницы в файл "dom.png"
# browser.save_screenshot("dom.png")

# Открываем новую веб-страницу с указанным URL в браузере
browser.get("https://en.wikipedia.org/wiki/Selenium")

# Задерживаем выполнение программы на 3 секунды, чтобы дать время странице загрузиться
time.sleep(3)

# Закомментированная строка: сохраняет скриншот текущей страницы в файл "selenium.png"
# browser.save_screenshot("selenium.png")

# Обновляем текущую страницу в браузере
browser.refresh()

# Закомментированная строка: закрывает браузер и завершает сессию веб-драйвера
# browser.quit()