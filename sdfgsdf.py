import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

exec_path = 'drivers/chromedriver.exe'
driver = webdriver.Chrome(executable_path=exec_path)

try:
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
                    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
                    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    driver.implicitly_wait(15)
    driver.find_element(By.XPATH, '//*[@id ="identifierId"]').send_keys("testpip161@gmail.com")
    driver.find_element(By.XPATH, '//*[@id ="identifierNext"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id ="password"]/div[1]/div / div[1]/input').send_keys("Test161pip")
    driver.find_element(By.XPATH, '//*[@id ="passwordNext"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,
                             '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div[8]/div/div[1]/div[2]/div/table/tbody/tr').click()
    subject = driver.find_element(By.XPATH,
                                       '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div/table/tr/td/div[2]/div[1]/div[2]/div[1]/h2')
    with allure.step('Делаем скриншот:'):
        allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    print(subject.text)
    time.sleep(15)
except Exception as e:
    with allure.step('Делаем скриншот:'):
        allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    print(e)
finally:
    driver.close()