import time
from appium import webdriver
desired_cap = {
 "appium:deviceName": "Android Emulator",
 "platformName": "Android",
 "appium:appPackage": "com.android2.calculator3",
 "appium:appWaitActivity": "com.xlythe.calculator.material.Theme.Orange",
 "appium:app": "C:\\Users\\ustmtest09\\Downloads\\Calculator.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("5")
driver.find_element_by_id("com.android2.calculator3:id/op_add").click()
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("1")
driver.find_element_by_id("com.android2.calculator3:id/eq").click()
s = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
filename = activityname + s
driver.save_screenshot("/Users/ustmtest09/PycharmProjects/pythonProject/" + filename + ".png")
