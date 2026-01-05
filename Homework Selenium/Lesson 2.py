import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://hyperskill.org/")

go_button = driver.find_element("xpath", "//div[text()='Let’s go']")
assert go_button.text == "Let’s go", "Кнопка Let’s go не найдена"
go_button.click()

driver.find_element("xpath", "//li[contains(@class, 'nav-item')]/a[@class='nav-link' and @href='#']").click()
time.sleep(1)
driver.find_element("xpath", "//a[contains (@class, 'dropdown-toggle')]").click()
time.sleep(1)

python_button = driver.find_element("xpath", "//section/a[text()='Python']")
python_button.click()
time.sleep(5)

assert "Hyperskill" in driver.title, "Неверный заголовок страницы"
assert "https://hyperskill.org/categories/1" == driver.current_url, "Неверный URL страницы"

