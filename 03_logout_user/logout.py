# Verify that home page is visible successfully
# Click on 'Signup / Login' button
# Verify 'Login to your account' is visible
# Enter correct email address and password
# Click 'login' button
# Verify that 'Logged in as username' is visible
# Click 'Logout' button
# Verify that user is navigated to login page
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
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
# Login
def Login(driver, email, password):
    login_form= driver.find_element(By.CLASS_NAME, "login-form")
    login_form.find_element(By.NAME, "email").clear()
    login_form.find_element(By.NAME, "email").send_keys(email)
    login_form.find_element(By.NAME, "password").send_keys(password)
    login_form.find_element(By.CLASS_NAME, "btn-default").click()
    try:
        username = "Stephie"
        user_detail = driver.find_element(By.XPATH,"//a[contains(., 'Logged in as')]")
        assert f"Logged in as {username}" in user_detail.text
        print(user_detail.text)
    except:
        print("try again")
Login(driver, "stephie3@yopmail.com" , "2026")
logout = driver.find_element(By.CLASS_NAME, "fa-lock")
logout.click()
WebDriverWait(driver, 10).until( EC.url_contains("/login"))
assert "/login" in driver.current_url