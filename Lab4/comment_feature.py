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

    def delete_post(self):
        self.browser.find_element_by_link_text('Posts').click()
        time.sleep(1)
        first_post = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a")
        first_post.click()
        time.sleep(1)
        delete_btn = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/form/div[2]/div/div/button[3]")
        delete_btn.click()
        yes_btn = self.browser.find_element_by_class_name('css-t4884')
        yes_btn.click()
        time.sleep(1)

    def create_first_post(self):
        self.login()
        post_page = self.browser.find_element_by_link_text('Posts')
        post_page.click()
        time.sleep(1)
        create_post_button = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/button")
        create_post_button.click()
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys("first post")
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys(Keys.ENTER)
        time.sleep(1)
        drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-3--value']/div[1]")
        drop_down_list.click()
        time.sleep(1)
        selected_option = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/form/div[1]/div[1]/div/div[4]/div/div/div/div[2]")
        selected_option.click()
        time.sleep(1)
        save_btn = self.browser.find_element_by_class_name('css-2960tt')
        save_btn.click()
        time.sleep(1)
        back_to_post_page = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div[1]/div/div[1]/a')
        back_to_post_page.click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav[1]/div/ul[1]/li[1]/a").click()
        time.sleep(1)

    def test_1_create_comment(self):
        self.create_first_post()
        create_comment_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div[2]/div/div[1]/div[2]/div[2]/span/a[2]")
        create_comment_btn.click()
        time.sleep(1)
        author_drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-5--value']")
        author_drop_down_list.click()
        time.sleep(1)
        selected_author_option = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/form/div[2]/div[1]/div/div/div/div[2]")
        selected_author_option.click()
        time.sleep(1)
        post_drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-6--value']")
        post_drop_down_list.click()
        selected_post_option = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/form/div[2]/div[2]/div/div/div/div[2]")
        selected_post_option.click()
        time.sleep(1)
        create_btn = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/form/div[3]/button[1]")
        create_btn.click()
        time.sleep(1)
        back_to_comments_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/div/div[1]/a")
        back_to_comments_page.click()
        time.sleep(1)

        result_of_author = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[3]/a").text
        result_of_post = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[4]/a").text
        self.browser.close()
        self.assertEqual(result_of_post, 'first post')

    def test_2_edit_comment(self):
        self.login()
        comment_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div[2]/div/div[1]/div[2]/div[2]/span/a[1]/div[1]")
        comment_page.click()
        time.sleep(1)
        first_coment = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a")
        first_coment.click()
        time.sleep(1)
        comment_state_drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/form/div[1]/div[1]/div/div[4]/div/div/div/div/span[2]")
        comment_state_drop_down_list.click()
        time.sleep(1)
        selected_option = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/form/div[1]/div[1]/div/div[4]/div/div/div/div[2]")
        selected_option.click()
        time.sleep(1)
        save_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/form/div[2]/div/div/button[1]")
        save_btn.click()
        time.sleep(1)
        back_to_comments_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/div/div[1]/a")
        back_to_comments_page.click()
        time.sleep(1)
        comment_state = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[6]/div").text
        self.browser.close()
        self.assertEqual(comment_state, 'Draft')

    def test_3_delete_comment(self):
        self.login()
        comment_page = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div[2]/div/div[1]/div[2]/div[2]/span/a[1]/div[1]")
        comment_page.click()
        time.sleep(1)
        first_coment = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a")
        first_coment.click()
        time.sleep(1)
        delete_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/form/div[2]/div/div/button[3]")
        delete_btn.click()
        time.sleep(1)
        confirm_btn = self.browser.find_element_by_class_name('css-t4884')
        confirm_btn.click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav[1]/div/ul[1]/li[1]/a").click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div[2]/div/div[1]/div[2]/div[2]/span/a[1]/div[2]").text

        self.assertEqual(result, '0 Items')
        self.delete_post()
        self.browser.close()

if __name__ == "__main__":
    unittest.main()