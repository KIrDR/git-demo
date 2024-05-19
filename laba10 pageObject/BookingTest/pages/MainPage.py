from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.CSS_SELECTOR, "a[data-testid='header-sign-in-button']")
        self.email_input = (By.CSS_SELECTOR, "input[type='email']")
        self.continue_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.sign_in_submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.account_button = (By.CLASS_NAME, "a83ed08757")  # Обновленный селектор
        self.manage_account_button = (By.LINK_TEXT, "Управлять аккаунтом")
        self.personal_details_button = (By.XPATH, "//h2[contains(text(),'Персональные данные')]/../span/span")
        self.edit_birth_date_button = (By.CSS_SELECTOR, "button[data-ga-label='Edit section: dateOfBirth']")
        self.day_input = (By.NAME, "dateOfBirth__day")
        self.month_select = (By.NAME, "dateOfBirth__month")
        self.year_input = (By.NAME, "dateOfBirth__year")
        self.save_birth_date_button = (By.CSS_SELECTOR, "button[data-ga-label='Save section: dateOfBirth']")
        self.birth_date_error_message = (By.ID, ":r1s:-note")
        self.phone_input = (By.NAME, "phoneNumber")
        self.phone_error_message = (By.XPATH, "//div[contains(text(),'Введите действительный номер телефона и код страны')]")

    def click_sign_in_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.sign_in_button)).click()

    def enter_email(self, email):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.email_input)).send_keys(email)

    def click_continue_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.continue_button)).click()

    def enter_password(self, password):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_sign_in_submit_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.sign_in_submit_button)).click()

    def get_logged_in_user_name(self):
        return WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.a3332d346a.a6a383700c"))).text

    def click_account_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.account_button)).click()

    def click_manage_account_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.manage_account_button)).click()

    def click_personal_details_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.personal_details_button)).click()

    def click_edit_birth_date_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.edit_birth_date_button)).click()

    def enter_birth_date(self, day, month, year):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.day_input)).send_keys(day)
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.month_select)).send_keys(month)
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.year_input)).send_keys(year)

    def click_save_birth_date_button(self):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(self.save_birth_date_button)).click()

    def get_birth_date_error_message(self):
        return WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.birth_date_error_message)).text

    def enter_phone_number(self, phone_number):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.phone_input)).send_keys(phone_number)

    def get_phone_error_message(self):
        return WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(self.phone_error_message)).text
