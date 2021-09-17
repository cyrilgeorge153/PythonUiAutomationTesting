class Home_Page:
    heading_products_xpath = "//span[@class='title']"
    link_your_cart_xpath = "//a[@class='shopping_cart_link']"

    def __init__(self, driver):
        self.driver = driver

    def verify_products_heading_is_dislayed(self):
        return self.driver.find_element_by_xpath(self.heading_products_xpath).is_displayed()

    def verify_your_cart_link_is_dislayed(self):
        return self.driver.find_element_by_xpath(self.link_your_cart_xpath).is_displayed()
