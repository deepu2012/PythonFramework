from selenium import webdriver
from pages.URL1 import URL1
from utils import utils
import pytest
import time




class Test_Launch_URL():
    @pytest.fixture()
    def test_setup(self):
        global driver
        # driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
        driver = webdriver.Chrome(executable_path="/Users/jaijeetpandey/PycharmProjects/MyFramework/drivers/chromedriver")
        driver.implicitly_wait(2)
        driver.maximize_window()
        print ("Window Maximised")
        yield
        driver.close()
        driver.quit()
        print ("Test Completed")


    def test_launchURL_1(self,test_setup):
        driver.get(utils.TwitterURL)
        twitter = URL1(driver)
        twitter.EnterEmail(utils.EmailID)
        twitter.EnterPaswd(utils.Password)
        twitter.signup()

    def test_launchURL_2(self,test_setup):
        try :
            driver.get("https://linkedin.com")
            print ("Url Launched_2")
            assert driver.title=="LinkedIn: Log In or Sign Up1"
            driver.find_element_by_xpath("//nav[@class='nav']/a[@href='https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin']").click()
            driver.find_element_by_xpath("//input[@id='username']").send_keys("myqacoach@gmail.com")
            time.sleep(2)
        except AssertionError as e:
            print ('Error Occured')
            print (e)
            utils.capture_screen(self,driver,utils.whoami())

        finally:
            print ("Test2Completed")




