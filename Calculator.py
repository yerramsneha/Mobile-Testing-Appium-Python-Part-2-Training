from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

desired_cap = {
  "appium:deviceName": "Android Emulator",
  "platformName": "Android",
  "appium:appPackage": "com.android2.calculator3",
  "appium:appWaitActivity": "com.xlythe.calculator.material.Theme.Orange",
  "appium:app": "C:\\Users\\ustmtest04\\Downloads\\Calculator.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

# find_element_by_id , send_keys() , click()
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("10")
driver.find_element_by_id("com.android2.calculator3:id/op_add").click()
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("40")
driver.find_element_by_id("com.android2.calculator3:id/eq").click()
# Screenshot of the current activity
filename = activityname + s
driver.save_screenshot("/Users/ustmtest04/PycharmProjects/pythonProject/screenshot/"+filename+".png")

# TouchAction() , tap() , perform()
sub = driver.find_element_by_id("com.android2.calculator3:id/op_sub")
num = driver.find_element_by_id("com.android2.calculator3:id/digit_5")
equ = driver.find_element_by_id("com.android2.calculator3:id/eq")
touch = TouchAction(driver)
touch.tap(sub).perform()
touch.tap(num).perform()
touch.tap(equ).perform()

# Screenshot
s = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
# This is the current activity
filename1 = activityname + s
driver.save_screenshot("/Users/ustmtest04/PycharmProjects/pythonProject/screenshot/"+filename1+".png")






