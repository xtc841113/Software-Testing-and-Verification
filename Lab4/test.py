from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

    def qtest_2_create_second_post(self):
        self.login()
        time.sleep(1)
        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div[2]/div/div[1]/div[2]/div[1]/span/a[2]").click()
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys("second post")
        time.sleep(1)
        create_btn = self.browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div/form/div[3]/button[1]')
        create_btn.click()
        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='mceu_11']/button").click()
        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='mceu_55']").send_keys("<p>Hi ...</p>")
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='mceu_57']/button").click()
        time.sleep(1)


        js = "var q=document.documentElement.scrollTop=200"
        self.browser.execute_script(js)
        time.sleep(1)


        self.browser.find_element_by_xpath("//*[@id='mceu_37']/button/i").click()
        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='mceu_62']").send_keys("<p>Hello World!</p>")
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='mceu_64']/button").click()
        time.sleep(1)


        save_btn = self.browser.find_element_by_class_name('css-2960tt')
        save_btn.click()
        time.sleep(1)
        back_to_post_page = self.browser.find_element_by_xpath("//*[@id='mceu_127']")
        back_to_post_page.click()
        time.sleep(1)
        self.browser.close()

    def test_1(self):
        self.login()
        users_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav/div/ul[1]/li[5]/a")
        users_page.click()
        time.sleep(1)
        create_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/div[1]/div[2]/div/div[5]/div/button")
        create_btn.click()
        time.sleep(1)
        self.browser.find_element_by_name('name.first').send_keys("大雄")
        self.browser.find_element_by_name('name.last').send_keys("野比")
        self.browser.find_element_by_name('email').send_keys("d1@keystonejs.com")
        self.browser.find_element_by_name('password').send_keys("asd1234567")
        self.browser.find_element_by_name('password_confirm').send_keys("asd1234567")
        time.sleep(1)
        submit_btn = self.browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div/form/div[3]/button[1]")
        submit_btn.submit()
        time.sleep(1)
        back_to_users_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/div/div[1]/a")
        back_to_users_page.click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/div[1]/div[1]/div/input").send_keys("野比")
        time.sleep(1)
        result = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/a").text

        self.assertEqual(result, '野比大雄')

        self.browser.close()
if __name__ == "__main__":
    unittest.main()