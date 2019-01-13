import config
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.pythonanywhere.com/login/?next=/")
driver.find_element_by_id('id_auth-username').send_keys(config.USERNAME)
driver.find_element_by_id('id_auth-password').send_keys(config.PASSWORD)
driver.find_element_by_id('id_next').click()

driver.find_element_by_id('id_web_app_link').click()
driver.find_element_by_class_name('webapp_extend').click()
print('Done')

