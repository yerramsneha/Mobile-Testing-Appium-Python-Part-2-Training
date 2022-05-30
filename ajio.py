import time

from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_cap = {
  "appium:deviceName": "Android Emulator",
  "platformName": "Android",
  "appium:appPackage": "com.ril.ajio",
  "appium:appWaitActivity": "com.ril.ajio.home.AjioHomeActivity",
  "appium:app": "C:\\Users\\Vishnu Anand\\Downloads\\com.ril.ajio_2022-05-09.apk"}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)
driver.find_element_by_id("com.ril.ajio:id/lsccmVAjio").click()
driver.find_element_by_id("com.ril.ajio:id/touch_outside").click()
driver.find_element_by_id("com.ril.ajio:id/llpsTvSearch").click()
driver.find_element_by_id("com.ril.ajio:id/searchETV").send_keys("bags")
driver.find_element_by_id("com.ril.ajio:id/search_image").click()
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.ImageView[1]").click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(533, 1932)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(547, 400)
actions.w3c_actions.pointer_action.release()
actions.perform()

s = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
filename = activityname + s
driver.save_screenshot("/Users/Vishnu Anand/PycharmProjects/pythonProject4/screenshot/" + filename + ".png")
