import time

class URL1():
    def __init__(self,driver):
        self.driver = driver
        self.signup_xpath = "//*[@id='doc']//div[2]/div/a[1]"
        self.email_xpath = "//input[@name='session[username_or_email]']"
        self.paswd_xpath = "//input[@name='session[password]'][1]"

    def signup(self):
        self.driver.find_element_by_xpath(self.signup_xpath).click()
        time.sleep(2)
        print("Test1Completed")

    def EnterEmail(self,email):
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def EnterPaswd(self, paswd):
        self.driver.find_element_by_xpath(self.paswd_xpath).send_keys(paswd)
