import allure
import time

import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


exec_path = 'drivers/chromedriver.exe'


class TestPageSearch:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path=exec_path)

    def teardown(self):
        self.driver.quit()

    @allure.feature('Open pages')
    @allure.story('Открываем страницу google.com')
    @allure.severity('blocker')
    def test_google_search(self):
        self.driver.get('https://google.com')
        with allure.step('Делаем скриншот:'):
            allure.attach(self.driver.get_screenshot_as_png(),name='Screenshot',attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Google'

    @allure.feature('Open pages')
    @allure.story('Открываем страницу yandex.ru')
    @allure.severity('critical')
    def test_yandex_search(self):
        self.driver.get('https://yandex.ru')
        with allure.step('Делаем скриншот:'):
            allure.attach(self.driver.get_screenshot_as_png(),name='Screenshot',attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Яндекс'

    @allure.feature('Open pages')
    @allure.story('Открываем страницу mail.ru')
    @allure.severity('trivial')
    def test_mail_search(self):
        self.driver.get('https://mail.ru')
        with allure.step('Делаем скриншот:'):
            allure.attach(self.driver.get_screenshot_as_png(),name='Screenshot',attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Mail.ru: поч...новости, игры'

    @allure.feature('Open pages')
    @allure.story('Открываем страницу vk.ru')
    @allure.severity('trivial')
    def test_vk_search(self):
        self.driver.get('https://vk.ru')
        with allure.step('Делаем скриншот:'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Добро пожаловать | ВКонтакте'

    @allure.feature('test2')
    @allure.story('Открываем страницу vk.ru')
    @allure.severity('trivial')
    def test_basic_duckduckgo_search(self):
        URL = 'https://duckduckgo.com/'
        PHRASE = 'panda'

        self.driver.get(URL)

        search_input = self.driver.find_element(By.ID,'search_form_input_homepage')
        with allure.step('Делаем скриншот:'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        search_input.send_keys(PHRASE + Keys.RETURN)

        link_divs = self.driver.find_elements(By.CSS_SELECTOR,'#links > div')
        with allure.step('Делаем скриншот:'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert len(link_divs) > 0

        xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
        results = self.driver.find_elements(By.XPATH, xpath)
        with allure.step('Делаем скриншот:'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert len(results) > 0

        search_input = self.driver.find_element(By.ID,'search_form_input')
        with allure.step('Делаем скриншот:'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert search_input.get_attribute('value') == PHRASE

    @allure.feature('test3')
    @allure.story('poisk')
    @allure.severity('critical')
    def test_open_first_email_and_get_subject_name(self):
        try:
            self.driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
               'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
               '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
            self.driver.implicitly_wait(15)
            self.driver.find_element(By.XPATH,'//*[@id ="identifierId"]').send_keys("testpip161@gmail.com")
            self.driver.find_element(By.XPATH,'//*[@id ="identifierNext"]').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH,'//*[@id ="password"]/div[1]/div / div[1]/input').send_keys("Test161pip")
            self.driver.find_element(By.XPATH,'//*[@id ="passwordNext"]').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[2]/div/table/tbody/tr').click()
            subject=self.driver.find_element(By.XPATH , '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td/div[2]/div[1]/div[2]/div[1]/h2')
            with allure.step('Делаем скриншот:'):
             allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
            print(subject.text)
            time.sleep(15)
        except Exception as e:
            with allure.step('Делаем скриншот:'):
             allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
            print(e)
        finally:
            self.driver.close()