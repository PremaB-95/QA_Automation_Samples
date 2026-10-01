from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# Driver Setup
URL= "https://www.automationexercise.com/"
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.maximize_window()
driver.get(URL)
# Locator
Login = (By.XPATH, "//a[@href= '/login']")
# Login Page
driver.find_element(*Login).click()
Login_heading = driver.find_element(By.XPATH, "//div[@class = 'login-form']//h2").text
assert Login_heading == "Login to your account"
# Data Set
login_data = [
    ("stephie3@yopmail.com", "2026"),
    ("stephie3@yopmail.com", "Abc1"),
    ("john3@yopmail.com", "2026"),
]
# Login
def Login(driver, email, password):
    login_form= driver.find_element(By.CLASS_NAME, "login-form")
    login_form.find_element(By.NAME, "email").clear()
    login_form.find_element(By.NAME, "email").send_keys(email)
    login_form.find_element(By.NAME, "password").send_keys(password)
    login_form.find_element(By.CLASS_NAME, "btn-default").click()
    try:
        logout = driver.find_element(By.CLASS_NAME, "fa-lock")
        assert logout.is_displayed(), "Login Successful"
        logout.click()
    except:
        error = driver.find_element(
            By.XPATH, "//p[contains(text(), 'Your email or password is incorrect!')]"
        )
        assert error.is_displayed()
for email, password in login_data:
    Login(driver, email, password)