from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import Client




class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://mattylyd.pythonanywhere.com/admin')
        self.browser.find_element_by_name('username').send_keys("MDR824")
        time.sleep(1)
        self.browser.find_element_by_name('password').send_keys("DjangoTest123")
        time.sleep(1)
        self.browser.find_element_by_xpath("//input[@value='Log in']").click()
        time.sleep(1)


    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Load main site click add new
        self.browser.get('http://mattylyd.pythonanywhere.com')
        self.assertIn("Matt R-J\'s CV" , self.browser.title)
        header = self.browser.find_element_by_tag_name('h1')
        self.assertIn('Click to Enter', header.text)
        header.click()
        self.assertIn("Matt R-J\'s CV" , self.browser.title)
        title = self.browser.find_element_by_xpath("//h1/a")
        self.assertIn("Matt R-J\'s CV" , title.text)
        time.sleep(2)
        plus = self.browser.find_element_by_class_name("fas.fa-plus")
        plus.click()

        #Load new site and add new post
        new = self.browser.find_element_by_tag_name("h2")
        self.assertIn("New post", new.text)
        self.browser.find_element_by_class_name("fas.fa-plus")
        self.browser.find_element_by_name("title").send_keys("FT Title")
        self.browser.find_element_by_name("text").send_keys("FT text")
        self.browser.find_element_by_name("start_date").click()
        actions = ActionChains(self.browser)
        actions.send_keys('29062020')
        actions.perform()
        self.browser.find_element_by_name("end_date").click()
        actions = ActionChains(self.browser)
        actions.send_keys('28062020')
        actions.perform()
        self.browser.find_element_by_class_name("save.btn.btn-default").click()

        #Show no ptag
        #Dates wrong way round produce error
        error=self.browser.find_element_by_name("error")
        self.assertEqual(error.text, "Date invalid")

        #Dates fixed should submit
        self.browser.find_element_by_name("start_date").click()
        actions = ActionChains(self.browser)
        actions.send_keys('27062020')
        actions.perform()
        self.browser.find_element_by_name("end_date").click()
        actions = ActionChains(self.browser)
        actions.send_keys('28062020')
        actions.perform()
        self.browser.find_element_by_class_name("save.btn.btn-default").click()
        time.sleep(2)

        #Check for pencil icon to see if on post detail
        pencil = self.browser.find_element_by_class_name("fas.fa-pen")
        self.assertEqual(pencil.get_attribute("class"), "fas fa-pen")

        #Get back to post list
        #Find id of created post
        id = self.browser.current_url
        for i in range(len(id)-1):
            print(i)
            if(id[i] == "/" and id[i+1]=="p"):
                id = id[i:]
                break

        self.browser.find_element_by_xpath("//h1/a").click()
        time.sleep(2)
        title = self.browser.find_element_by_xpath("//a[@href='"+id+"']")
        self.assertEqual(title.text, "FT Title")
        title.click()
        time.sleep(2)
        #Edit post
        self.browser.find_element_by_class_name("fas.fa-pen").click()
        time.sleep(2)
        self.browser.find_element_by_name("title").clear()
        self.browser.find_element_by_name("title").send_keys("FT Title Edit")
        self.browser.find_element_by_class_name("save.btn.btn-default").click()
        self.browser.find_element_by_xpath("//h1/a").click()
        time.sleep(2)
        #Check it's still there after edit
        title = self.browser.find_element_by_xpath("//a[@href='"+id+"']")
        title.click()
        title = self.browser.find_element_by_tag_name("h2")
        self.assertEqual("FT Title Edit", title.text)
        #Delete Post
        self.browser.find_element_by_class_name("fas.fa-trash").click()
        #Check it's deleted
        find = self.browser.find_elements_by_xpath("//*[contains(text(),'" + "FT Title Edit" + "')]");
        self.assertTrue("Text not found!", len(find) > 0)








if __name__ == '__main__':
    unittest.main(warnings='ignore')