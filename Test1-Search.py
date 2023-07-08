import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Edge при начале каждого теста
        self.driver = webdriver.Edge()

    def test_search_in_python_org(self):
        driver = self.driver
        # открытие в Edge страницы http://www.instituteiba.by
        driver.get("http://www.instituteiba.by")
        # проверка наличия фразы в заголовке страницы
        self.assertIn("Курсы программирования в Минске", driver.title)
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы с именем q (строка поиска)
        # (откройте вручную в любом браузере сайт http://www.instituteiba.by,
        # нажмите правой кнопкой мыши по строке поиска,
        # выберите пункт "просмотреть код",
        # убедитесь, что у этого элемента name="q")
        elem = driver.find_element(By.NAME, "q")
        # ждем 5 секунд
        time.sleep(5)
        # набор слова chupakabra в найденном элементе
        elem.send_keys("barbados")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия строки "No results found."
        # на странице с результатами поиска
        self.assertIn("К сожалению, на ваш поисковый запрос ничего не найдено.", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)
        # получение элемента страницы с именем q
        # на обновленной странице
        elem = driver.find_element(By.NAME, "q")
        # очищаем строку поиска
        elem.clear()
        # ждем 5 секунд
        time.sleep(5)
        # набор слова dilinjer в найденном элементе
        elem.send_keys("dilinjer")
        # ждем 5 секунд
        time.sleep(5)
        # нажатие кнопки Enter в найденном элементе
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка отсутствия строки "No results found."
        # на странице с результатами поиска
        self.assertIn("К сожалению, на ваш поисковый запрос ничего не найдено.", driver.page_source)

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

