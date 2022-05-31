from appium import webdriver
import time

from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_cap = {
  "Appium:deviceName": "Android Emulator",
  "platformName": "Android",
  "Appium:appPackage": "com.ril.ajio",
  "Appium:appWaitActivity": "com.ril.ajio.home.AjioHomeActivity",
  "Appium:app": "C:\\Users\\RAJASEKHAR\\Downloads\\ajio-7-13-0.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)
driver.find_element_by_id("com.ril.ajio:id/lsccmVAjio").click()
driver.find_element_by_id("com.ril.ajio:id/llpsTvSearch").click()
driver.find_element_by_id("com.ril.ajio:id/searchETV").send_keys("tops")
driver.find_element_by_id("com.ril.ajio:id/search_image").click()
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup[1]/android.widget.LinearLayout[3]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.ImageView[1]").click()
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(533, 1932)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(547, 400)
actions.w3c_actions.pointer_action.release()
actions.perform()
