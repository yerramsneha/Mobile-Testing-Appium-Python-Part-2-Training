from appium import webdriver
import time


from appium.webdriver.common.touch_action import TouchAction

desired_cap = {"appium:deviceName": "Android Emulator",
  "platformName": "Android",
  "appium:appPackage": "com.android2.calculator3",
  "appium:appWaitActivity": "com.xlythe.calculator.material.Theme.Orange",
  "appium:app": "C:\\Users\\RAJASEKHAR\\Downloads\\Calculator.apk"}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("2")
driver.find_element_by_id("com.android2.calculator3:id/op_add").click()
driver.find_element_by_id("com.android2.calculator3:id/formula").send_keys("5")
driver.find_element_by_id("com.android2.calculator3:id/eq").click()
s = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
filename = activityname + s
driver.save_screenshot("/Users/RAJASEKHAR/PycharmProjects/pythonProject/screen shot/" + filename + ".png")
touch = TouchAction(driver)
touch.press(x=320,y=722).move_to(x=320,y=430).release().perform()
for i in range(5):
  touch = TouchAction(driver)
  touch.press(x=320, y=722).move_to(x=320, y=430).release().perform()
  time.sleep(3)

