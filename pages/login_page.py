class Login_Page:
    textbox_username_id = "user-name"
    textbox_password_id = "password"
    button_login_id = "login-button"
    img_swag_labs_logo_xpath = "//div[@class='login_logo']"
    button_login_id = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def verify_swag_labs_logo_is_dislayed(self):
        return self.driver.find_element_by_xpath(self.img_swag_labs_logo_xpath).is_displayed()

    def verify_login_button_is_dislayed(self):
        return self.driver.find_element_by_id(self.button_login_id).is_displayed()
