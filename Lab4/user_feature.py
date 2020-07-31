from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import unittest

class test(unittest.TestCase):
    def login(self):
        driver_path = "/Users/weijhehuang/tools/webdriver/chromedriver"
        self.browser = webdriver.Chrome(driver_path)
        self.browser.maximize_window()
        self.browser.get("http://127.0.0.1:3000")
        self.browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul[2]/li[2]/a").click()
        self.browser.find_element_by_name('email').send_keys("demo@keystonejs.com")
        self.browser.find_element_by_name('password').send_keys("demo")
        self.browser.find_element_by_class_name('css-2960tt').submit()
        time.sleep(1)

    def test_1_create_user(self):
        self.login()
        users_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav/div/ul[1]/li[5]/a")
        users_page.click()
        time.sleep(1)
        create_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/div[1]/div[2]/div/div[5]/div/button")
        create_btn.click()
        time.sleep(1)
        self.browser.find_element_by_name('name.first').send_keys("大雄")
        self.browser.find_element_by_name('name.last').send_keys("野比")
        self.browser.find_element_by_name('email').send_keys("demo1@keystonejs.com")
        self.browser.find_element_by_name('password').send_keys("asd1234567")
        self.browser.find_element_by_name('password_confirm').send_keys("asd1234567")
        time.sleep(1)
        submit_btn = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div/form/div[3]/button[1]")
        submit_btn.submit()
        time.sleep(1)
        back_to_users_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/div/div[1]/a")
        back_to_users_page.click()
        time.sleep(1)



if __name__ == "__main__":
    unittest.main()