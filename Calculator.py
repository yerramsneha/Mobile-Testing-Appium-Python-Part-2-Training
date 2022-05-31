from appium import webdriver
import time
desired_cap = {"appium:deviceName": "Android Emulator",
  "platformName": "Android",
  "appium:appPackage": "com.android2.calculator3",
  "appium:appWaitActivity": "com.xlythe.calculator.material.Theme.Orange",
  "appium:app": "C:\\Users\\meenu\\Downloads\\Calculator (1).apk"}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("8")
driver.find_element_by_id("com.android2.calculator3:id/op_add").click()
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("9")
driver.find_element_by_id("com.android2.calculator3:id/eq").click()
s = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
filename = activityname + s
driver.save_screenshot("/Users/meenu/PycharmProjects/pythonProject1/" + filename + ".png")

