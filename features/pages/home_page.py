from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class HomePage:

    URL = "https://www.demoblaze.com/index.html"
    CAROUSEL_SELECTOR = (By.XPATH, "//div[@class='carousel-inner']")
    CAROUSEL_ACTIVE_IMAGE_SELECTOR = (By.XPATH, "//div[@class='carousel-item active']")
    CAROUSEL_FIRST_IMAGE = (By.XPATH, "//img[@alt='First slide']")
    CAROUSEL_SECOND_IMAGE = (By.XPATH, "//img[@alt='Second slide']")
    CAROUSEL_THIRD_IMAGE = (By.XPATH, "//img[@alt='Third slide']")
    CAROUSEL_NEXT = (By.XPATH, "//a[@data-slide='next']")
    CAROUSEL_PREVIOUS = (By.XPATH, "//a[@data-slide='prev']")

    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get(HomePage.URL)

    def hover_mouse_on_carousel_images(self):
        carousel = self.driver.find_element(*HomePage.CAROUSEL_SELECTOR)
        hover = ActionChains(self.driver).move_to_element(carousel)
        hover.perform()

    def check_carousel_current_image(self):
        current_image = self.driver.find_element(*HomePage.CAROUSEL_ACTIVE_IMAGE_SELECTOR)
        image = current_image.find_element(By.TAG_NAME, "img")
        image_name = image.get_attribute("src")
        print(image_name)
        return image_name




