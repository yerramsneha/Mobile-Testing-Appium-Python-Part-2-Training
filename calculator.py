from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

desired_cap = {
  "appium:deviceName": "Android Emulator",
  "platformName": "Android",
  "appium:appPackage": "com.android2.calculator3",
  "appium:appWaitActivity": "com.xlythe.calculator.material.Theme.Orange",
  "appium:app": "C:\\Users\\ustmtest05\\Downloads\\Calculator.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

# find_element_by_id , send_keys() , click()
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("20")
driver.find_element_by_id("com.android2.calculator3:id/op_add").click()
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("30")
driver.find_element_by_id("com.android2.calculator3:id/eq").click()

#TouchAction() , tap() , perform()
sub = driver.find_element_by_id("com.android2.calculator3:id/op_sub")
num = driver.find_element_by_id("com.android2.calculator3:id/digit_2")
equ = driver.find_element_by_id("com.android2.calculator3:id/eq")
touch = TouchAction(driver)
touch.tap(sub).perform()
touch.tap(num).perform()
touch.tap(equ).perform()

#Screenshot
s = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
# this is the current activity
filename = activityname + s
driver.save_screenshot("/Users/ustmtest05/PycharmProjects/pythonProject/screenshot/"+filename+".png")