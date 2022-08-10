

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait



service_obj = Service("C:\\Users\\q1015716\\Desktop\\PythonRecordings\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://yocket.com/feed")
driver.maximize_window()
driver.implicitly_wait(10)

errmsg = "Required field"
driver.find_element(By.XPATH, "//span[text()='College Finder']").click()
driver.find_element(By.XPATH, "//button[normalize-space(text())='Masters']").click()

driver.find_element(By.XPATH, "//button[normalize-space(text())='Next']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Select Country']").send_keys("United")
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//ul[@class='vs__dropdown-menu']")))
countries = driver.find_elements(By.XPATH, "//ul[@class='vs__dropdown-menu']/li")
for country in countries:
    if country.text == "United Kingdom":
        country.click()
        break

driver.find_element(By.XPATH, "//input[@placeholder='Select Major']").send_keys("Computer")
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//ul[@class='vs__dropdown-menu']")))
courses = driver.find_elements(By.XPATH, "//ul/li[@class='vs__dropdown-option']")
for subject in courses:
    if subject.text == "Computer Engineering":
        subject.click()
        break

driver.find_element(By.XPATH, "//button[normalize-space(text())='Next']").click()

driver.find_element(By.XPATH, "//input[@placeholder='Select College']").send_keys("Biju")
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//ul[@class='vs__dropdown-menu']")))
colleges = driver.find_elements(By.XPATH, "//ul/li[@class='vs__dropdown-option']")
for colg in colleges:
    if colg.text == "Bijupattnaik University Of Technology, Rourkela":
        colg.click()
        break

driver.find_element(By.XPATH, "//input[@placeholder='Select Major']").send_keys("Computer")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//li[@id='vs6__option-3']")))
courses = driver.find_elements(By.XPATH, "//ul[@class='vs__dropdown-menu']/li")
for subject in courses:
    if subject.text == "Computer Science":
        subject.click()
        break

dropdown = Select(driver.find_element(By.ID, 'marks_type'))
dropdown.select_by_index(3)
dropdown.select_by_value('100')
dropdown.select_by_visible_text('4 GPA')
dropdown.select_by_visible_text('10 CGPA')
driver.find_element(By.ID, 'marks').send_keys('8')
driver.find_element(By.XPATH, "//button[normalize-space(text())='Next']").click()
wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Next']")))
driver.find_element(By.XPATH, "//button[normalize-space(text())='Next']").click()
driver.find_element(By.XPATH, "//button[normalize-space(text())='Find Universities']").click()
driver.find_element(By.XPATH, "//button[normalize-space(text())='Log in']").click()
driver.find_element(By.XPATH, "//span[normalize-space(text())='Login with Email']").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("swagatikameher@outlook.com")
driver.find_element(By.XPATH, "//button[normalize-space(text())='Request Code']").click()
driver.execute_script("window.open('https://outlook.live.com/owa/')")
newwindow = driver.window_handles
driver.switch_to.window(newwindow[1])
driver.find_element(By.XPATH, "(//li/a[text()='Sign in'])[1]").click()
driver.find_element(By.NAME, 'loginfmt').send_keys("swagatikameher@outlook.com")
driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']")))
driver.find_element(By.NAME, 'passwd').send_keys("Ihatemylife@123")
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//input[@id='idSIButton9']")))
driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@id='idSIButton9']")))
driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys('hello@yocket.in')
driver.find_element(By.XPATH, "//i[@data-icon-name='Search']").click()
results = driver.find_element(By.XPATH, '//div[@id="groupHeaderAll results"]/following-sibling::div')
lst = results.text.split(" ")
for i in lst:
    if i.isdigit():
        driver.switch_to.window(newwindow[0])
        driver.find_element(By.ID, 'firstInput').send_keys(i)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Verify and Proceed']")))
        driver.find_element(By.XPATH, "//button[normalize-space(text())='Verify and Proceed']").click()
        # if driver.find_element(By.XPATH, "//button[starts-with(@class, 'absolute top')]").is_displayed():
        #     driver.find_element(By.XPATH, "//button[starts-with(@class, 'absolute top')]").click()
        dropdown = Select(driver.find_element(By.XPATH, "//select[starts-with(@class, 'text-md bg-trans')]"))
        dropdown.select_by_visible_text('Cost')
        University_name = driver.find_element(By.XPATH, "//div[starts-with(@class, 'grid grid-cols')]/div/div[3]/p/a")
        print(University_name.text)
        driver.quit()