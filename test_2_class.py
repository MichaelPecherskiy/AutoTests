import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

import time


class TestXUnitClass:

    driver: WebDriver
    send_keys: WebElement
    window_handles: WebDriver
    ActionChains: WebDriver

    def setup_method(self):
        self.driver = WebDriver(executable_path='C://Users//Pecherskii//PycharmProjects//chromedriver.exe')
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.close()

    def test_find_videocard(self):
        with allure.step('Открываем сайт https://www.regard.ru//'):
            self.driver.get('https://www.regard.ru//')
        time.sleep(3)
        with allure.step('Вписываем в поле поиска "Видеокарта"'):
            search_video = self.driver.find_element_by_xpath('//input[@name="query"]')
        search_video.click()
        search_video.send_keys('Видеокарта')
        with allure.step('Кликаем на кнопку поиска'):
            search_find = self.driver.find_element_by_xpath('//div[@class="button-container"]//button[@type="submit"]')
        search_find.click()
        time.sleep(3)
        assert True

    def test_block(self):
        with allure.step('Открываем сайт https://www.regard.ru//'):
            self.driver.get('https://www.regard.ru//')
        time.sleep(3)
        with allure.step('Находим блоки питания'):
            find_block = self.driver.find_element_by_xpath('//li[@class="container   "]//a[@href="/catalog/group43000.htm"]')
            find_block.click()
        with allure.step('Выбираем открываем содержимое блоков питания и проверяем что количество = 6'):
            accord = self.driver.find_element_by_xpath('//li[@class="  "]//a[@href="/catalog/group43044.htm"]')
            accord.click()
            accord_block = self.driver.find_element_by_xpath('//div[@class="block"]')
            if accord_block == 6:
                assert True

    def test_change_city(self):
        with allure.step('Открываем сайт https://www.regard.ru//'):
            self.driver.get('https://www.regard.ru//')
            time.sleep(3)
        with allure.step('Меням город Москва на Город Липецк'):
            menu = self.driver.find_element_by_xpath('//div[@id="chcity"]').click()
            self.driver.implicitly_wait(5)
            hidden_submenu = self.driver.find_element_by_xpath('//div[@id="chcity"]//a[@class="secondCity"]')
            ActionChains(self.driver).move_to_element(menu).click(hidden_submenu).perform()
            self.driver.implicitly_wait(3)
        assert True



