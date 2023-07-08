import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Edge при начале каждого теста
        self.driver = webdriver.Edge()

    def test_login_logout(self):
        driver = self.driver
        # открытие в Edge страницы https://ru.ucoin.net/login
        # на которой есть кнопка Вход
        driver.get("https://ru.ucoin.net/login")
        # ждем 5 секунд
        time.sleep(5)
        # # поиск ссылки с текстом "Вход"
        # elem = driver.find_element(By.NAME, "Вход")
        # # нажатие на ссылку
        # elem.click()
        # # ждем 5 секунд
        # time.sleep(5)
        # поиск текстового поля для ввода логина по XPath
        # (тег input с name='login')
        elem = driver.find_element(By.NAME, "email")
        # ввод логина
        elem.send_keys("anton_kurach@tut.by")
        # ждем 5 секунд
        time.sleep(5)
        # поиск текстового поля для ввода пароля по XPath
        # (тег input с name='password')
        elem = driver.find_element(By.NAME, "passwd")
        # ввод логина
        elem.send_keys("15sePt2012")
        # ждем 5 секунд
        time.sleep(5)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия на странице строки "Your account"
        # после входа
        self.assertIn("Антон из деревни", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)
        # вывод кода страницы для отладки, потом можно будет убрать
        print(driver.page_source)
        # поиск ссылки с текстом "Sign out"
        # elem = driver.find_element(By.NAME, "Выход")
        # # нажатие на ссылку
        # elem.click()
        driver.get("https://ru.ucoin.net/?logout=1")
        # ждем 5 секунд
        time.sleep(5)
        # поиск кнопки на форме в главной области страницы
        # по CSS-селектору
        elem = driver.find_element(By.LINK_TEXT, '/?logout=1')
        # нажатие на кнопку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)
        # проверка отсутствия на странице строки "Your account"
        # после выхода
        self.assertNotIn("Статистика", driver.page_source)


    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
