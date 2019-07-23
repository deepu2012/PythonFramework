#CONSTANTS
import inspect
import moment
import allure

TwitterURL = "https://twitter.com"
LinkedURL = "https://linkedin.com"
EmailID = "MyQACoach@gmail.com"
Password = "MyHero"


def whoami():
    return inspect.stack()[1][3]


def capture_screen(self, driver, test_name):
    self.driver = driver
    t = moment.now().strftime('%d-%m-%y_%H-%M-%S')
    test_name = test_name +"_"+t
    allure.attach(self.driver.get_screenshot_as_png(),
                  name = test_name,
                  attachment_type=allure.attachment_type.PNG)
    # Save physical copy of report in screenshot folder
    self.driver.get_screenshot_as_file("/Users/jaijeetpandey/PycharmProjects/MyFramework/screenshots/"
                                       +test_name+'.png')
