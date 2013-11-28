from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CourseSection(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_course_section(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/")
        driver.find_element_by_xpath("(//a[contains(text(),'Add')])[7]").click()
        driver.find_element_by_id("id_section_no").clear()
        driver.find_element_by_id("id_section_no").send_keys("SWENG")
        driver.find_element_by_css_selector("img[alt=\"Add Another\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | id_course | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=id_course | ]]
        driver.find_element_by_id("id_name").clear()
        driver.find_element_by_id("id_name").send_keys("Software Testing")
        driver.find_element_by_id("id_full_name").clear()
        driver.find_element_by_id("id_full_name").send_keys("Software testing with unit tests")
        driver.find_element_by_id("id_schedule_no").clear()
        driver.find_element_by_id("id_schedule_no").send_keys("105")
        driver.find_element_by_link_text("Today").click()
        driver.find_element_by_css_selector("#calendarlink1 > img[alt=\"Calendar\"]").click()
        driver.find_element_by_css_selector("#calendarbox1 > div > a.calendarnav-next").click()
        driver.find_element_by_link_text("31").click()
        driver.find_element_by_name("_save").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_name("_save").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
