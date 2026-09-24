from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

URL= "https://www.xyz.com/"
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.maximize_window()
driver.get(URL)

Login = (By.XPATH, "//a[@href= '/login']")
Home_banner = (By.XPATH, "//section[@id = 'slider']")
Signup_heading = (By.XPATH, "//div[@class = 'signup-form']//h2")
# Validate Home page
assert driver.find_element(*Home_banner).is_displayed()

# Validate Sign up page
driver.find_element(*Login).click()
Signup_heading = driver.find_element(By.XPATH, "//div[@class = 'signup-form']//h2").text
assert Signup_heading == "New User Signup!"

# Signup
driver.find_element(By.XPATH, '//input [@data-qa="signup-name"]').send_keys("Stephie")
driver.find_element(By.XPATH, '//input [@data-qa="signup-email"]').send_keys("stephie3@yopmail.com")
driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
    (By.XPATH, "//h2[contains(., 'Account Information')]")))
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("2026")


# Date select
def select_date(driver, date_input):
    day, month, year = date_input.split("/")
    Select(driver.find_element(By.ID, "days")).select_by_value(day)
    Select(driver.find_element(By.ID, "months")).select_by_value(month)
    Select(driver.find_element(By.ID, "years")).select_by_value(year)
select_date(driver, "4/5/1995")
# Checkboxes select
Checkboxes = driver.find_elements(By.XPATH, "//div[@class='checkbox']")
for Checkbox in Checkboxes:
    Checkbox.click()

# Address selection
Fname = "Stephie"
def enter_address(driver, Fname,Lname, address,state,city,zip,Mobile ):
    driver.find_element(By.ID, "first_name").send_keys(Fname)
    driver.find_element(By.ID, "last_name").send_keys(Lname)
    driver.find_element(By.ID, "address1").send_keys(address)
    driver.find_element(By.ID, "state").send_keys(state)
    driver.find_element(By.ID, "city").send_keys(city)
    driver.find_element(By.ID, "zipcode").send_keys(zip)
    driver.find_element(By.ID, "mobile_number").send_keys(Mobile)
enter_address(driver, Fname, "Doe", "ABC","ABC", "ABC", "1234", "123456789")
driver.find_element(By.CSS_SELECTOR, "button[data-qa='create-account']").click()

# Verify Account creation and continue
Success_msg = driver.find_element(By.CLASS_NAME, "text-center").text
assert "Account Created!" == Success_msg
driver.find_element(By.CLASS_NAME, "btn-primary").click()

# Verify Correct User Login
element = driver.find_element(By.CSS_SELECTOR, "a")
assert f"Logged in as {Fname}" in element.text

# Delete Account and click Continue
driver.find_element(By.XPATH, "//a[@href ='/delete_account'] ").click()
Deleted_msg = driver.find_element(By.CLASS_NAME, "text-center").text
if Deleted_msg== "Account Deleted!":
    driver.find_element(By.CLASS_NAME, "btn-primary").click()