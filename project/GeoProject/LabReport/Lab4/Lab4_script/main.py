from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest
import os

class test(unittest.TestCase):

    def login(self):
        driver_path = os.path.abspath('.') +"/chromedriver"
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

    def test_a_create_first_post(self):
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
        back_to_post_page = self.browser.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div[1]/div/div[1]/a')
        back_to_post_page.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath(
        "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a").text
        time.sleep(1)
        self.browser.close()
        self.assertEqual(result, 'first post')

    def test_b_create_second_post(self):
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
        result = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[2]/td[2]/a").text
        time.sleep(1)
        self.browser.close()
        self.assertEqual(result, 'second post')

    def test_c_edit_first_post(self):
        self.login()
        time.sleep(1)
        self.browser.find_element_by_link_text('Posts').click()
        time.sleep(1)
        first_post = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a")
        first_post.click()
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys('edit-')
        time.sleep(1)
        save_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/form/div[2]/div/div/button[1]")
        save_btn.click()
        time.sleep(1)
        back_to_post_page = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/div/main/div/div/div[1]/div/div[1]/a')
        back_to_post_page.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a").text
        time.sleep(1)
        self.browser.close()
        self.assertEqual(result, 'edit-first post')

    def test_d_search_posts(self):
        self.login()
        time.sleep(1)
        self.browser.find_element_by_link_text('Posts').click()
        time.sleep(1)
        searchBar = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/div[1]/div[1]/div/input")
        searchBar.send_keys("edit-first post")
        time.sleep(1)
        searchResult = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a").text
        self.browser.close()
        self.assertEqual(searchResult, 'edit-first post')

    def test_e_delete_all_post(self):
        self.login()
        time.sleep(1)
        self.browser.find_element_by_link_text('Posts').click()
        time.sleep(1)
        first_post = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a")
        first_post.click()
        time.sleep(1)
        delete_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/form/div[2]/div/div/button[3]")
        delete_btn.click()
        yes_btn = self.browser.find_element_by_class_name('css-t4884')
        yes_btn.click()
        time.sleep(1)
        second_post = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a")
        second_post.click()
        time.sleep(1)
        delete_btn = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/form/div[2]/div/div/button[3]")
        delete_btn.click()
        yes_btn = self.browser.find_element_by_class_name('css-t4884')
        yes_btn.click()
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav[1]/div/ul[1]/li[1]/a").click()
        time.sleep(1)
        result = self.browser.find_element_by_class_name('dashboard-group__list-count').text
        self.browser.close()
        self.assertEqual(result, '0 Items')

    def test_f_create_first_category(self):
        self.login()
        create_category_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div[2]/div/div[1]/div[2]/div[3]/span/a[2]")
        create_category_btn.click()
        time.sleep(1)
        self.browser.find_element_by_name('name').send_keys('first category')
        time.sleep(1)
        create_btn = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/div[3]/button[1]')
        create_btn.submit()
        time.sleep(1)
        back_to_categories_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/div/div[1]/a")
        back_to_categories_page.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[2]/a").text

        self.assertEqual(result, 'first category')

        self.browser.close()


    def test_g_create_comment(self):
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

        result_of_post = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[4]/a").text
        self.browser.close()
        self.assertEqual(result_of_post, 'first post')

    def test_h_edit_comment(self):
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

    def test_i_delete_comment(self):
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

    def test_j_show_posts_of_the_specific_category_by_pressing_category_name_on_the_Blog_page(self):
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
        state_drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-2--value']/div[1]")
        state_drop_down_list.click()
        time.sleep(1)
        selected_publish = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/form/div[1]/div[1]/div/div[3]/div/div/div/div[2]")
        selected_publish.click()
        time.sleep(1)
        author_drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-3--value']/div[1]")
        author_drop_down_list.click()
        time.sleep(1)
        selected_option = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/form/div[1]/div[1]/div/div[4]/div/div/div/div[2]")
        selected_option.click()
        time.sleep(1)
        categories_drop_down_list = self.browser.find_element_by_xpath("//*[@id='react-select-4--value']/div[1]")
        js = "var q=document.documentElement.scrollTop=100000"
        self.browser.execute_script(js)
        time.sleep(3)
        categories_drop_down_list.click()
        time.sleep(1)
        selected_first_category = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[1]/form/div[1]/div[1]/div/div[9]/div/div/div/div[2]")
        selected_first_category.click()
        time.sleep(1)
        save_btn = self.browser.find_element_by_class_name('css-2960tt')
        save_btn.click()
        time.sleep(1)
        back_to_post_page = self.browser.find_element_by_xpath(
            '//*[@id="react-root"]/div/main/div/div/div[1]/div/div[1]/a')
        back_to_post_page.click()
        time.sleep(1)
        global_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav[1]/div/ul[2]/li[1]/a")
        global_btn.click()
        time.sleep(1)
        blog_page = self.browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul[1]/li[2]/a")
        blog_page.click()
        time.sleep(1)
        first_category = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[2]/a")
        first_category.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/article/div[2]/h3/a").text

        self.assertEqual(result, 'first post')

        self.browser.close()

    def test_k_create_enquiry(self):
        self.login()
        global_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav/div/ul[2]/li[1]/a/span")
        global_btn.click()
        time.sleep(1)
        contact_page = self.browser.find_element_by_xpath("//*[@id='navbar-collapse']/ul[1]/li[4]/a")
        contact_page.click()
        time.sleep(1)
        self.browser.find_element_by_name('name.full').send_keys("王小明")
        time.sleep(1)
        self.browser.find_element_by_name('email').send_keys("demo@keystonejs.com")
        time.sleep(1)
        self.browser.find_element_by_name('phone').send_keys("0912345678")
        time.sleep(1)
        regarding = Select(self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div[4]/div/select"))
        regarding.select_by_index(1)
        time.sleep(1)
        self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div[5]/div/textarea").send_keys("Hi ...")
        time.sleep(1)
        submit_btn = self.browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div[6]/div/button")
        submit_btn.submit()
        time.sleep(1)
        admin_ui_btn = self.browser.find_element_by_xpath("/html/body/div/div[1]/a")
        admin_ui_btn.click()
        time.sleep(1)
        name = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[2]/a").text
        email = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[3]/a").text
        enquiry_type = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[4]/div").text

        self.assertEqual(name, '王小明')
        self.assertEqual(email, 'demo@keystonejs.com')
        self.assertEqual(enquiry_type, 'Just leaving a message')

        self.browser.close()

    def test_l_delete_enquiry(self):
        self.login()
        enquiry_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav/div/ul[1]/li[4]/a")
        enquiry_page.click()
        time.sleep(1)
        delete_btn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr/td[1]/button/span")
        delete_btn.click()
        time.sleep(1)
        confirm_btn = self.browser.find_element_by_xpath("/html/body/div[8]/div/div/div/div/div[2]/button[1]")
        confirm_btn.click()
        time.sleep(1)
        result = self.browser.find_element_by_xpath("//*[@id='react-root']/div/main/div/div/div/h2").text

        self.assertEqual(result, 'No enquiries found...')

        self.browser.close()

    def test_m_create_user(self):
        self.login()
        users_page = self.browser.find_element_by_xpath("//*[@id='react-root']/div/header/nav/div/ul[1]/li[5]/a")
        users_page.click()
        time.sleep(1)
        create_btn = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/div[1]/div[2]/div/div[5]/div/button")
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
        back_to_users_page = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/div/div[1]/a")
        back_to_users_page.click()
        time.sleep(1)
        self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[1]/div[1]/div[1]/div/input").send_keys("野比")
        time.sleep(1)
        result = self.browser.find_element_by_xpath(
            "//*[@id='react-root']/div/main/div/div/div[3]/div/div/table/tbody/tr[1]/td[1]/a").text

        self.assertEqual(result, '野比大雄')

        self.browser.close()
if __name__ == "__main__":
    unittest.main()